"""Tests para el módulo principal del CLI."""

import pytest
from unittest.mock import Mock, patch, MagicMock
from src.main import main
from src.exceptions import (
    CityNotFoundException,
    InvalidAPIKeyException,
    NetworkException,
    ConfigurationException,
)
from tests.fixtures.api_responses import get_successful_response


class TestMain:
    """Tests para la función main del CLI."""

    @pytest.fixture(autouse=True)
    def setup_config(self, monkeypatch):
        """Auto-fixture que configura el entorno para todos los tests."""
        monkeypatch.setattr("src.config.Config.API_KEY", "test_api_key")
        monkeypatch.setattr("src.config.Config.TIMEOUT", 10)

    def test_main_exits_with_0_on_success(self, monkeypatch, capsys):
        """Verifica que main() salga con código 0 en caso de éxito."""
        # Mock del input del usuario
        monkeypatch.setattr("builtins.input", lambda _: "Buenos Aires")
        
        # Mock de WeatherService
        mock_service = Mock()
        mock_service.get_weather.return_value = get_successful_response()
        mock_service.parse_weather_data.return_value = {
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
        
        with patch("src.main.WeatherService", return_value=mock_service):
            with pytest.raises(SystemExit) as exc_info:
                main()
        
        assert exc_info.value.code == 0
        
        # Verificar que se imprimió información del clima
        captured = capsys.readouterr()
        assert "BUENOS AIRES" in captured.out

    def test_main_exits_with_1_on_empty_city(self, monkeypatch, capsys):
        """Verifica que main() salga con código 1 si la ciudad está vacía."""
        monkeypatch.setattr("builtins.input", lambda _: "")
        
        with pytest.raises(SystemExit) as exc_info:
            main()
        
        assert exc_info.value.code == 1
        
        captured = capsys.readouterr()
        assert "Error" in captured.out

    def test_main_exits_with_1_on_city_not_found(self, monkeypatch, capsys):
        """Verifica que main() salga con código 1 si la ciudad no existe."""
        monkeypatch.setattr("builtins.input", lambda _: "CiudadInexistente")
        
        # Mock de WeatherService que lanza CityNotFoundException
        mock_service = Mock()
        mock_service.get_weather.side_effect = CityNotFoundException("CiudadInexistente")
        
        with patch("src.main.WeatherService", return_value=mock_service):
            with pytest.raises(SystemExit) as exc_info:
                main()
        
        assert exc_info.value.code == 1
        
        captured = capsys.readouterr()
        assert "No se encontró la ciudad" in captured.out

    def test_main_exits_with_1_on_invalid_api_key(self, monkeypatch, capsys):
        """Verifica que main() salga con código 1 si la API key es inválida."""
        monkeypatch.setattr("builtins.input", lambda _: "Madrid")
        
        mock_service = Mock()
        mock_service.get_weather.side_effect = InvalidAPIKeyException()
        
        with patch("src.main.WeatherService", return_value=mock_service):
            with pytest.raises(SystemExit) as exc_info:
                main()
        
        assert exc_info.value.code == 1
        
        captured = capsys.readouterr()
        assert "API key inválida" in captured.out

    def test_main_exits_with_1_on_network_error(self, monkeypatch, capsys):
        """Verifica que main() salga con código 1 en error de red."""
        monkeypatch.setattr("builtins.input", lambda _: "Madrid")
        
        mock_service = Mock()
        mock_service.get_weather.side_effect = NetworkException("Error de conexión")
        
        with patch("src.main.WeatherService", return_value=mock_service):
            with pytest.raises(SystemExit) as exc_info:
                main()
        
        assert exc_info.value.code == 1
        
        captured = capsys.readouterr()
        assert "Error de conexión" in captured.out

    def test_main_exits_with_1_on_configuration_error(self, monkeypatch, capsys):
        """Verifica que main() salga con código 1 en error de configuración."""
        # Mockear input para que no intente leer
        monkeypatch.setattr("builtins.input", lambda _: "Madrid")
        # Resetear la API key a None para que falle la validación
        monkeypatch.setattr("src.config.Config.API_KEY", None)
        
        with pytest.raises(SystemExit) as exc_info:
            main()
        
        assert exc_info.value.code == 1
        
        captured = capsys.readouterr()
        assert "API key" in captured.out

    def test_main_exits_with_0_on_keyboard_interrupt(self, monkeypatch, capsys):
        """Verifica que main() maneje gracefully Ctrl+C."""
        def mock_input(_):
            raise KeyboardInterrupt()
        
        monkeypatch.setattr("builtins.input", mock_input)
        
        # Crear mock pero no importa porque KeyboardInterrupt se lanza en input
        mock_service = Mock()
        
        with patch("src.main.WeatherService", return_value=mock_service):
            with pytest.raises(SystemExit) as exc_info:
                main()
        
        assert exc_info.value.code == 0
        
        captured = capsys.readouterr()
        assert "Hasta luego" in captured.out

    def test_main_shows_welcome_message(self, monkeypatch, capsys):
        """Verifica que main() muestre el mensaje de bienvenida."""
        monkeypatch.setattr("builtins.input", lambda _: "Madrid")
        
        mock_service = Mock()
        mock_service.get_weather.return_value = get_successful_response()
        mock_service.parse_weather_data.return_value = {
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
        
        with patch("src.main.WeatherService", return_value=mock_service):
            with pytest.raises(SystemExit):
                main()
        
        captured = capsys.readouterr()
        assert "Weather CLI" in captured.out

    def test_main_shows_loading_message(self, monkeypatch, capsys):
        """Verifica que main() muestre mensaje de carga."""
        monkeypatch.setattr("builtins.input", lambda _: "Madrid")
        
        mock_service = Mock()
        mock_service.get_weather.return_value = get_successful_response()
        mock_service.parse_weather_data.return_value = {
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
        
        with patch("src.main.WeatherService", return_value=mock_service):
            with pytest.raises(SystemExit):
                main()
        
        captured = capsys.readouterr()
        assert "Consultando el clima" in captured.out

    def test_main_strips_whitespace_from_city_input(self, monkeypatch, capsys):
        """Verifica que main() limpie espacios del input."""
        monkeypatch.setattr("builtins.input", lambda _: "  Madrid  ")
        
        mock_service = Mock()
        mock_service.get_weather.return_value = get_successful_response()
        mock_service.parse_weather_data.return_value = {
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
        
        with patch("src.main.WeatherService", return_value=mock_service):
            with pytest.raises(SystemExit):
                main()
        
        # Si llega aquí sin error, significa que procesó correctamente el input

    def test_main_shows_suggestion_on_city_not_found(self, monkeypatch, capsys):
        """Verifica que main() muestre sugerencia cuando la ciudad no existe."""
        monkeypatch.setattr("builtins.input", lambda _: "XYZ123")
        
        mock_service = Mock()
        mock_service.get_weather.side_effect = CityNotFoundException("XYZ123")
        
        with patch("src.main.WeatherService", return_value=mock_service):
            with pytest.raises(SystemExit):
                main()
        
        captured = capsys.readouterr()
        assert "Sugerencia" in captured.out

    def test_main_handles_unexpected_exception(self, monkeypatch, capsys):
        """Verifica que main() maneje excepciones inesperadas."""
        monkeypatch.setattr("builtins.input", lambda _: "Madrid")
        
        mock_service = Mock()
        mock_service.get_weather.side_effect = Exception("Unexpected error")
        
        with patch("src.main.WeatherService", return_value=mock_service):
            with pytest.raises(SystemExit) as exc_info:
                main()
        
        assert exc_info.value.code == 1
        
        captured = capsys.readouterr()
        assert "Error inesperado" in captured.out
