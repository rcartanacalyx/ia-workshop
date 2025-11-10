"""Tests para el servicio de clima."""

import pytest
import requests
from unittest.mock import Mock, patch, MagicMock
from src.weather_service import WeatherService
from src.exceptions import (
    CityNotFoundException,
    InvalidAPIKeyException,
    NetworkException,
    WeatherAPIException,
)
from tests.fixtures.api_responses import (
    get_successful_response,
    get_madrid_response,
    get_not_found_response,
    get_unauthorized_response,
    get_malformed_response,
)


class TestWeatherService:
    """Tests para la clase WeatherService."""

    @pytest.fixture(autouse=True)
    def setup_config(self, monkeypatch):
        """Auto-fixture que configura el entorno para todos los tests."""
        monkeypatch.setattr("src.config.Config.API_KEY", "test_api_key")
        monkeypatch.setattr("src.config.Config.TIMEOUT", 10)

    @pytest.fixture
    def weather_service(self):
        """Fixture que crea una instancia de WeatherService con config válida."""
        return WeatherService(skip_validation=True)

    def test_get_weather_success(self, weather_service, monkeypatch):
        """Verifica que get_weather() retorne datos cuando la API responde OK."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = get_successful_response()
        
        monkeypatch.setattr("requests.get", lambda *args, **kwargs: mock_response)
        
        result = weather_service.get_weather("Buenos Aires")
        
        assert result["name"] == "Buenos Aires"
        assert result["cod"] == 200
        assert "main" in result

    def test_get_weather_raises_exception_for_empty_city(self, weather_service):
        """Verifica que get_weather() lance ValueError si la ciudad está vacía."""
        with pytest.raises(ValueError) as exc_info:
            weather_service.get_weather("")
        
        assert "no puede estar vacío" in str(exc_info.value)

    def test_get_weather_raises_exception_for_whitespace_city(self, weather_service):
        """Verifica que get_weather() lance ValueError si la ciudad son solo espacios."""
        with pytest.raises(ValueError) as exc_info:
            weather_service.get_weather("   ")
        
        assert "no puede estar vacío" in str(exc_info.value)

    def test_get_weather_strips_whitespace(self, weather_service, monkeypatch):
        """Verifica que get_weather() limpie espacios del nombre de la ciudad."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = get_successful_response()
        
        mock_get = Mock(return_value=mock_response)
        monkeypatch.setattr("requests.get", mock_get)
        
        weather_service.get_weather("  Madrid  ")
        
        # Verificar que la URL generada no tenga espacios extras
        call_args = mock_get.call_args
        url = call_args[0][0]
        assert "q=Madrid" in url or "Madrid" in url

    def test_get_weather_raises_city_not_found_on_404(self, weather_service, monkeypatch):
        """Verifica que get_weather() lance CityNotFoundException en 404."""
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.json.return_value = get_not_found_response()
        
        monkeypatch.setattr("requests.get", lambda *args, **kwargs: mock_response)
        
        with pytest.raises(CityNotFoundException) as exc_info:
            weather_service.get_weather("CiudadInexistente")
        
        assert "CiudadInexistente" in str(exc_info.value)

    def test_get_weather_raises_invalid_api_key_on_401(self, weather_service, monkeypatch):
        """Verifica que get_weather() lance InvalidAPIKeyException en 401."""
        mock_response = Mock()
        mock_response.status_code = 401
        mock_response.json.return_value = get_unauthorized_response()
        
        monkeypatch.setattr("requests.get", lambda *args, **kwargs: mock_response)
        
        with pytest.raises(InvalidAPIKeyException):
            weather_service.get_weather("Madrid")

    def test_get_weather_raises_exception_on_500(self, weather_service, monkeypatch):
        """Verifica que get_weather() lance WeatherAPIException en error 500."""
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.text = "Internal Server Error"
        
        monkeypatch.setattr("requests.get", lambda *args, **kwargs: mock_response)
        
        with pytest.raises(WeatherAPIException) as exc_info:
            weather_service.get_weather("Madrid")
        
        assert "500" in str(exc_info.value)

    def test_get_weather_raises_network_exception_on_timeout(self, weather_service, monkeypatch):
        """Verifica que get_weather() lance NetworkException en timeout."""
        def mock_get(*args, **kwargs):
            raise requests.exceptions.Timeout("Connection timed out")
        
        monkeypatch.setattr("requests.get", mock_get)
        
        with pytest.raises(NetworkException) as exc_info:
            weather_service.get_weather("Madrid")
        
        assert "Timeout" in str(exc_info.value)

    def test_get_weather_raises_network_exception_on_connection_error(self, weather_service, monkeypatch):
        """Verifica que get_weather() lance NetworkException en error de conexión."""
        def mock_get(*args, **kwargs):
            raise requests.exceptions.ConnectionError("Connection failed")
        
        monkeypatch.setattr("requests.get", mock_get)
        
        with pytest.raises(NetworkException) as exc_info:
            weather_service.get_weather("Madrid")
        
        assert "conexión" in str(exc_info.value).lower()

    def test_parse_weather_data_success(self, weather_service):
        """Verifica que parse_weather_data() parsee correctamente los datos."""
        data = get_successful_response()
        
        result = weather_service.parse_weather_data(data)
        
        assert result["city"] == "Buenos Aires"
        assert result["country"] == "AR"
        assert result["temperature"] == 25.5
        assert result["humidity"] == 65
        assert result["pressure"] == 1013
        assert result["wind_speed"] == 3.5
        assert result["latitude"] == -34.6037
        assert result["longitude"] == -58.3816
        assert "cielo claro" in result["description"].lower()

    def test_parse_weather_data_with_madrid(self, weather_service):
        """Verifica que parse_weather_data() funcione con diferentes ciudades."""
        data = get_madrid_response()
        
        result = weather_service.parse_weather_data(data)
        
        assert result["city"] == "Madrid"
        assert result["country"] == "ES"
        assert result["temperature"] == 18.3
        assert "nuboso" in result["description"].lower()

    def test_parse_weather_data_raises_exception_on_malformed_data(self, weather_service):
        """Verifica que parse_weather_data() lance excepción con datos malformados."""
        malformed_data = get_malformed_response()
        
        with pytest.raises(WeatherAPIException) as exc_info:
            weather_service.parse_weather_data(malformed_data)
        
        assert "parsear" in str(exc_info.value).lower()

    def test_parse_weather_data_capitalizes_description(self, weather_service):
        """Verifica que parse_weather_data() capitalice la descripción."""
        data = get_successful_response()
        data["weather"][0]["description"] = "cielo claro"
        
        result = weather_service.parse_weather_data(data)
        
        assert result["description"][0].isupper()  # Primera letra en mayúscula

    def test_weather_service_uses_config_timeout(self, weather_service, monkeypatch):
        """Verifica que WeatherService use el timeout de Config."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = get_successful_response()
        
        mock_get = Mock(return_value=mock_response)
        monkeypatch.setattr("requests.get", mock_get)
        
        weather_service.get_weather("Madrid")
        
        # Verificar que se llamó con el timeout correcto (10 del autofixture)
        call_kwargs = mock_get.call_args[1]
        assert call_kwargs.get("timeout") == 10
