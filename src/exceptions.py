"""
Excepciones personalizadas para Weather CLI.

Este módulo define una jerarquía de excepciones específicas para el dominio
de la aplicación de clima, permitiendo manejo granular de diferentes tipos
de errores que pueden ocurrir durante la consulta a la API de OpenWeatherMap.

La jerarquía es:
    Exception (built-in)
    ├── WeatherAPIException (base para errores de API)
    │   ├── CityNotFoundException (ciudad no encontrada - 404)
    │   ├── InvalidAPIKeyException (API key inválida - 401)
    │   └── NetworkException (problemas de red/timeout)
    └── ConfigurationException (problemas de configuración)

Esta estructura permite capturar excepciones en diferentes niveles de
especificidad según sea necesario.

Example:
    >>> from src.exceptions import CityNotFoundException
    >>> try:
    ...     raise CityNotFoundException("Atlantis")
    ... except CityNotFoundException as e:
    ...     print(e)
    No se encontró la ciudad: Atlantis
"""


class WeatherAPIException(Exception):
    """
    Excepción base para todos los errores relacionados con la API del clima.
    
    Esta clase sirve como padre para todas las excepciones específicas de
    la API de OpenWeatherMap, permitiendo capturar cualquier error de API
    con un solo except si es necesario.
    
    No se debería instanciar directamente; usar las subclases específicas.
    
    Example:
        >>> try:
        ...     # Código que puede lanzar cualquier error de API
        ...     pass
        ... except WeatherAPIException as e:
        ...     # Captura CityNotFound, InvalidAPIKey, Network, etc.
        ...     print(f"Error de API: {e}")
    """

    pass


class CityNotFoundException(WeatherAPIException):
    """
    Se lanza cuando la ciudad buscada no se encuentra en la API de OpenWeatherMap.
    
    Esta excepción corresponde a un error HTTP 404 de la API, indicando que
    el nombre de ciudad no existe en la base de datos de OpenWeatherMap o
    está mal escrito.
    
    Attributes:
        city_name (str): Nombre de la ciudad que no fue encontrada.
    
    Example:
        >>> raise CityNotFoundException("Gotham")
        Traceback (most recent call last):
        ...
        CityNotFoundException: No se encontró la ciudad: Gotham
    
    Note:
        Sugerencias al usuario: verificar ortografía, probar nombre en inglés,
        o agregar código de país (ej: "Paris,FR").
    """

    def __init__(self, city_name: str):
        """
        Inicializa la excepción con el nombre de la ciudad no encontrada.
        
        Args:
            city_name (str): Nombre de la ciudad que causó el error.
        """
        self.city_name = city_name
        super().__init__(f"No se encontró la ciudad: {city_name}")


class InvalidAPIKeyException(WeatherAPIException):
    """
    Se lanza cuando la API key es inválida, expirada o no está autorizada.
    
    Esta excepción corresponde a un error HTTP 401 de la API, indicando que
    la API key proporcionada no es válida o no tiene permisos.
    
    Causas comunes:
    - API key incorrecta o con typo
    - API key recién creada (puede tardar 10-30 min en activarse)
    - API key revocada o expirada
    - Límites de rate limiting excedidos
    
    Example:
        >>> raise InvalidAPIKeyException()
        Traceback (most recent call last):
        ...
        InvalidAPIKeyException: API key inválida. Verifica tu configuración en el archivo .env
    
    Note:
        Si la API key es nueva, esperar 10-30 minutos antes de volver a intentar.
    """

    def __init__(self):
        """Inicializa la excepción con un mensaje estándar de API key inválida."""
        super().__init__(
            "API key inválida. Verifica tu configuración en el archivo .env"
        )


class ConfigurationException(Exception):
    """
    Se lanza cuando hay problemas con la configuración de la aplicación.
    
    Esta excepción NO hereda de WeatherAPIException porque representa un
    error de configuración local (antes de contactar la API), no un error
    de la API externa.
    
    Causas comunes:
    - Falta el archivo .env
    - Variable OPENWEATHER_API_KEY no está definida
    - API key es el placeholder "your_api_key_here"
    - Timeout configurado <= 0
    
    Example:
        >>> raise ConfigurationException("Falta API key")
        Traceback (most recent call last):
        ...
        ConfigurationException: Falta API key
    
    Note:
        Esta excepción debe manejarse al inicio de la aplicación para
        fallar rápido con mensaje claro antes de intentar usar la API.
    """

    pass


class NetworkException(WeatherAPIException):
    """
    Se lanza cuando hay problemas de red o timeout al consultar la API.
    
    Esta excepción agrupa todos los errores relacionados con la conectividad
    de red, no con la respuesta de la API (que tendría status codes).
    
    Causas comunes:
    - Timeout (la API no responde en el tiempo configurado)
    - Sin conexión a internet
    - DNS no resuelve el dominio de la API
    - Firewall bloqueando la conexión
    - Proxy mal configurado
    
    Args:
        message (str): Mensaje descriptivo del error de red.
            Default: "Error de conexión con la API".
    
    Example:
        >>> raise NetworkException("Timeout después de 10 segundos")
        Traceback (most recent call last):
        ...
        NetworkException: Timeout después de 10 segundos
    
    Note:
        Si hay timeouts frecuentes, considerar aumentar REQUEST_TIMEOUT en .env
    """

    def __init__(self, message: str = "Error de conexión con la API"):
        """
        Inicializa la excepción con un mensaje de error de red.
        
        Args:
            message (str): Descripción específica del problema de red.
        """
        super().__init__(message)
