"""Tests para el formateador de clima."""

import pytest
from src.weather_formatter import WeatherFormatter


class TestWeatherFormatter:
    """Tests para la clase WeatherFormatter."""

    @pytest.fixture
    def sample_weather_data(self):
        """Fixture con datos de clima de ejemplo."""
        return {
            "city": "Buenos Aires",
            "country": "AR",
            "temperature": 25.5,
            "feels_like": 25.2,
            "description": "Cielo claro",
            "humidity": 65,
            "pressure": 1013,
            "wind_speed": 3.5,
            "latitude": -34.6037,
            "longitude": -58.3816,
        }

    def test_format_weather_includes_city_name(self, sample_weather_data):
        """Verifica que el formato incluya el nombre de la ciudad."""
        result = WeatherFormatter.format_weather(sample_weather_data)
        
        assert "BUENOS AIRES" in result
        assert "AR" in result

    def test_format_weather_includes_temperature_celsius(self, sample_weather_data):
        """Verifica que el formato incluya temperatura en Celsius."""
        result = WeatherFormatter.format_weather(sample_weather_data)
        
        assert "25.5°C" in result
        assert "°F" not in result  # NO debe incluir Fahrenheit

    def test_format_weather_includes_description(self, sample_weather_data):
        """Verifica que el formato incluya la descripción del clima."""
        result = WeatherFormatter.format_weather(sample_weather_data)
        
        assert "Cielo claro" in result

    def test_format_weather_includes_humidity(self, sample_weather_data):
        """Verifica que el formato incluya la humedad."""
        result = WeatherFormatter.format_weather(sample_weather_data)
        
        assert "65%" in result
        assert "Humedad" in result

    def test_format_weather_includes_wind_speed(self, sample_weather_data):
        """Verifica que el formato incluya la velocidad del viento."""
        result = WeatherFormatter.format_weather(sample_weather_data)
        
        assert "3.5 m/s" in result

    def test_format_weather_converts_wind_to_kmh(self, sample_weather_data):
        """Verifica que el formato convierta m/s a km/h."""
        result = WeatherFormatter.format_weather(sample_weather_data)
        
        # 3.5 m/s = 12.6 km/h
        assert "12.6 km/h" in result

    def test_format_weather_includes_pressure(self, sample_weather_data):
        """Verifica que el formato incluya la presión."""
        result = WeatherFormatter.format_weather(sample_weather_data)
        
        assert "1013 hPa" in result

    def test_format_weather_includes_coordinates(self, sample_weather_data):
        """Verifica que el formato incluya las coordenadas."""
        result = WeatherFormatter.format_weather(sample_weather_data)
        
        assert "-34.6037" in result
        assert "-58.3816" in result

    def test_format_weather_includes_emojis(self, sample_weather_data):
        """Verifica que el formato incluya emojis."""
        result = WeatherFormatter.format_weather(sample_weather_data)
        
        assert "🌡️" in result  # Temperatura
        assert "☁️" in result   # Clima
        assert "💧" in result   # Humedad
        assert "💨" in result   # Viento
        assert "🎚️" in result   # Presión
        assert "📍" in result   # Coordenadas

    def test_format_weather_includes_separator(self, sample_weather_data):
        """Verifica que el formato incluya líneas decorativas."""
        result = WeatherFormatter.format_weather(sample_weather_data)
        
        assert "━" in result

    def test_format_error_includes_error_emoji(self):
        """Verifica que format_error() incluya el emoji de error."""
        result = WeatherFormatter.format_error("Test error message")
        
        assert "❌" in result
        assert "Error:" in result
        assert "Test error message" in result

    def test_format_welcome_includes_globe_emoji(self):
        """Verifica que format_welcome() incluya el emoji de globo."""
        result = WeatherFormatter.format_welcome()
        
        assert "🌍" in result
        assert "Weather CLI" in result

    def test_format_welcome_includes_separator(self):
        """Verifica que format_welcome() incluya línea decorativa."""
        result = WeatherFormatter.format_welcome()
        
        assert "=" in result

    def test_format_city_prompt_returns_correct_text(self):
        """Verifica que format_city_prompt() retorne el texto correcto."""
        result = WeatherFormatter.format_city_prompt()
        
        assert "ciudad" in result.lower()

    def test_format_loading_includes_city_name(self):
        """Verifica que format_loading() incluya el nombre de la ciudad."""
        result = WeatherFormatter.format_loading("Madrid")
        
        assert "Madrid" in result
        assert "🌍" in result

    def test_format_weather_with_different_city(self):
        """Verifica que format_weather() funcione con diferentes ciudades."""
        data = {
            "city": "Madrid",
            "country": "ES",
            "temperature": 18.3,
            "feels_like": 17.8,
            "description": "Muy nuboso",
            "humidity": 72,
            "pressure": 1015,
            "wind_speed": 4.2,
            "latitude": 40.4165,
            "longitude": -3.7026,
        }
        
        result = WeatherFormatter.format_weather(data)
        
        assert "MADRID" in result
        assert "ES" in result
        assert "18.3°C" in result
        assert "Muy nuboso" in result

    def test_format_weather_wind_conversion_accuracy(self):
        """Verifica que la conversión de viento sea precisa."""
        data = {
            "city": "Test",
            "country": "XX",
            "temperature": 20,
            "feels_like": 20,
            "description": "Test",
            "humidity": 50,
            "pressure": 1000,
            "wind_speed": 5.0,  # 5 m/s = 18 km/h
            "latitude": 0,
            "longitude": 0,
        }
        
        result = WeatherFormatter.format_weather(data)
        
        assert "5.0 m/s" in result
        assert "18.0 km/h" in result

    def test_emojis_dict_has_all_required_emojis(self):
        """Verifica que el diccionario EMOJIS tenga todos los emojis necesarios."""
        assert "globe" in WeatherFormatter.EMOJIS
        assert "thermometer" in WeatherFormatter.EMOJIS
        assert "cloud" in WeatherFormatter.EMOJIS
        assert "droplet" in WeatherFormatter.EMOJIS
        assert "wind" in WeatherFormatter.EMOJIS
        assert "gauge" in WeatherFormatter.EMOJIS
        assert "pin" in WeatherFormatter.EMOJIS
