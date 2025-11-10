# Changelog

Todos los cambios notables del proyecto Weather CLI se documentan en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto adhiere a [Versionado Semántico](https://semver.org/lang/es/).

## [Unreleased]

### Added
- Documentación completa de on-boarding en ONBOARDING.md
- Docstrings detallados en todos los módulos, clases y funciones
- Comentarios explicativos en código complejo
- Este archivo CHANGELOG.md

### Changed
- Mejorados los docstrings con ejemplos de uso y notas adicionales
- Documentación de módulos con información de arquitectura

## [1.0.0] - 2025-11-10

### Added
- CLI interactivo para consulta de clima de cualquier ciudad
- Integración con OpenWeatherMap API v2.5
- Formateo amigable de salida con emojis y decoración
- Manejo robusto de excepciones:
  - `CityNotFoundException` para ciudad no encontrada (404)
  - `InvalidAPIKeyException` para API key inválida (401)
  - `NetworkException` para problemas de red/timeout
  - `ConfigurationException` para problemas de configuración
  - `WeatherAPIException` como clase base para errores de API
- Configuración via variables de entorno (.env)
- Suite completa de tests (55 tests, 95.65% coverage):
  - Tests unitarios de servicio API (14 tests)
  - Tests de formateo de salida (18 tests)
  - Tests de configuración (11 tests)
  - Tests de flujo principal del CLI (12 tests)
- Fixtures de datos de prueba para API responses
- Script de entrada `run.py` para ejecución correcta con imports relativos
- Documentación completa en README.md:
  - Instrucciones de instalación (Windows, Linux, Mac)
  - Guía de uso con ejemplos
  - Configuración de variables de entorno
  - Troubleshooting de problemas comunes
  - Sección de testing con comandos
  - Cobertura de código detallada
- Archivos de configuración:
  - `.env.example` con plantilla de variables
  - `pytest.ini` para configuración de tests
  - `.coveragerc` para configuración de coverage
  - `.gitignore` completo para Python
  - `requirements.txt` para dependencias de producción
  - `requirements-dev.txt` para dependencias de desarrollo

### Features
- Consulta de clima en tiempo real para cualquier ciudad del mundo
- Soporte multiidioma (español, inglés, francés, alemán, etc.)
- Temperaturas en grados Celsius (sistema métrico)
- Información detallada: temperatura, humedad, viento, presión, coordenadas
- Conversión automática de velocidad del viento (m/s a km/h)
- Validación de input de usuario
- Timeout configurable para requests HTTP
- Mensajes de error descriptivos con sugerencias
- Manejo graceful de Ctrl+C (KeyboardInterrupt)

### Technical Details
- **Lenguaje**: Python 3.11+
- **Arquitectura**: Layered Architecture con separación de responsabilidades
- **Módulos**:
  - `main.py`: Entry point y coordinación del flujo
  - `weather_service.py`: Cliente de API de OpenWeatherMap
  - `weather_formatter.py`: Formateo de salida para consola
  - `config.py`: Configuración centralizada y variables de entorno
  - `exceptions.py`: Jerarquía de excepciones personalizadas
- **Dependencias de producción**:
  - `requests==2.31.0`: Cliente HTTP
  - `python-dotenv==1.0.0`: Gestión de variables de entorno
- **Dependencias de desarrollo**:
  - `pytest==7.4.3`: Framework de testing
  - `pytest-mock==3.12.0`: Mocking para tests
  - `pytest-cov==4.1.0`: Medición de cobertura
  - `responses==0.24.1`: Mock de HTTP requests

### Documentation
- README.md completo con:
  - Badges de Python version, tests, coverage
  - Características del proyecto
  - Requisitos previos
  - Instrucciones de instalación detalladas
  - Guía de configuración de API key
  - Ejemplos de uso
  - Documentación de testing
  - Estructura del proyecto
  - Troubleshooting de 7 problemas comunes
  - Estadísticas de cobertura de código
  - Tecnologías utilizadas
  - Buenas prácticas implementadas
  - Información de contribución y licencia

### Quality Assurance
- **Cobertura de código**: 95.65%
  - `config.py`: 100%
  - `exceptions.py`: 100%
  - `weather_formatter.py`: 100%
  - `weather_service.py`: 96.97%
  - `main.py`: 88.10%
- **Principios aplicados**:
  - Separación de responsabilidades (SRP)
  - Type hints en todas las funciones
  - Docstrings con formato Google Style
  - Manejo exhaustivo de excepciones
  - Validación de inputs
  - Código limpio y legible

## Notas de Versión

### v1.0.0 - Release Inicial
Esta es la primera versión estable de Weather CLI. El proyecto incluye todas las
funcionalidades básicas necesarias para consultar el clima de cualquier ciudad,
con manejo robusto de errores, tests completos, y documentación exhaustiva.

**Características destacadas**:
- ✅ CLI funcional con experiencia de usuario amigable
- ✅ 55 tests automatizados con alta cobertura (95.65%)
- ✅ Documentación completa en README.md y ONBOARDING.md
- ✅ Manejo de errores para todos los escenarios posibles
- ✅ Configuración flexible via variables de entorno
- ✅ Código limpio siguiendo mejores prácticas de Python

**Próximas mejoras planeadas** (v1.1.0):
- [ ] Cache de consultas recientes para optimizar requests
- [ ] Soporte para múltiples ciudades en una consulta
- [ ] Pronóstico extendido de 5 días
- [ ] Opción para mostrar sensación térmica (feels_like)
- [ ] Configuración de unidades (Celsius/Fahrenheit)
- [ ] Logging con el módulo `logging` de Python
- [ ] Modo verbose para debugging

**Agradecimientos**:
- [OpenWeatherMap](https://openweathermap.org/) por su excelente API gratuita
- Comunidad de Python por las herramientas de desarrollo

---

**Convenciones de este Changelog**:
- `Added`: Nuevas funcionalidades
- `Changed`: Cambios en funcionalidades existentes
- `Deprecated`: Funcionalidades obsoletas que se eliminarán pronto
- `Removed`: Funcionalidades eliminadas
- `Fixed`: Corrección de bugs
- `Security`: Correcciones de seguridad
