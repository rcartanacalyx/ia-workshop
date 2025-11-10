"""Tests para el módulo de configuración."""

import os
import pytest
from src.config import Config
from src.exceptions import ConfigurationException


class TestConfig:
    """Tests para la clase Config."""

    def test_config_has_base_url(self):
        """Verifica que la URL base esté definida."""
        assert Config.BASE_URL == "https://api.openweathermap.org/data/2.5/weather"

    def test_config_has_default_lang(self):
        """Verifica que el idioma por defecto sea español."""
        assert Config.LANG == "es"

    def test_config_has_default_timeout(self):
        """Verifica que el timeout por defecto sea 10 segundos."""
        assert Config.TIMEOUT == 10

    def test_validate_raises_exception_when_no_api_key(self, monkeypatch):
        """Verifica que validate() lance excepción si no hay API key."""
        monkeypatch.setattr(Config, "API_KEY", None)
        
        with pytest.raises(ConfigurationException) as exc_info:
            Config.validate()
        
        assert "No se encontró la API key" in str(exc_info.value)

    def test_validate_raises_exception_when_api_key_is_placeholder(self, monkeypatch):
        """Verifica que validate() lance excepción si API key es el placeholder."""
        monkeypatch.setattr(Config, "API_KEY", "your_api_key_here")
        
        with pytest.raises(ConfigurationException) as exc_info:
            Config.validate()
        
        assert "No se encontró la API key" in str(exc_info.value)

    def test_validate_raises_exception_when_timeout_is_zero(self, monkeypatch):
        """Verifica que validate() lance excepción si timeout es 0."""
        monkeypatch.setattr(Config, "API_KEY", "valid_key")
        monkeypatch.setattr(Config, "TIMEOUT", 0)
        
        with pytest.raises(ConfigurationException) as exc_info:
            Config.validate()
        
        assert "timeout debe ser mayor a 0" in str(exc_info.value)

    def test_validate_raises_exception_when_timeout_is_negative(self, monkeypatch):
        """Verifica que validate() lance excepción si timeout es negativo."""
        monkeypatch.setattr(Config, "API_KEY", "valid_key")
        monkeypatch.setattr(Config, "TIMEOUT", -5)
        
        with pytest.raises(ConfigurationException) as exc_info:
            Config.validate()
        
        assert "timeout debe ser mayor a 0" in str(exc_info.value)

    def test_validate_passes_with_valid_config(self, monkeypatch):
        """Verifica que validate() no lance excepción con configuración válida."""
        monkeypatch.setattr(Config, "API_KEY", "valid_api_key_123")
        monkeypatch.setattr(Config, "TIMEOUT", 10)
        
        # No debería lanzar excepción
        Config.validate()

    def test_get_api_url_constructs_correct_url(self, monkeypatch):
        """Verifica que get_api_url() construya la URL correctamente."""
        monkeypatch.setattr(Config, "API_KEY", "test_key_123")
        monkeypatch.setattr(Config, "LANG", "es")
        
        url = Config.get_api_url("Buenos Aires")
        
        assert "https://api.openweathermap.org/data/2.5/weather" in url
        assert "q=Buenos Aires" in url
        assert "appid=test_key_123" in url
        assert "lang=es" in url
        assert "units=metric" in url

    def test_get_api_url_with_different_city(self, monkeypatch):
        """Verifica que get_api_url() funcione con diferentes ciudades."""
        monkeypatch.setattr(Config, "API_KEY", "test_key")
        
        url = Config.get_api_url("Madrid")
        
        assert "q=Madrid" in url

    def test_config_loads_from_environment(self, monkeypatch):
        """Verifica que la configuración se cargue desde variables de entorno."""
        monkeypatch.setenv("OPENWEATHER_API_KEY", "env_key_123")
        monkeypatch.setenv("WEATHER_LANG", "en")
        monkeypatch.setenv("REQUEST_TIMEOUT", "20")
        
        # Recargar el módulo para que tome las nuevas variables
        from importlib import reload
        import src.config
        reload(src.config)
        
        assert src.config.Config.API_KEY == "env_key_123"
        assert src.config.Config.LANG == "en"
        assert src.config.Config.TIMEOUT == 20
