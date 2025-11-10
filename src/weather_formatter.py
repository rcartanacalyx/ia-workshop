"""Formateador de datos del clima para salida en consola."""

from typing import Dict, Any


class WeatherFormatter:
    """
    Clase para formatear datos del clima en texto descriptivo amigable para consola.
    
    Esta clase proporciona métodos estáticos para transformar datos estructurados
    del clima en strings formateados con emojis, colores ASCII, y formato legible.
    
    Todas las funciones son estáticas ya que no mantienen estado y solo realizan
    transformaciones de formato. Se usa como una utilidad de presentación.
    
    Attributes:
        EMOJIS (Dict[str, str]): Diccionario de emojis utilizados en el formateo.
            Incluye: globe, thermometer, cloud, droplet, wind, gauge, pin.
    
    Example:
        >>> data = {
        ...     "city": "Madrid", "country": "ES", "temperature": 18.3,
        ...     "description": "Muy nuboso", "humidity": 72,
        ...     "wind_speed": 4.2, "pressure": 1015,
        ...     "latitude": 40.42, "longitude": -3.7
        ... }
        >>> output = WeatherFormatter.format_weather(data)
        >>> print(output)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                   CLIMA EN MADRID, ES
        ...
    
    Note:
        Todos los métodos son @staticmethod ya que no requieren instancia.
        La clase funciona como un namespace para funciones de formateo.
    """

    # Emojis para decorar la salida visual del CLI
    EMOJIS = {
        "globe": "🌍",
        "thermometer": "🌡️",
        "cloud": "☁️",
        "droplet": "💧",
        "wind": "💨",
        "gauge": "🎚️",
        "pin": "📍",
    }

    @staticmethod
    def format_weather(weather_data: Dict[str, Any]) -> str:
        """
        Formatea los datos del clima en un texto descriptivo amigable con emojis.

        Toma los datos estructurados del clima y genera un string multilinea
        con formato visual atractivo incluyendo emojis, líneas decorativas,
        y conversión de unidades para mejor comprensión del usuario.

        Args:
            weather_data (Dict[str, Any]): Diccionario con datos del clima parseados.
                Debe contener las claves: city, country, temperature, description,
                humidity, wind_speed, pressure, latitude, longitude.

        Returns:
            str: String formateado con múltiples líneas conteniendo toda la
                información del clima en formato legible con emojis y decoración.
        
        Example:
            >>> data = {
            ...     "city": "Buenos Aires", "country": "AR",
            ...     "temperature": 25.5, "description": "Cielo claro",
            ...     "humidity": 65, "wind_speed": 3.5,
            ...     "pressure": 1013, "latitude": -34.60, "longitude": -58.38
            ... }
            >>> output = WeatherFormatter.format_weather(data)
            >>> print(output)
            ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                       CLIMA EN BUENOS AIRES, AR
            ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            
            🌡️  Temperatura: 25.5°C
            ☁️  Condición: Cielo claro
            💧 Humedad: 65%
            💨 Viento: 3.5 m/s (12.6 km/h)
            🎚️  Presión: 1013 hPa
            📍 Coordenadas: -34.6, -58.38
            ...
        
        Note:
            - La velocidad del viento se convierte automáticamente de m/s a km/h
            - Las temperaturas están en Celsius
            - Se usan caracteres Unicode (━) para las líneas decorativas
        """
        # Extraer datos del diccionario
        city = weather_data["city"]
        country = weather_data["country"]
        temp = weather_data["temperature"]
        description = weather_data["description"]
        humidity = weather_data["humidity"]
        wind_speed = weather_data["wind_speed"]
        pressure = weather_data["pressure"]
        lat = weather_data["latitude"]
        lon = weather_data["longitude"]

        # Convertir velocidad del viento de m/s a km/h (multiplicar por 3.6)
        wind_kmh = wind_speed * 3.6

        # Línea decorativa usando caracteres Unicode
        separator = "━" * 45

        # Construir string formateado con f-string multilínea
        output = f"""
{separator}
           CLIMA EN {city.upper()}, {country}
{separator}

{WeatherFormatter.EMOJIS['thermometer']}  Temperatura: {temp}°C
{WeatherFormatter.EMOJIS['cloud']}  Condición: {description}
{WeatherFormatter.EMOJIS['droplet']} Humedad: {humidity}%
{WeatherFormatter.EMOJIS['wind']} Viento: {wind_speed} m/s ({wind_kmh:.1f} km/h)
{WeatherFormatter.EMOJIS['gauge']}  Presión: {pressure} hPa
{WeatherFormatter.EMOJIS['pin']} Coordenadas: {lat}, {lon}

{separator}
"""
        return output

    @staticmethod
    def format_error(error_message: str) -> str:
        """
        Formatea un mensaje de error de forma amigable con emoji de error.

        Agrega emoji de cruz roja (❌) y formato consistente para todos
        los mensajes de error del CLI.

        Args:
            error_message (str): Mensaje de error a formatear.

        Returns:
            str: String formateado con el error, emoji, y líneas en blanco.
        
        Example:
            >>> error = WeatherFormatter.format_error("Ciudad no encontrada")
            >>> print(error)
            
            ❌ Error: Ciudad no encontrada
            
        """
        return f"\n❌ Error: {error_message}\n"

    @staticmethod
    def format_welcome() -> str:
        """
        Genera el mensaje de bienvenida del CLI con emoji y separador.

        Muestra el título de la aplicación con emoji de globo terráqueo
        y una línea de iguales como separador visual.

        Returns:
            str: String con el mensaje de bienvenida formateado.
        
        Example:
            >>> welcome = WeatherFormatter.format_welcome()
            >>> print(welcome)
            
            🌍 Weather CLI - Consulta el clima de cualquier ciudad
            ============================================================
            
        """
        return f"""
{WeatherFormatter.EMOJIS['globe']} Weather CLI - Consulta el clima de cualquier ciudad
{'=' * 60}
"""

    @staticmethod
    def format_city_prompt() -> str:
        """
        Genera el prompt para solicitar el nombre de la ciudad al usuario.

        Texto que se muestra para pedir input al usuario.

        Returns:
            str: String con el prompt para solicitar ciudad.
        
        Example:
            >>> prompt = WeatherFormatter.format_city_prompt()
            >>> city = input(prompt)  # Usuario ingresa "Madrid"
        """
        return "\nIngresa el nombre de la ciudad: "

    @staticmethod
    def format_loading(city: str) -> str:
        """
        Genera el mensaje de carga mientras se consulta la API.

        Muestra feedback visual al usuario indicando que se está
        procesando su consulta.

        Args:
            city (str): Nombre de la ciudad que se está consultando.

        Returns:
            str: String con el mensaje de carga incluyendo nombre de ciudad.
        
        Example:
            >>> loading = WeatherFormatter.format_loading("París")
            >>> print(loading)
            
            🌍 Consultando el clima de: París
        """
        return f"\n{WeatherFormatter.EMOJIS['globe']} Consultando el clima de: {city}"
