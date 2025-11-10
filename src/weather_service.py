"""Servicio para consultar el clima usando la API de OpenWeatherMap."""

from typing import Dict, Any
import requests

from .config import Config
from .exceptions import (
    CityNotFoundException,
    InvalidAPIKeyException,
    NetworkException,
    WeatherAPIException,
)


class WeatherService:
    """
    Servicio para interactuar con la API de OpenWeatherMap.
    
    Esta clase encapsula toda la lógica de comunicación con la API externa,
    incluyendo construcción de URLs, manejo de requests HTTP, validación de
    respuestas, y transformación de datos JSON a formato estructurado.
    
    La clase implementa manejo robusto de errores para todos los códigos HTTP
    posibles (200, 404, 401, 500) y excepciones de red (timeout, connection error).
    
    Attributes:
        No tiene atributos de instancia. Toda la configuración se obtiene
        de la clase Config (API key, timeout, idioma, etc.).
    
    Example:
        >>> service = WeatherService()
        >>> data = service.get_weather("Buenos Aires")
        >>> parsed = service.parse_weather_data(data)
        >>> print(parsed["temperature"])
        25.5
    
    Note:
        Para tests, se puede instanciar con skip_validation=True para omitir
        la validación de la API key y otras configuraciones.
    """

    def __init__(self, skip_validation=False):
        """
        Inicializa el servicio y valida la configuración.
        
        Al inicializar, se valida automáticamente que:
        - La API key de OpenWeatherMap esté configurada
        - La API key no sea el placeholder por defecto
        - El timeout sea mayor a 0 segundos
        
        Args:
            skip_validation (bool): Si es True, omite la validación de configuración.
                Útil para tests unitarios donde se mockean las configuraciones.
                Por defecto False.
        
        Raises:
            ConfigurationException: Si la validación falla (API key faltante,
                API key con valor placeholder, o timeout inválido).
        """
        if not skip_validation:
            Config.validate()

    def get_weather(self, city: str) -> Dict[str, Any]:
        """
        Obtiene la información del clima para una ciudad específica desde OpenWeatherMap.

        Realiza una petición HTTP GET a la API de OpenWeatherMap con el nombre de
        la ciudad, maneja la respuesta según el código HTTP, y retorna los datos
        del clima en formato JSON.
        
        El método valida el input, construye la URL con parámetros apropiados,
        realiza la request con timeout, y convierte códigos de error HTTP en
        excepciones específicas para manejo uniforme.

        Args:
            city (str): Nombre de la ciudad a consultar. Puede incluir país para
                desambiguar (ej: "Paris, FR"). Se limpia de espacios en blanco
                automáticamente.

        Returns:
            Dict[str, Any]: Respuesta JSON completa de la API de OpenWeatherMap
                conteniendo: coord, weather, main, wind, clouds, sys, name, etc.
                Ver: https://openweathermap.org/current#current_JSON

        Raises:
            ValueError: Si el nombre de la ciudad está vacío o es solo espacios.
            CityNotFoundException: Si la API retorna 404 (ciudad no encontrada).
            InvalidAPIKeyException: Si la API retorna 401 (API key inválida).
            NetworkException: Si hay timeout, error de conexión, o problemas de red.
            WeatherAPIException: Para otros errores HTTP (500, etc.) o errores
                inesperados de la API.
        
        Example:
            >>> service = WeatherService()
            >>> data = service.get_weather("Madrid")
            >>> print(data["name"])
            'Madrid'
            >>> print(data["main"]["temp"])
            18.3
        
        Note:
            El timeout por defecto es 10 segundos (configurable vía REQUEST_TIMEOUT
            en .env). Las temperaturas se retornan en Celsius (units=metric).
        """
        # Validar que el nombre de la ciudad no esté vacío
        if not city or not city.strip():
            raise ValueError("El nombre de la ciudad no puede estar vacío")

        # Limpiar espacios en blanco del nombre de la ciudad
        city = city.strip()
        
        # Construir URL completa con API key, idioma, y unidades métricas
        url = Config.get_api_url(city)

        try:
            # Realizar petición GET con timeout configurado
            response = requests.get(url, timeout=Config.TIMEOUT)

            # Manejo específico de códigos de estado HTTP
            if response.status_code == 200:
                # Éxito: retornar datos JSON de la API
                return response.json()

            elif response.status_code == 404:
                # Ciudad no encontrada en la base de datos de OpenWeatherMap
                raise CityNotFoundException(city)

            elif response.status_code == 401:
                # API key inválida, expirada, o no autorizada
                raise InvalidAPIKeyException()

            else:
                # Otros errores HTTP (500, 503, etc.)
                raise WeatherAPIException(
                    f"Error de la API: {response.status_code} - {response.text}"
                )

        except requests.exceptions.Timeout:
            # La API no respondió dentro del tiempo límite
            raise NetworkException(
                f"Timeout al intentar conectar con la API (>{Config.TIMEOUT}s)"
            )

        except requests.exceptions.ConnectionError:
            # No se pudo establecer conexión (sin internet, DNS falla, etc.)
            raise NetworkException(
                "No se pudo conectar con la API. Verifica tu conexión a internet."
            )

        except requests.exceptions.RequestException as e:
            # Otros errores de requests (SSL, redirect infinito, etc.)
            raise NetworkException(f"Error de red: {str(e)}")

    def parse_weather_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Parsea y estructura los datos relevantes del clima desde el JSON de la API.

        Extrae solo los campos necesarios del JSON completo de OpenWeatherMap,
        transformándolos a un diccionario estructurado más simple y consistente.
        También realiza pequeñas transformaciones como capitalizar la descripción.

        Args:
            data (Dict[str, Any]): Respuesta JSON completa de la API de OpenWeatherMap.
                Debe contener las claves: name, sys, main, weather, wind, coord.

        Returns:
            Dict[str, Any]: Diccionario con datos estructurados conteniendo:
                - city (str): Nombre de la ciudad
                - country (str): Código del país (AR, ES, US, etc.)
                - temperature (float): Temperatura actual en Celsius
                - feels_like (float): Sensación térmica en Celsius
                - description (str): Descripción del clima (Capitalizada)
                - humidity (int): Humedad en porcentaje
                - pressure (int): Presión atmosférica en hPa
                - wind_speed (float): Velocidad del viento en m/s
                - latitude (float): Latitud de la ciudad
                - longitude (float): Longitud de la ciudad

        Raises:
            WeatherAPIException: Si faltan campos esperados en el JSON (KeyError)
                o si la estructura es inválida (IndexError).
        
        Example:
            >>> api_response = {
            ...     "name": "Madrid",
            ...     "sys": {"country": "ES"},
            ...     "main": {"temp": 18.3, "feels_like": 17.8, "humidity": 72, "pressure": 1015},
            ...     "weather": [{"description": "muy nuboso"}],
            ...     "wind": {"speed": 4.2},
            ...     "coord": {"lat": 40.42, "lon": -3.7}
            ... }
            >>> service = WeatherService(skip_validation=True)
            >>> parsed = service.parse_weather_data(api_response)
            >>> print(parsed["city"])
            'Madrid'
            >>> print(parsed["description"])
            'Muy nuboso'
        
        Note:
            La descripción del clima se capitaliza automáticamente para mejor
            presentación (ej: "cielo claro" → "Cielo claro").
        """
        try:
            return {
                "city": data["name"],
                "country": data["sys"]["country"],
                "temperature": data["main"]["temp"],
                "feels_like": data["main"]["feels_like"],
                # Capitalizar primera letra de la descripción para mejor formato
                "description": data["weather"][0]["description"].capitalize(),
                "humidity": data["main"]["humidity"],
                "pressure": data["main"]["pressure"],
                "wind_speed": data["wind"]["speed"],
                "latitude": data["coord"]["lat"],
                "longitude": data["coord"]["lon"],
            }
        except (KeyError, IndexError) as e:
            # Faltan campos esperados o estructura JSON inválida
            raise WeatherAPIException(f"Error al parsear los datos de la API: {str(e)}")
