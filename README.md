# 🌍 Weather CLI

Script CLI en Python para consultar el clima de cualquier ciudad del mundo utilizando la API de OpenWeatherMap.

![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)
![Tests](https://img.shields.io/badge/tests-55%20passed-brightgreen.svg)
![Coverage](https://img.shields.io/badge/coverage-95.65%25-brightgreen.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## ✨ Características

- 🌡️ Consulta de clima en tiempo real para cualquier ciudad
- 🌐 Soporte de ciudades de todo el mundo
- 📊 Información detallada: temperatura, humedad, viento, presión
- 🎨 Interfaz CLI amigable con emojis
- ✅ Cobertura de tests del 95.65%
- 🛡️ Manejo robusto de errores
- 🔒 Configuración segura con variables de entorno

## 📋 Requisitos Previos

- Python 3.11 o superior
- pip (gestor de paquetes de Python)
- Cuenta en [OpenWeatherMap](https://openweathermap.org/api) (gratuita)

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/rcartanacalyx/ia-workshop.git
cd ia-workshop
```

### 2. Crear entorno virtual

```bash
python -m venv venv
```

### 3. Activar el entorno virtual

**En Windows (PowerShell):**
```powershell
.venv\Scripts\activate
```

**En Windows (CMD):**
```cmd
.venv\Scripts\activate.bat
```

**En Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Obtener API key de OpenWeatherMap

1. Crea una cuenta gratuita en https://openweathermap.org/users/sign_up
2. Ve a https://home.openweathermap.org/api_keys
3. Genera una nueva API key (puede tardar unos minutos en activarse)

### 6. Configurar variables de entorno

```bash
# Copiar el archivo de ejemplo
cp .env.example .env

# Editar .env y agregar tu API key
# OPENWEATHER_API_KEY=tu_api_key_aqui
```

**En Windows:**
```powershell
copy .env.example .env
# Luego edita .env con tu editor favorito
```

## 💻 Uso

### Ejecutar el script

**Opción 1 - Usando el script de entrada (recomendado):**
```bash
python run.py
```

**Opción 2 - Como módulo de Python:**
```bash
python -m src.main
```

**Nota:** No ejecutes directamente `python src/main.py` porque usa imports relativos.

### Ejemplo de uso

```
🌍 Weather CLI - Consulta el clima de cualquier ciudad
============================================================

Ingresa el nombre de la ciudad: Buenos Aires

🌍 Consultando el clima de: Buenos Aires

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           CLIMA EN BUENOS AIRES, AR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🌡️  Temperatura: 25.5°C
☁️  Condición: Cielo claro
💧 Humedad: 65%
💨 Viento: 3.5 m/s (12.6 km/h)
🎚️  Presión: 1013 hPa
📍 Coordenadas: -34.61, -58.38

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 🧪 Desarrollo y Testing

### Instalar dependencias de desarrollo

```bash
pip install -r requirements-dev.txt
```

### Ejecutar tests

```bash
# Ejecutar todos los tests
pytest

# Tests con output verbose
pytest -v

# Tests con cobertura
pytest --cov=src

# Tests con reporte HTML de cobertura
pytest --cov=src --cov-report=html
# Abre htmlcov/index.html en tu navegador
```

### Estructura de Tests

```
tests/
├── __init__.py
├── test_config.py              # Tests de configuración
├── test_main.py                # Tests del CLI principal
├── test_weather_formatter.py   # Tests de formateo
├── test_weather_service.py     # Tests del servicio de API
└── fixtures/
    ├── __init__.py
    └── api_responses.py        # Datos mock de la API
```

## 📁 Estructura del Proyecto

```
weather-cli/
├── src/
│   ├── __init__.py
│   ├── main.py                 # Entry point del CLI
│   ├── weather_service.py      # Servicio de consulta a API
│   ├── weather_formatter.py    # Formateo de salida
│   ├── config.py               # Configuración y env vars
│   └── exceptions.py           # Excepciones personalizadas
├── tests/
│   ├── __init__.py
│   ├── test_*.py               # Tests unitarios
│   └── fixtures/
│       └── api_responses.py    # Fixtures de tests
├── .env.example                # Plantilla de variables de entorno
├── .gitignore
├── requirements.txt            # Dependencias de producción
├── requirements-dev.txt        # Dependencias de desarrollo
├── pytest.ini                  # Configuración de pytest
├── .coveragerc                 # Configuración de coverage
└── README.md                   # Este archivo
```

## ⚙️ Configuración

### Variables de Entorno (`.env`)

```env
# API key de OpenWeatherMap (OBLIGATORIO)
OPENWEATHER_API_KEY=your_api_key_here

# Idioma de las respuestas (opcional, por defecto: 'es')
WEATHER_LANG=es

# Timeout para requests HTTP en segundos (opcional, por defecto: 10)
REQUEST_TIMEOUT=10
```

### Idiomas Soportados

Puedes cambiar el idioma de las respuestas modificando `WEATHER_LANG` en `.env`:

- `es` - Español
- `en` - Inglés
- `fr` - Francés
- `de` - Alemán
- `pt` - Portugués
- [Ver lista completa](https://openweathermap.org/current#multi)

## 🔧 Troubleshooting

### Error: "No se encontró la API key de OpenWeatherMap"

**Solución:**
1. Verifica que existe el archivo `.env` en la raíz del proyecto
2. Asegúrate de que `OPENWEATHER_API_KEY` esté configurada
3. La API key no debe ser `your_api_key_here`

### Error: "API key inválida"

**Solución:**
1. Verifica que copiaste correctamente la API key
2. Las nuevas API keys pueden tardar unos minutos en activarse
3. Verifica que tu cuenta de OpenWeatherMap esté activa

### Error: "No se encontró la ciudad: XXX"

**Solución:**
1. Verifica la ortografía del nombre de la ciudad
2. Intenta con el nombre en inglés (ej: "Munich" en lugar de "München")
3. Para ciudades con nombres comunes, prueba agregando el país (ej: "Paris, FR")

### Error: "Timeout al intentar conectar con la API"

**Solución:**
1. Verifica tu conexión a internet
2. Aumenta el valor de `REQUEST_TIMEOUT` en `.env`
3. Intenta nuevamente en unos minutos

### Los tests fallan

**Solución:**
1. Asegúrate de tener instaladas las dependencias de desarrollo:
   ```bash
   pip install -r requirements-dev.txt
   ```
2. Verifica que estás en el directorio raíz del proyecto
3. El entorno virtual debe estar activado

## 📊 Cobertura de Tests

El proyecto cuenta con **95.65% de cobertura de código** con 55 tests que cubren:

| Módulo | Coverage |
|--------|----------|
| `src/config.py` | 100% |
| `src/exceptions.py` | 100% |
| `src/weather_formatter.py` | 100% |
| `src/weather_service.py` | 96.97% |
| `src/main.py` | 88.10% |
| **TOTAL** | **95.65%** |

## 🛠️ Tecnologías Utilizadas

- **Python 3.11+** - Lenguaje de programación
- **requests** - Cliente HTTP para llamadas a la API
- **python-dotenv** - Gestión de variables de entorno
- **pytest** - Framework de testing
- **pytest-cov** - Medición de cobertura de código
- **pytest-mock** - Mocking para tests
- **responses** - Mock de HTTP requests en tests

## 📝 Buenas Prácticas Implementadas

- ✅ **Separación de responsabilidades** (SRP)
- ✅ **Manejo exhaustivo de excepciones**
- ✅ **Type hints** para mejor documentación
- ✅ **Docstrings** en todas las funciones públicas
- ✅ **Tests unitarios** con alta cobertura
- ✅ **Configuración segura** con variables de entorno
- ✅ **Validación de inputs**
- ✅ **Código limpio y legible**

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👤 Autor

**Reynaldo Cartana**
- GitHub: [@rcartanacalyx](https://github.com/rcartanacalyx)

## 🙏 Agradecimientos

- [OpenWeatherMap](https://openweathermap.org/) por su excelente API
- Comunidad de Python por las increíbles herramientas

---

⭐ Si este proyecto te fue útil, considera darle una estrella en GitHub