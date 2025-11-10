"""Entry point principal del CLI de consulta de clima."""

import sys
from typing import NoReturn

from .weather_service import WeatherService
from .weather_formatter import WeatherFormatter
from .exceptions import (
    CityNotFoundException,
    InvalidAPIKeyException,
    NetworkException,
    WeatherAPIException,
    ConfigurationException,
)


def main() -> NoReturn:
    """
    Función principal del CLI de consulta de clima.

    Esta función coordina el flujo completo de la aplicación:
    1. Muestra mensaje de bienvenida al usuario
    2. Solicita el nombre de una ciudad
    3. Valida que el input no esté vacío
    4. Consulta la API de OpenWeatherMap
    5. Procesa y formatea la respuesta
    6. Muestra el clima en formato amigable
    
    El flujo incluye manejo exhaustivo de errores para todos los casos
    posibles (ciudad no encontrada, API key inválida, problemas de red,
    errores de configuración, etc.).
    
    Returns:
        NoReturn: Esta función siempre termina con sys.exit() y nunca retorna.
    
    Note:
        La función captura KeyboardInterrupt (Ctrl+C) para permitir salida
        limpia del programa sin stack trace.
    
    Example:
        >>> # Al ejecutar el programa
        >>> main()
        🌍 Weather CLI - Consulta el clima de cualquier ciudad
        ============================================================
        
        Ingresa el nombre de la ciudad: Buenos Aires
        
        🌍 Consultando el clima de: Buenos Aires
        
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                   CLIMA EN BUENOS AIRES, AR
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        ...
    """
    try:
        # Mostrar mensaje de bienvenida al usuario
        print(WeatherFormatter.format_welcome())

        # Inicializar el servicio de clima y validar configuración (API key, timeout, etc.)
        weather_service = WeatherService()

        # Solicitar el nombre de la ciudad al usuario y limpiar espacios en blanco
        city = input(WeatherFormatter.format_city_prompt()).strip()

        # Validar que el usuario haya ingresado algo (no string vacío)
        if not city:
            print(WeatherFormatter.format_error("Debes ingresar el nombre de una ciudad"))
            sys.exit(1)

        # Mostrar feedback visual mientras se consulta la API
        print(WeatherFormatter.format_loading(city))

        # Obtener datos del clima desde OpenWeatherMap API (puede lanzar excepciones)
        weather_data = weather_service.get_weather(city)

        # Extraer y estructurar solo los campos relevantes del JSON de la API
        parsed_data = weather_service.parse_weather_data(weather_data)

        # Formatear los datos en texto amigable con emojis y mostrar al usuario
        print(WeatherFormatter.format_weather(parsed_data))

        # Salir con código 0 indicando ejecución exitosa
        sys.exit(0)

    # Manejo de error de configuración (falta API key o está mal configurada)
    except ConfigurationException as e:
        print(WeatherFormatter.format_error(str(e)))
        sys.exit(1)

    # Manejo de ciudad no encontrada (API retorna 404)
    except CityNotFoundException as e:
        print(WeatherFormatter.format_error(str(e)))
        print("💡 Sugerencia: Verifica que el nombre de la ciudad esté bien escrito.\n")
        sys.exit(1)

    # Manejo de API key inválida o no autorizada (API retorna 401)
    except InvalidAPIKeyException as e:
        print(WeatherFormatter.format_error(str(e)))
        sys.exit(1)

    # Manejo de problemas de red (timeout, sin conexión, etc.)
    except NetworkException as e:
        print(WeatherFormatter.format_error(str(e)))
        sys.exit(1)

    # Manejo de otros errores de la API (500, errores de parseo, etc.)
    except WeatherAPIException as e:
        print(WeatherFormatter.format_error(f"Error de la API: {str(e)}"))
        sys.exit(1)

    # Manejo de Ctrl+C para salida limpia sin stack trace
    except KeyboardInterrupt:
        print("\n\n👋 ¡Hasta luego!\n")
        sys.exit(0)

    # Catch-all para cualquier error inesperado no manejado específicamente
    except Exception as e:
        print(WeatherFormatter.format_error(f"Error inesperado: {str(e)}"))
        sys.exit(1)


if __name__ == "__main__":
    main()
