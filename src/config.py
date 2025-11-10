"""
Configuración de la aplicación y carga de variables de entorno.

Este módulo maneja toda la configuración centralizada de la aplicación Weather CLI,
incluyendo la carga de variables de entorno desde archivo .env, validación de
configuración requerida, y construcción de URLs para la API de OpenWeatherMap.

La configuración se implementa como atributos de clase en vez de instancia para
permitir acceso global sin necesidad de instanciar objetos.

Variables de entorno utilizadas:
    - OPENWEATHER_API_KEY (obligatoria): API key de OpenWeatherMap
    - WEATHER_LANG (opcional): Idioma de respuestas (default: 'es')
    - REQUEST_TIMEOUT (opcional): Timeout HTTP en segundos (default: 10)

Example:
    >>> from src.config import Config
    >>> Config.validate()  # Valida que API key esté configurada
    >>> url = Config.get_api_url("Madrid")
    >>> print(url)
    https://api.openweathermap.org/data/2.5/weather?q=Madrid&appid=...
"""

import os
from typing import Optional

from dotenv import load_dotenv

from .exceptions import ConfigurationException

# Cargar variables de entorno desde archivo .env en la raíz del proyecto
load_dotenv()


class Config:
    """
    Configuración centralizada de la aplicación Weather CLI.
    
    Clase que encapsula toda la configuración necesaria para interactuar
    con la API de OpenWeatherMap, cargando valores desde variables de entorno
    con defaults razonables cuando aplica.
    
    Todos los atributos son de clase (no de instancia) para permitir acceso
    global sin necesidad de instanciar. Se usa como un singleton de configuración.
    
    Attributes:
        BASE_URL (str): URL base de la API de OpenWeatherMap (weather endpoint).
        API_KEY (Optional[str]): API key de OpenWeatherMap, cargada desde variable
            de entorno OPENWEATHER_API_KEY. None si no está configurada.
        LANG (str): Código de idioma para respuestas (es, en, fr, etc.).
            Default: 'es' (español).
        TIMEOUT (int): Timeout para peticiones HTTP en segundos. Default: 10.
    
    Example:
        >>> Config.validate()  # Verificar configuración antes de usar
        >>> print(Config.API_KEY)
        'abc123...'
        >>> print(Config.LANG)
        'es'
        >>> url = Config.get_api_url("Londres")
    
    Note:
        La API key DEBE estar configurada antes de usar el servicio.
        Llamar a validate() al inicio de la aplicación para verificar.
    """

    # URL base de la API de OpenWeatherMap (endpoint de clima actual)
    BASE_URL: str = "https://api.openweathermap.org/data/2.5/weather"

    # API key (cargada desde variable de entorno OPENWEATHER_API_KEY)
    # None si no está configurada
    API_KEY: Optional[str] = os.getenv("OPENWEATHER_API_KEY")

    # Idioma para las respuestas (por defecto español)
    # Valores posibles: es, en, fr, de, pt, it, ja, etc.
    LANG: str = os.getenv("WEATHER_LANG", "es")

    # Timeout para las peticiones HTTP en segundos
    # Aumentar si la conexión es lenta
    TIMEOUT: int = int(os.getenv("REQUEST_TIMEOUT", "10"))

    @classmethod
    def validate(cls) -> None:
        """
        Valida que la configuración esté correctamente establecida.
        
        Verifica que:
        1. La API key de OpenWeatherMap esté configurada
        2. La API key no sea el valor placeholder por defecto
        3. El timeout sea un valor positivo válido
        
        Esta función debe llamarse al inicio de la aplicación, típicamente
        en el constructor de WeatherService, para detectar problemas de
        configuración antes de intentar hacer requests a la API.

        Raises:
            ConfigurationException: Si la API key no está configurada, es el
                placeholder por defecto, o si el timeout es inválido (<=0).
        
        Example:
            >>> Config.validate()  # Si todo está bien, no hace nada
            >>> # Si falta API key, lanza ConfigurationException con mensaje
        
        Note:
            Es mejor fallar rápido con un mensaje claro que fallar después
            con un error HTTP 401 críptico.
        """
        # Verificar que la API key esté configurada y no sea el placeholder
        if not cls.API_KEY or cls.API_KEY == "your_api_key_here":
            raise ConfigurationException(
                "No se encontró la API key de OpenWeatherMap.\n"
                "Por favor:\n"
                "1. Copia el archivo .env.example a .env\n"
                "2. Obtén tu API key en https://openweathermap.org/api\n"
                "3. Configura OPENWEATHER_API_KEY en el archivo .env"
            )

        # Verificar que el timeout sea válido (mayor a 0)
        if cls.TIMEOUT <= 0:
            raise ConfigurationException("El timeout debe ser mayor a 0 segundos")

    @classmethod
    def get_api_url(cls, city: str) -> str:
        """
        Construye la URL completa para consultar el clima de una ciudad.
        
        Combina la URL base con todos los parámetros necesarios: nombre de ciudad,
        API key, idioma, y unidades de medida (métrico para Celsius).

        Args:
            city (str): Nombre de la ciudad a consultar. Puede incluir código de
                país para desambiguar (ej: "Paris,FR" vs "Paris,US").

        Returns:
            str: URL completa con query parameters listos para hacer GET request.
        
        Example:
            >>> url = Config.get_api_url("Madrid")
            >>> print(url)
            https://api.openweathermap.org/data/2.5/weather?q=Madrid&appid=...&lang=es&units=metric
            >>> url = Config.get_api_url("Paris,FR")
            >>> print(url)
            https://api.openweathermap.org/data/2.5/weather?q=Paris,FR&appid=...&lang=es&units=metric
        
        Note:
            - El parámetro units=metric hace que las temperaturas sean en Celsius
            - El idioma (lang) afecta la descripción del clima (ej: "cielo claro")
            - La API key se incluye como parámetro appid
        """
        return (
            f"{cls.BASE_URL}"
            f"?q={city}"
            f"&appid={cls.API_KEY}"
            f"&lang={cls.LANG}"
            f"&units=metric"  # Unidades métricas: Celsius, metros/segundo
        )
