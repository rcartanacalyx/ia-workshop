"""Fixtures con respuestas de ejemplo de la API de OpenWeatherMap."""


def get_successful_response():
    """Respuesta exitosa de la API para Buenos Aires."""
    return {
        "coord": {"lon": -58.3816, "lat": -34.6037},
        "weather": [
            {
                "id": 800,
                "main": "Clear",
                "description": "cielo claro",
                "icon": "01d",
            }
        ],
        "base": "stations",
        "main": {
            "temp": 25.5,
            "feels_like": 25.2,
            "temp_min": 24.0,
            "temp_max": 27.0,
            "pressure": 1013,
            "humidity": 65,
        },
        "visibility": 10000,
        "wind": {"speed": 3.5, "deg": 180},
        "clouds": {"all": 0},
        "dt": 1699632000,
        "sys": {
            "type": 1,
            "id": 8224,
            "country": "AR",
            "sunrise": 1699605600,
            "sunset": 1699653600,
        },
        "timezone": -10800,
        "id": 3435910,
        "name": "Buenos Aires",
        "cod": 200,
    }


def get_madrid_response():
    """Respuesta exitosa de la API para Madrid."""
    return {
        "coord": {"lon": -3.7026, "lat": 40.4165},
        "weather": [
            {
                "id": 803,
                "main": "Clouds",
                "description": "muy nuboso",
                "icon": "04d",
            }
        ],
        "base": "stations",
        "main": {
            "temp": 18.3,
            "feels_like": 17.8,
            "temp_min": 16.5,
            "temp_max": 20.1,
            "pressure": 1015,
            "humidity": 72,
        },
        "visibility": 10000,
        "wind": {"speed": 4.2, "deg": 270},
        "clouds": {"all": 75},
        "dt": 1699632000,
        "sys": {
            "type": 2,
            "id": 2007545,
            "country": "ES",
            "sunrise": 1699598400,
            "sunset": 1699636800,
        },
        "timezone": 3600,
        "id": 3117735,
        "name": "Madrid",
        "cod": 200,
    }


def get_not_found_response():
    """Respuesta de error 404 cuando la ciudad no existe."""
    return {"cod": "404", "message": "city not found"}


def get_unauthorized_response():
    """Respuesta de error 401 cuando la API key es inválida."""
    return {
        "cod": 401,
        "message": "Invalid API key. Please see https://openweathermap.org/faq#error401 for more info.",
    }


def get_malformed_response():
    """Respuesta malformada (sin campos esperados)."""
    return {
        "coord": {"lon": -58.3816, "lat": -34.6037},
        # Falta el campo "main" y otros campos críticos
        "name": "Test City",
        "cod": 200,
    }
