# 📚 On-boarding: Weather CLI

> Última actualización: 10 de noviembre de 2025  
> Generado por: GitHub Copilot On-boarding Assistant

---

## 🎯 Descripción General

### ¿Qué hace este proyecto?

**Weather CLI** es una aplicación de línea de comandos (CLI) desarrollada en Python que permite consultar el clima en tiempo real de cualquier ciudad del mundo. El proyecto utiliza la API de OpenWeatherMap para obtener información meteorológica actualizada y la presenta al usuario de manera amigable con emojis y formato descriptivo.

La aplicación fue diseñada siguiendo principios de Clean Code y SOLID, con una arquitectura modular que separa responsabilidades, manejo robusto de errores, y una suite completa de tests automatizados que garantizan su calidad y confiabilidad.

El proyecto es ideal para desarrolladores que quieran aprender sobre integración de APIs REST, testing en Python, manejo de excepciones, configuración con variables de entorno, y buenas prácticas de desarrollo de software.

### Tipo de Proyecto

- **Categoría**: Aplicación CLI (Command Line Interface)
- **Propósito**: Consulta de información meteorológica en tiempo real
- **Usuarios**: Desarrolladores y usuarios finales que necesiten información del clima desde la terminal

### Información Clave

- **Repositorio**: https://github.com/rcartanacalyx/ia-workshop
- **Branch principal**: main
- **Autor**: Reynaldo Cartana (@rcartanacalyx)
- **Licencia**: MIT
- **Versión de Python**: 3.11+

---

## 🛠️ Stack Tecnológico

### Backend

- **Lenguaje**: Python 3.11+
- **Librería HTTP**: requests 2.31.0
- **Configuración**: python-dotenv 1.0.0 para variables de entorno
- **API Externa**: OpenWeatherMap Weather API v2.5

### Herramientas de Desarrollo

- **Testing Framework**: pytest 7.4.3
- **Test Mocking**: pytest-mock 3.12.0
- **Test Coverage**: pytest-cov 4.1.0
- **HTTP Mocking**: responses 0.24.1
- **Entorno Virtual**: venv (estándar de Python)

### Infraestructura

- **Control de Versiones**: Git + GitHub
- **Gestión de Dependencias**: pip + requirements.txt
- **Configuración**: Archivos .env para variables de entorno
- **CI/CD**: No implementado (proyecto educativo)

### API Externa

- **Servicio**: OpenWeatherMap API
- **Endpoint**: `https://api.openweathermap.org/data/2.5/weather`
- **Autenticación**: API Key
- **Plan**: Free tier (60 llamadas/minuto, 1M llamadas/mes)
- **Documentación**: https://openweathermap.org/current

---

## 🏗️ Arquitectura del Proyecto

### Patrón Arquitectónico

El proyecto sigue una **arquitectura en capas (Layered Architecture)** con separación clara de responsabilidades:

1. **Capa de Presentación (UI)**: Manejo de entrada/salida del usuario
2. **Capa de Lógica de Negocio**: Procesamiento de datos del clima
3. **Capa de Acceso a Datos**: Comunicación con la API externa
4. **Capa de Infraestructura**: Configuración y manejo de errores

### Diagrama de Arquitectura (ASCII)

```
┌─────────────────────────────────────────────────────────────┐
│                        USUARIO                              │
│                      (Terminal CLI)                         │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│                    CAPA DE PRESENTACIÓN                     │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  main.py                                              │  │
│  │  - Punto de entrada                                   │  │
│  │  - Manejo de input del usuario                        │  │
│  │  - Coordinación de flujo                              │  │
│  │  - Manejo de excepciones                              │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  weather_formatter.py                                 │  │
│  │  - Formateo de salida                                 │  │
│  │  - Emojis y decoración                                │  │
│  │  - Mensajes de usuario                                │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│              CAPA DE LÓGICA DE NEGOCIO                      │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  weather_service.py                                   │  │
│  │  - Consulta a OpenWeatherMap API                      │  │
│  │  - Parseo de respuestas JSON                          │  │
│  │  - Validación de datos                                │  │
│  │  - Transformación de datos                            │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│                CAPA DE INFRAESTRUCTURA                      │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  config.py                                            │  │
│  │  - Carga de variables de entorno                      │  │
│  │  - Configuración centralizada                         │  │
│  │  - Validación de configuración                        │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  exceptions.py                                        │  │
│  │  - Excepciones personalizadas                         │  │
│  │  - Jerarquía de errores                               │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│                    API EXTERNA                              │
│                 OpenWeatherMap API                          │
└─────────────────────────────────────────────────────────────┘
```

### Capas de la Aplicación

1. **Capa de Presentación** (`main.py`, `weather_formatter.py`)
   - **Responsabilidad**: Interacción con el usuario, formateo de salida
   - **Ubicación**: `src/main.py`, `src/weather_formatter.py`

2. **Capa de Lógica de Negocio** (`weather_service.py`)
   - **Responsabilidad**: Procesamiento y transformación de datos del clima
   - **Ubicación**: `src/weather_service.py`

3. **Capa de Acceso a Datos** (`weather_service.py`)
   - **Responsabilidad**: Comunicación HTTP con la API de OpenWeatherMap
   - **Ubicación**: `src/weather_service.py` (método `get_weather()`)

4. **Capa de Infraestructura** (`config.py`, `exceptions.py`)
   - **Responsabilidad**: Configuración, variables de entorno, manejo de errores
   - **Ubicación**: `src/config.py`, `src/exceptions.py`

### Flujo de una Request Típica

```
[Usuario ingresa "Buenos Aires"]
         ↓
[main.py - valida input no vacío]
         ↓
[WeatherService.get_weather("Buenos Aires")]
         ↓
[Construcción de URL con Config.get_api_url()]
         ↓
[HTTP GET a OpenWeatherMap API con requests]
         ↓
[Validación de status code (200, 404, 401, 500)]
         ↓
[WeatherService.parse_weather_data(response.json())]
         ↓
[Extracción de campos relevantes del JSON]
         ↓
[WeatherFormatter.format_weather(parsed_data)]
         ↓
[Generación de texto con emojis y formato]
         ↓
[Impresión en consola]
         ↓
[sys.exit(0) - Éxito]
```

---

## 📁 Estructura de Directorios

```
ia-workshop/
├── src/                        # Código fuente principal
│   ├── __init__.py            # Inicialización del paquete
│   ├── main.py                # Entry point del CLI
│   ├── weather_service.py     # Cliente de la API de OpenWeatherMap
│   ├── weather_formatter.py   # Formateo de salida para el usuario
│   ├── config.py              # Configuración y variables de entorno
│   └── exceptions.py          # Excepciones personalizadas
│
├── tests/                      # Suite de tests automatizados
│   ├── __init__.py
│   ├── test_main.py           # Tests del CLI principal (12 tests)
│   ├── test_weather_service.py # Tests del servicio API (14 tests)
│   ├── test_weather_formatter.py # Tests del formateo (18 tests)
│   ├── test_config.py         # Tests de configuración (11 tests)
│   └── fixtures/              # Datos de prueba
│       ├── __init__.py
│       └── api_responses.py   # Respuestas mock de la API
│
├── htmlcov/                    # Reportes de cobertura HTML
│   └── index.html             # Reporte principal de coverage
│
├── .venv/                      # Entorno virtual de Python (no versionado)
│
├── run.py                      # Script de entrada para ejecutar el CLI
├── requirements.txt            # Dependencias de producción
├── requirements-dev.txt        # Dependencias de desarrollo
├── pytest.ini                  # Configuración de pytest
├── .coveragerc                 # Configuración de coverage
├── .env.example                # Plantilla de variables de entorno
├── .env                        # Variables de entorno (no versionado)
├── .gitignore                  # Archivos ignorados por git
└── README.md                   # Documentación del proyecto
```

### Descripción de Carpetas Principales

#### `src/`

**Propósito**: Contiene todo el código fuente de la aplicación.

**Archivos importantes**:
- **`main.py`**: Entry point del CLI. Coordina el flujo completo: solicita input al usuario, llama al servicio, formatea la salida, y maneja todas las excepciones.
- **`weather_service.py`**: Cliente de la API de OpenWeatherMap. Realiza las peticiones HTTP, valida respuestas, y parsea los datos JSON.
- **`weather_formatter.py`**: Responsable del formateo visual de la información. Genera mensajes con emojis y estructura la salida.
- **`config.py`**: Configuración centralizada. Carga variables de entorno, valida configuración, y construye URLs de la API.
- **`exceptions.py`**: Jerarquía de excepciones personalizadas para diferentes tipos de errores.

#### `tests/`

**Propósito**: Suite completa de tests unitarios con 95.65% de cobertura.

**Archivos importantes**:
- **`test_main.py`**: 12 tests que verifican el comportamiento del CLI en diferentes escenarios (éxito, errores, validaciones).
- **`test_weather_service.py`**: 14 tests del servicio API (peticiones, parseo, manejo de errores HTTP).
- **`test_weather_formatter.py`**: 18 tests de formateo de salida.
- **`test_config.py`**: 11 tests de configuración y validación.
- **`fixtures/api_responses.py`**: Datos mock de respuestas de la API para tests.

### Archivos de Configuración Clave

- **`.env`**: Variables de entorno (API key, idioma, timeout). **NO se versiona**.
- **`.env.example`**: Plantilla para crear el archivo `.env`.
- **`pytest.ini`**: Configuración de pytest (paths, markers, opciones).
- **`.coveragerc`**: Configuración de coverage (fuentes, omisiones, formato de reporte).
- **`requirements.txt`**: Dependencias de producción (requests, python-dotenv).
- **`requirements-dev.txt`**: Dependencias de desarrollo (pytest, pytest-cov, etc.).
- **`run.py`**: Wrapper que ejecuta `src.main` como módulo usando `runpy`.

---

## ⚙️ Configuración del Entorno

### Pre-requisitos

- **Python 3.11 o superior**: Verifica con `python --version`
- **pip**: Gestor de paquetes de Python (incluido con Python)
- **Cuenta OpenWeatherMap**: Crea una cuenta gratuita en https://openweathermap.org/users/sign_up
- **Git**: Para clonar el repositorio
- **Editor de texto**: VS Code recomendado

### Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto basado en `.env.example`:

```bash
# OpenWeatherMap API Configuration
OPENWEATHER_API_KEY=tu_api_key_aqui

# Idioma de las respuestas (es, en, fr, de, pt, etc.)
WEATHER_LANG=es

# Timeout para requests HTTP en segundos
REQUEST_TIMEOUT=10
```

**Variables disponibles**:

| Variable | Descripción | Obligatorio | Valor por Defecto |
|----------|-------------|-------------|-------------------|
| `OPENWEATHER_API_KEY` | API key de OpenWeatherMap | ✅ Sí | - |
| `WEATHER_LANG` | Idioma de las respuestas | ❌ No | `es` |
| `REQUEST_TIMEOUT` | Timeout de HTTP en segundos | ❌ No | `10` |

**Idiomas soportados**: `es` (Español), `en` (Inglés), `fr` (Francés), `de` (Alemán), `pt` (Portugués), `it` (Italiano), `ja` (Japonés), etc. [Ver lista completa](https://openweathermap.org/current#multi).

### Instalación Local

#### Opción 1: Instalación Manual (Recomendado para desarrollo)

```powershell
# 1. Clonar el repositorio
git clone https://github.com/rcartanacalyx/ia-workshop.git
cd ia-workshop

# 2. Crear entorno virtual
python -m venv .venv

# 3. Activar entorno virtual (PowerShell)
.venv\Scripts\activate

# 4. Instalar dependencias de producción
pip install -r requirements.txt

# 5. Instalar dependencias de desarrollo (opcional, para tests)
pip install -r requirements-dev.txt

# 6. Copiar archivo de configuración
copy .env.example .env

# 7. Editar .env y agregar tu API key
# Abre .env con tu editor y reemplaza "your_api_key_here" con tu API key real

# 8. Ejecutar la aplicación
python run.py
```

**En Linux/Mac**:
```bash
# 3. Activar entorno virtual
source .venv/bin/activate

# 6. Copiar archivo de configuración
cp .env.example .env
```

#### Opción 2: Quick Start (Sin desarrollo)

```powershell
git clone https://github.com/rcartanacalyx/ia-workshop.git
cd ia-workshop
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
# Edita .env con tu API key
python run.py
```

### Obtener API Key de OpenWeatherMap

1. **Crear cuenta**: Ve a https://home.openweathermap.org/users/sign_up
2. **Verificar email**: Confirma tu cuenta desde el email recibido
3. **Generar API key**: Ve a https://home.openweathermap.org/api_keys
4. **Copiar la clave**: Copia la API key generada
5. **Pegar en `.env`**: Edita `.env` y reemplaza `your_api_key_here` con tu clave

**⚠️ Importante**: Las API keys nuevas pueden tardar **10-30 minutos** en activarse. Si recibes "API key inválida", espera unos minutos y vuelve a intentar.

### Configuración de Debugging en VS Code

Si usas VS Code, puedes crear `.vscode/launch.json` para debugging:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Weather CLI",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/run.py",
            "console": "integratedTerminal",
            "justMyCode": true,
            "env": {
                "PYTHONPATH": "${workspaceFolder}"
            }
        }
    ]
}
```

**Uso**: Presiona `F5` en VS Code para ejecutar en modo debug con breakpoints.

---

## 🚀 Funcionalidades Principales

### 1. Consulta de Clima por Ciudad

**Descripción**: Funcionalidad principal que permite consultar el clima de cualquier ciudad del mundo ingresando su nombre.

**Ubicación del código**: `src/main.py` (función `main()`), `src/weather_service.py` (clase `WeatherService`)

**Flujo**:
1. Usuario ingresa nombre de la ciudad
2. Validación de input no vacío
3. Consulta a OpenWeatherMap API
4. Parseo de respuesta JSON
5. Formateo de datos
6. Presentación al usuario

**Ejemplo de uso**:
```
Ingresa el nombre de la ciudad: Madrid

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           CLIMA EN MADRID, ES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🌡️  Temperatura: 18.3°C
☁️  Condición: Muy nuboso
💧 Humedad: 72%
💨 Viento: 4.2 m/s (15.1 km/h)
🎚️  Presión: 1015 hPa
📍 Coordenadas: 40.42, -3.7
```

### 2. Formateo Amigable de Información

**Descripción**: Presenta la información del clima en formato descriptivo con emojis, conversión de unidades, y estructura visual clara.

**Ubicación del código**: `src/weather_formatter.py` (clase `WeatherFormatter`)

**Características**:
- Emojis temáticos (🌡️ termómetro, ☁️ nube, 💧 gota, 💨 viento)
- Conversión de velocidad del viento de m/s a km/h
- Temperatura en grados Celsius
- Líneas decorativas para mejor lectura
- Capitalización de descripciones del clima

### 3. Manejo Robusto de Errores

**Descripción**: Sistema completo de manejo de excepciones que cubre todos los escenarios posibles.

**Ubicación del código**: `src/exceptions.py`, `src/main.py` (bloque try-except), `src/weather_service.py`

**Errores manejados**:
- **CityNotFoundException**: Ciudad no encontrada (404)
- **InvalidAPIKeyException**: API key inválida o no autorizada (401)
- **NetworkException**: Problemas de conexión o timeout
- **WeatherAPIException**: Errores generales de la API (500, etc.)
- **ConfigurationException**: Falta de API key o configuración incorrecta
- **KeyboardInterrupt**: Cierre graceful con Ctrl+C
- **Exception genérica**: Captura de errores inesperados

**Ejemplo de error**:
```
❌ Error: No se encontró la ciudad: XYZ123
💡 Sugerencia: Verifica que el nombre de la ciudad esté bien escrito.
```

### 4. Validación de Configuración

**Descripción**: Validación automática de variables de entorno al iniciar la aplicación.

**Ubicación del código**: `src/config.py` (método `Config.validate()`)

**Validaciones**:
- API key presente y no vacía
- API key diferente del placeholder "your_api_key_here"
- Timeout mayor a 0 segundos

**Código de ejemplo**:
```python
from src.config import Config

# Validación automática en WeatherService.__init__()
Config.validate()  # Lanza ConfigurationException si hay problemas
```

---

## 🔄 Flujos de Negocio Clave

### Flujo 1: Consulta Exitosa de Clima

**Descripción**: Flujo completo desde que el usuario ingresa una ciudad hasta que ve la información formateada.

**Pasos**:

1. **Inicialización** → Archivo: `src/main.py` líneas 13-52
   - Se imprime mensaje de bienvenida
   - Se crea instancia de `WeatherService()`
   - Se valida la configuración (API key)

2. **Input del Usuario** → Archivo: `src/main.py` líneas 27-32
   - Se solicita nombre de la ciudad
   - Se limpia espacios en blanco con `.strip()`
   - Se valida que no esté vacío

3. **Consulta a la API** → Archivo: `src/weather_service.py` líneas 24-74
   - Se construye URL con `Config.get_api_url(city)`
   - Se realiza `requests.get()` con timeout
   - Se valida el status code HTTP

4. **Parseo de Datos** → Archivo: `src/weather_service.py` líneas 76-103
   - Se extraen campos relevantes del JSON
   - Se estructura en diccionario Python
   - Se capitalizan descripciones

5. **Formateo y Presentación** → Archivo: `src/weather_formatter.py` líneas 11-58
   - Se genera texto con emojis
   - Se convierte velocidad del viento a km/h
   - Se agregan líneas decorativas
   - Se imprime en consola

6. **Finalización** → Archivo: `src/main.py` línea 43
   - Se ejecuta `sys.exit(0)` para indicar éxito

**Diagrama**:
```
[Usuario] → [Input: "Buenos Aires"]
              ↓
[Validación: no vacío] ✓
              ↓
[WeatherService.get_weather("Buenos Aires")]
              ↓
[HTTP GET] → [OpenWeatherMap API]
              ↓
[Status 200] ✓ → [Response JSON]
              ↓
[WeatherService.parse_weather_data(json)]
              ↓
[Dict: {city, temp, humidity, ...}]
              ↓
[WeatherFormatter.format_weather(dict)]
              ↓
[String formateado con emojis]
              ↓
[print()] → [Consola]
              ↓
[sys.exit(0)]
```

**Código de ejemplo completo**:
```python
# Flujo simplificado
try:
    # 1. Input
    city = input("Ingresa la ciudad: ").strip()
    
    # 2. Consulta
    weather_service = WeatherService()
    weather_data = weather_service.get_weather(city)
    
    # 3. Parseo
    parsed_data = weather_service.parse_weather_data(weather_data)
    
    # 4. Formateo
    formatted_output = WeatherFormatter.format_weather(parsed_data)
    
    # 5. Presentación
    print(formatted_output)
    sys.exit(0)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
```

### Flujo 2: Manejo de Ciudad No Encontrada

**Descripción**: Manejo del error 404 cuando el usuario ingresa una ciudad inexistente o mal escrita.

**Pasos**:

1. **Input Incorrecto** → Archivo: `src/main.py` línea 27
   - Usuario ingresa "XYZ123" (ciudad inexistente)

2. **Consulta a la API** → Archivo: `src/weather_service.py` líneas 45-49
   - Se envía request a OpenWeatherMap
   - API responde con status 404

3. **Detección del Error** → Archivo: `src/weather_service.py` líneas 56-57
   - Se detecta `response.status_code == 404`
   - Se lanza `CityNotFoundException(city)`

4. **Captura en Main** → Archivo: `src/main.py` líneas 47-50
   - Se captura la excepción
   - Se formatea el error
   - Se muestra sugerencia al usuario

5. **Finalización con Error** → Archivo: `src/main.py` línea 50
   - Se ejecuta `sys.exit(1)` para indicar error

**Diagrama**:
```
[Usuario] → [Input: "XYZ123"]
              ↓
[WeatherService.get_weather("XYZ123")]
              ↓
[HTTP GET] → [OpenWeatherMap API]
              ↓
[Status 404] ✗ → {"cod": "404", "message": "city not found"}
              ↓
[raise CityNotFoundException("XYZ123")]
              ↓
[Captura en main()]
              ↓
[WeatherFormatter.format_error("No se encontró la ciudad: XYZ123")]
              ↓
[print()] → ["❌ Error: No se encontró la ciudad: XYZ123"]
[print()] → ["💡 Sugerencia: Verifica que el nombre esté bien escrito."]
              ↓
[sys.exit(1)]
```

**Código relevante**:
```python
# weather_service.py
if response.status_code == 404:
    raise CityNotFoundException(city)

# main.py
except CityNotFoundException as e:
    print(WeatherFormatter.format_error(str(e)))
    print("💡 Sugerencia: Verifica que el nombre de la ciudad esté bien escrito.\n")
    sys.exit(1)
```

### Flujo 3: Validación de Configuración al Inicio

**Descripción**: Validación automática de la API key antes de realizar cualquier consulta.

**Pasos**:

1. **Inicialización de WeatherService** → Archivo: `src/weather_service.py` líneas 16-23
   - Se crea instancia de `WeatherService()`
   - Se llama a `Config.validate()` si `skip_validation=False`

2. **Validación de API Key** → Archivo: `src/config.py` líneas 28-40
   - Se verifica que `Config.API_KEY` no sea `None`
   - Se verifica que no sea el placeholder "your_api_key_here"
   - Se verifica que `Config.TIMEOUT > 0`

3. **Lanzamiento de Excepción** → Archivo: `src/config.py` líneas 32-37
   - Si falta la API key, se lanza `ConfigurationException`
   - Mensaje incluye instrucciones detalladas

4. **Captura en Main** → Archivo: `src/main.py` líneas 45-46
   - Se captura `ConfigurationException`
   - Se formatea y muestra el error

**Diagrama**:
```
[WeatherService()] → [__init__()]
              ↓
[Config.validate()]
              ↓
[¿API_KEY existe?] ✗
              ↓
[raise ConfigurationException("No se encontró la API key...")]
              ↓
[Captura en main()]
              ↓
[print(error)]
              ↓
[sys.exit(1)]
```

---

## 🗄️ Base de Datos

**No aplica**: Este proyecto no utiliza base de datos. Toda la información se obtiene en tiempo real de la API de OpenWeatherMap y no se persiste localmente.

---

## 🔌 Integraciones Externas

### 1. OpenWeatherMap API

**Propósito**: Obtener información meteorológica en tiempo real de ciudades de todo el mundo.

**Documentación**: https://openweathermap.org/current

**Autenticación**: API Key (AppID) enviada como parámetro en la URL.

**Configuración**: 
- Variable de entorno: `OPENWEATHER_API_KEY`
- Se obtiene en: https://home.openweathermap.org/api_keys

**Ubicación en código**: `src/weather_service.py` (clase `WeatherService`)

**Endpoint usado**:
```
GET https://api.openweathermap.org/data/2.5/weather
```

**Parámetros**:
- `q`: Nombre de la ciudad (ejemplo: "London", "Madrid", "Buenos Aires")
- `appid`: API key de autenticación
- `lang`: Idioma de la respuesta (ejemplo: "es", "en")
- `units`: Sistema de unidades ("metric" para Celsius, "imperial" para Fahrenheit)

**Ejemplo de request completa**:
```
https://api.openweathermap.org/data/2.5/weather?q=Buenos Aires&appid=tu_api_key&lang=es&units=metric
```

**Response exitosa (200)**:
```json
{
  "coord": {"lon": -58.3816, "lat": -34.6037},
  "weather": [
    {
      "id": 800,
      "main": "Clear",
      "description": "cielo claro",
      "icon": "01d"
    }
  ],
  "main": {
    "temp": 25.5,
    "feels_like": 25.2,
    "humidity": 65,
    "pressure": 1013
  },
  "wind": {"speed": 3.5, "deg": 180},
  "sys": {"country": "AR"},
  "name": "Buenos Aires"
}
```

**Códigos de estado HTTP manejados**:

| Código | Descripción | Manejo en el Código |
|--------|-------------|---------------------|
| 200 | Éxito | Retorna los datos JSON |
| 404 | Ciudad no encontrada | Lanza `CityNotFoundException` |
| 401 | API key inválida | Lanza `InvalidAPIKeyException` |
| 500 | Error del servidor | Lanza `WeatherAPIException` |
| Timeout | Sin respuesta en X segundos | Lanza `NetworkException` |
| Connection Error | Problema de red | Lanza `NetworkException` |

**Limitaciones conocidas**:

- **Rate Limiting**: Plan gratuito limita a 60 llamadas/minuto y 1 millón/mes
  - **Cómo se maneja**: El proyecto no implementa rate limiting activo. Si se excede, la API responde con error 429 (no manejado específicamente).

- **Activación de API Keys**: Las nuevas API keys tardan 10-30 minutos en activarse
  - **Cómo se maneja**: Se muestra mensaje de error al usuario sugiriendo esperar.

- **Nombres de ciudades**: Algunas ciudades requieren nombre en inglés o código de país
  - **Cómo se maneja**: Se sugiere al usuario verificar ortografía. Ejemplos: "Munich" en lugar de "München", o "Paris,FR" para especificar Francia.

- **Timeout**: Configurado a 10 segundos por defecto
  - **Cómo se maneja**: Configurable vía `REQUEST_TIMEOUT` en `.env`. Si se excede, se lanza `NetworkException`.

**Código de integración**:
```python
# src/weather_service.py
def get_weather(self, city: str) -> Dict[str, Any]:
    url = Config.get_api_url(city)
    
    try:
        response = requests.get(url, timeout=Config.TIMEOUT)
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            raise CityNotFoundException(city)
        elif response.status_code == 401:
            raise InvalidAPIKeyException()
        else:
            raise WeatherAPIException(f"Error: {response.status_code}")
            
    except requests.exceptions.Timeout:
        raise NetworkException(f"Timeout (>{Config.TIMEOUT}s)")
    except requests.exceptions.ConnectionError:
        raise NetworkException("No se pudo conectar con la API")
```

---

## 🧪 Testing

### Estructura de Tests

```
tests/
├── __init__.py
├── test_config.py              # 11 tests - Configuración y validación
├── test_main.py                # 12 tests - Flujo del CLI principal
├── test_weather_formatter.py   # 18 tests - Formateo de salida
├── test_weather_service.py     # 14 tests - Cliente de API
└── fixtures/
    ├── __init__.py
    └── api_responses.py        # Datos mock de respuestas API
```

**Total**: 55 tests unitarios con 95.65% de cobertura de código.

### Ejecutar Tests

```powershell
# Todos los tests (modo simple)
pytest

# Tests con output verbose
pytest -v

# Tests con cobertura
pytest --cov=src

# Tests con reporte HTML de cobertura
pytest --cov=src --cov-report=html
# Abre htmlcov/index.html en tu navegador

# Ejecutar solo un archivo de tests
pytest tests/test_weather_service.py

# Ejecutar un test específico
pytest tests/test_weather_service.py::TestWeatherService::test_get_weather_success

# Tests con output detallado de cada assert
pytest -vv

# Tests en modo quiet (solo resumen)
pytest -q
```

### Cobertura Actual

**Cobertura Total**: **95.65%** (objetivo: >80%)

| Módulo | Cobertura | Statements | Missing |
|--------|-----------|------------|---------|
| `src/config.py` | **100%** | 28 | 0 |
| `src/exceptions.py` | **100%** | 18 | 0 |
| `src/weather_formatter.py` | **100%** | 34 | 0 |
| `src/weather_service.py` | **96.97%** | 66 | 2 |
| `src/main.py` | **88.10%** | 42 | 5 |
| **TOTAL** | **95.65%** | **188** | **7** |

**Líneas no cubiertas**:
- `src/main.py`: Algunas ramas de error poco probables
- `src/weather_service.py`: Casos edge de errores de parseo

### Escribir Tests

**Framework**: pytest con fixtures y mocking

**Ejemplo de test unitario**:
```python
# tests/test_weather_service.py
import pytest
from src.weather_service import WeatherService
from src.exceptions import CityNotFoundException

class TestWeatherService:
    @pytest.fixture
    def weather_service(self):
        """Fixture que crea instancia de WeatherService."""
        return WeatherService(skip_validation=True)
    
    def test_get_weather_raises_city_not_found_on_404(self, weather_service, monkeypatch):
        """Verifica que se lance excepción cuando la ciudad no existe."""
        # Mock de requests.get para retornar 404
        mock_response = Mock()
        mock_response.status_code = 404
        monkeypatch.setattr("requests.get", lambda *args, **kwargs: mock_response)
        
        # Verificar que se lanza la excepción correcta
        with pytest.raises(CityNotFoundException) as exc_info:
            weather_service.get_weather("CiudadInexistente")
        
        assert "CiudadInexistente" in str(exc_info.value)
```

**Ejemplo con responses (HTTP mocking)**:
```python
import responses
from tests.fixtures.api_responses import get_successful_response

@responses.activate
def test_api_call():
    responses.add(
        responses.GET,
        "https://api.openweathermap.org/data/2.5/weather",
        json=get_successful_response(),
        status=200
    )
    
    service = WeatherService(skip_validation=True)
    result = service.get_weather("Buenos Aires")
    assert result["name"] == "Buenos Aires"
```

### Convenciones de Testing

- **Naming**: Los tests se nombran `test_<función>_<escenario>_<resultado_esperado>`
  - Ejemplo: `test_get_weather_raises_exception_for_empty_city`

- **Estructura**: Cada archivo de tests tiene una clase `Test<Módulo>`
  - Ejemplo: `TestWeatherService`, `TestWeatherFormatter`

- **Fixtures**: Se usan fixtures con `autouse=True` para configuración común
  - `setup_config`: Configura variables de entorno para todos los tests

- **Mocking**: Se usa `monkeypatch` de pytest y `responses` para HTTP mocking
  - `monkeypatch.setattr()` para mockear funciones y atributos
  - `@responses.activate` para mockear requests HTTP

- **Assertions**: Se usan `pytest.raises()` para verificar excepciones
  ```python
  with pytest.raises(CityNotFoundException) as exc_info:
      weather_service.get_weather("Invalid")
  assert "Invalid" in str(exc_info.value)
  ```

- **Aislamiento**: Cada test es independiente y no depende del orden de ejecución

- **Coverage**: Se excluyen de coverage `__init__.py` y la carpeta `tests/`

---

## 📐 Convenciones y Buenas Prácticas

### Naming Conventions

- **Variables**: `snake_case`
  - Ejemplos: `weather_data`, `api_key`, `wind_speed`

- **Funciones**: `snake_case`
  - Ejemplos: `get_weather()`, `parse_weather_data()`, `format_weather()`

- **Clases**: `PascalCase`
  - Ejemplos: `WeatherService`, `WeatherFormatter`, `Config`

- **Constantes**: `UPPER_SNAKE_CASE`
  - Ejemplos: `API_KEY`, `BASE_URL`, `TIMEOUT`, `EMOJIS`

- **Archivos**: `snake_case`
  - Ejemplos: `weather_service.py`, `weather_formatter.py`, `test_main.py`

- **Excepciones**: `PascalCase` terminando en `Exception`
  - Ejemplos: `CityNotFoundException`, `InvalidAPIKeyException`

### Estructura de Código

**Orden de imports**:
```python
# 1. Standard library
import sys
from typing import Dict, Any, NoReturn

# 2. Third-party libraries
import requests
from dotenv import load_dotenv

# 3. Local imports (relativos)
from .config import Config
from .exceptions import CityNotFoundException
```

**Orden de elementos en un archivo**:
1. Docstring del módulo
2. Imports
3. Constantes del módulo
4. Clases (si existen)
5. Funciones
6. Bloque `if __name__ == "__main__"` (si aplica)

**Ejemplo**:
```python
"""Módulo para consultar el clima usando OpenWeatherMap API."""

import requests
from typing import Dict, Any

from .config import Config
from .exceptions import WeatherAPIException

# Constantes
DEFAULT_TIMEOUT = 10

class WeatherService:
    """Servicio para interactuar con la API."""
    
    def __init__(self):
        """Inicializa el servicio."""
        pass
    
    def get_weather(self, city: str) -> Dict[str, Any]:
        """Obtiene el clima de una ciudad."""
        pass

def helper_function():
    """Función auxiliar."""
    pass
```

### Comentarios y Documentación

- **Docstrings obligatorios** para:
  - Todos los módulos (primera línea del archivo)
  - Todas las clases
  - Todos los métodos y funciones públicos

- **Formato de docstrings**: Estilo Google (descripción + Args + Returns + Raises)

**Ejemplo de docstring completo**:
```python
def get_weather(self, city: str) -> Dict[str, Any]:
    """
    Obtiene la información del clima para una ciudad específica.

    Args:
        city: Nombre de la ciudad a consultar.

    Returns:
        Diccionario con los datos del clima.

    Raises:
        CityNotFoundException: Si la ciudad no se encuentra.
        InvalidAPIKeyException: Si la API key es inválida.
        NetworkException: Si hay problemas de red o timeout.
        WeatherAPIException: Para otros errores de la API.
    """
    pass
```

- **Comentarios inline**: Solo para código complejo o no obvio
  ```python
  # Convertir velocidad del viento de m/s a km/h
  wind_kmh = wind_speed * 3.6
  ```

- **Type hints**: Obligatorios en todas las funciones
  ```python
  def parse_weather_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
  ```

### Manejo de Errores

**Patrón estándar**:
```python
try:
    # Código que puede fallar
    result = risky_operation()
except SpecificException as e:
    # Manejo específico
    handle_specific_error(e)
except AnotherException as e:
    # Otro manejo específico
    handle_another_error(e)
except Exception as e:
    # Catch-all para errores inesperados
    log_unexpected_error(e)
    raise  # Re-lanzar si es necesario
```

**Jerarquía de excepciones**:
```python
# exceptions.py
class WeatherAPIException(Exception):
    """Excepción base para errores de la API."""
    pass

class CityNotFoundException(WeatherAPIException):
    """Excepción específica para ciudad no encontrada."""
    def __init__(self, city_name: str):
        self.city_name = city_name
        super().__init__(f"No se encontró la ciudad: {city_name}")
```

**Principios**:
- Capturar excepciones específicas antes que genéricas
- No usar `except:` sin tipo (usar `except Exception:` como mínimo)
- Proporcionar mensajes de error descriptivos
- Incluir sugerencias al usuario cuando sea posible

### Imports Relativos

**En el paquete `src/`**: Se usan imports relativos
```python
# src/main.py
from .weather_service import WeatherService
from .weather_formatter import WeatherFormatter
from .exceptions import CityNotFoundException
```

**Ventajas**:
- Mejor encapsulación del paquete
- Facilita el testing con mocks
- Evita problemas de PATH

**Ejecución**: Se ejecuta como módulo usando `run.py` o `python -m src.main`

### Git Workflow

**Branching strategy**: No definida formalmente (proyecto educativo)

**Nombre de branches** (sugerido):
- `main` - Branch principal con código estable
- `feature/nombre` - Para nuevas funcionalidades
- `bugfix/nombre` - Para corrección de bugs
- `hotfix/nombre` - Para fixes urgentes

**Commits**:
- Mensajes en español
- Formato descriptivo
- Ejemplos:
  - "Agrega validación de API key en config"
  - "Corrige formato de temperatura en weather_formatter"
  - "Implementa tests de manejo de errores 404"

**Pull Requests** (sugerido):
- Descripción clara del cambio
- Tests pasando (55/55)
- Coverage mantenido o mejorado (>95%)

---

## 🔧 Troubleshooting Común

### Problema 1: "No se encontró la API key de OpenWeatherMap"

**Síntomas**:
```
❌ Error: No se encontró la API key de OpenWeatherMap.
Por favor:
1. Copia el archivo .env.example a .env
2. Obtén tu API key en https://openweathermap.org/api
3. Configura OPENWEATHER_API_KEY en el archivo .env
```

**Causa**: El archivo `.env` no existe o la variable `OPENWEATHER_API_KEY` no está configurada.

**Solución**:
```powershell
# 1. Copiar archivo de ejemplo
copy .env.example .env

# 2. Editar .env con tu editor
notepad .env
# o
code .env

# 3. Reemplazar "your_api_key_here" con tu API key real
# OPENWEATHER_API_KEY=1b30615abfd247baa223f4b97c76b0c8

# 4. Verificar que el archivo existe y tiene contenido
type .env
```

### Problema 2: "API key inválida"

**Síntomas**:
```
❌ Error: API key inválida. Verifica tu configuración en el archivo .env
```

**Causa**: La API key es incorrecta o aún no está activada (las nuevas tardan 10-30 minutos).

**Solución**:

1. **Verificar la API key en OpenWeatherMap**:
   - Ve a https://home.openweathermap.org/api_keys
   - Verifica que la key esté marcada como "Active"

2. **Verificar que copiaste bien la key**:
   ```powershell
   # Ver contenido de .env
   type .env
   # Verificar que OPENWEATHER_API_KEY no tenga espacios extra
   ```

3. **Si es nueva, esperar 10-30 minutos**:
   - Las API keys nuevas tardan en activarse
   - Mientras tanto, puedes ejecutar los tests

4. **Probar la key manualmente**:
   - Abre en el navegador:
     ```
     https://api.openweathermap.org/data/2.5/weather?q=London&appid=TU_API_KEY&units=metric
     ```
   - Si ves JSON con datos del clima, la key funciona
   - Si ves `{"cod":401,"message":"Invalid API key..."}`, aún no está activa

### Problema 3: "No se encontró la ciudad: XYZ"

**Síntomas**:
```
❌ Error: No se encontró la ciudad: XYZ
💡 Sugerencia: Verifica que el nombre de la ciudad esté bien escrito.
```

**Causa**: El nombre de la ciudad es incorrecto o está mal escrito.

**Solución**:

1. **Verificar ortografía**: "Madrif" → "Madrid"

2. **Usar nombre en inglés**: "München" → "Munich"

3. **Especificar país** (para ciudades con nombres comunes):
   - "Paris, FR" (París, Francia)
   - "Paris, US" (París, Texas)
   - "Santiago, CL" (Santiago de Chile)
   - "Santiago, ES" (Santiago de Compostela)

4. **Buscar en OpenWeatherMap**:
   - Ve a https://openweathermap.org/
   - Busca la ciudad y verifica cómo está registrada

### Problema 4: "Timeout al intentar conectar con la API"

**Síntomas**:
```
❌ Error: Timeout al intentar conectar con la API (>10s)
```

**Causa**: La conexión a internet es lenta o la API no responde.

**Solución**:

1. **Verificar conexión a internet**:
   ```powershell
   ping google.com
   ```

2. **Aumentar timeout en `.env`**:
   ```env
   REQUEST_TIMEOUT=30
   ```

3. **Verificar firewall/proxy**: Asegúrate de que Python puede hacer requests HTTP.

4. **Reintentar en unos minutos**: Puede ser un problema temporal de OpenWeatherMap.

### Problema 5: ImportError al ejecutar directamente

**Síntomas**:
```powershell
PS> python src/main.py
ImportError: attempted relative import with no known parent package
```

**Causa**: `src/main.py` usa imports relativos (`.weather_service`) que requieren ejecución como módulo.

**Solución**:

**✅ Correcto**:
```powershell
# Opción 1: Usar run.py
python run.py

# Opción 2: Ejecutar como módulo
python -m src.main
```

**❌ Incorrecto**:
```powershell
# No ejecutar directamente
python src/main.py  # ERROR
```

### Problema 6: Los tests fallan

**Síntomas**:
```
FAILED tests/test_main.py::TestMain::test_main_exits_with_0_on_success
```

**Causa**: Dependencias de desarrollo no instaladas o problemas de entorno.

**Solución**:

1. **Instalar dependencias de desarrollo**:
   ```powershell
   pip install -r requirements-dev.txt
   ```

2. **Verificar que el entorno virtual está activado**:
   ```powershell
   # Debería aparecer (.venv) al inicio del prompt
   (.venv) PS C:\Projects\ia-workshop>
   ```

3. **Reinstalar todo desde cero**:
   ```powershell
   # Desactivar entorno
   deactivate
   
   # Eliminar entorno viejo
   Remove-Item -Recurse -Force .venv
   
   # Crear nuevo
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   
   # Ejecutar tests
   pytest
   ```

4. **Ver detalles del error**:
   ```powershell
   pytest -vv  # Output muy verbose
   ```

### Problema 7: "ModuleNotFoundError: No module named 'src'"

**Síntomas**:
```
ModuleNotFoundError: No module named 'src'
```

**Causa**: Estás ejecutando desde el directorio incorrecto.

**Solución**:

```powershell
# Verificar que estás en la raíz del proyecto
pwd
# Debería mostrar: C:\Projects\ia-workshop

# Si estás en otro directorio, navega a la raíz
cd C:\Projects\ia-workshop

# Verificar que existe la carpeta src/
ls
# Debería mostrar: src/, tests/, run.py, etc.

# Ejecutar desde la raíz
python run.py
```

---

## 📚 Recursos Adicionales

### Documentación Externa

- **OpenWeatherMap API**:
  - Documentación oficial: https://openweathermap.org/current
  - FAQ: https://openweathermap.org/faq
  - Códigos de error: https://openweathermap.org/faq#error401

- **Python**:
  - Documentación oficial: https://docs.python.org/3/
  - Type hints: https://docs.python.org/3/library/typing.html
  - Virtual environments: https://docs.python.org/3/library/venv.html

- **Pytest**:
  - Documentación: https://docs.pytest.org/
  - Fixtures: https://docs.pytest.org/en/stable/fixture.html
  - Parametrize: https://docs.pytest.org/en/stable/parametrize.html

- **Requests**:
  - Documentación: https://requests.readthedocs.io/
  - Quickstart: https://requests.readthedocs.io/en/latest/user/quickstart/

- **Python-dotenv**:
  - GitHub: https://github.com/theskumar/python-dotenv
  - Documentación: https://pypi.org/project/python-dotenv/

### Herramientas Útiles

- **VS Code**: Editor recomendado
  - Extensión Python: https://marketplace.visualstudio.com/items?itemName=ms-python.python
  - Extensión Pylance: Incluida con la extensión Python

- **Postman**: Para probar la API manualmente
  - https://www.postman.com/

- **HTTPie**: Cliente HTTP para terminal (alternativa a curl)
  - https://httpie.io/
  - Ejemplo: `http GET "https://api.openweathermap.org/data/2.5/weather?q=London&appid=KEY"`

- **Coverage.py**: Para ver cobertura detallada
  - Documentación: https://coverage.readthedocs.io/

### Comandos Útiles

```powershell
# Ver versión de Python
python --version

# Ver paquetes instalados
pip list

# Ver información de un paquete
pip show requests

# Actualizar pip
python -m pip install --upgrade pip

# Verificar API key con curl (PowerShell)
curl "https://api.openweathermap.org/data/2.5/weather?q=London&appid=TU_API_KEY"

# Ver logs de git
git log --oneline

# Ver cambios no commiteados
git status
git diff
```

---

## 👥 Contactos y Soporte

### Equipo de Desarrollo

- **Autor Principal**: Reynaldo Cartana
  - GitHub: [@rcartanacalyx](https://github.com/rcartanacalyx)
  - Repositorio: https://github.com/rcartanacalyx/ia-workshop

### Para Nuevos Desarrolladores

**Primeros pasos recomendados**:

1. ✅ **Leer este documento completo** (30-45 minutos)
2. ✅ **Clonar el repositorio y configurar entorno** (10-15 minutos)
   ```powershell
   git clone https://github.com/rcartanacalyx/ia-workshop.git
   cd ia-workshop
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```
3. ✅ **Crear `.env` y obtener API key** (5-10 minutos + tiempo de espera)
   ```powershell
   copy .env.example .env
   # Editar .env con tu API key
   ```
4. ✅ **Ejecutar el proyecto localmente** (2 minutos)
   ```powershell
   python run.py
   # Probar con: Buenos Aires, Madrid, London, etc.
   ```
5. ✅ **Ejecutar los tests** (5 minutos)
   ```powershell
   pytest -v
   pytest --cov=src --cov-report=html
   # Abrir htmlcov/index.html
   ```
6. ✅ **Explorar el código base** (30-60 minutos)
   - Empezar por `src/main.py`
   - Seguir con `src/weather_service.py`
   - Revisar `src/weather_formatter.py`
   - Leer `src/config.py` y `src/exceptions.py`
   - Explorar tests en `tests/`
7. ✅ **Hacer una pequeña modificación** (15-30 minutos)
   - Sugerencias:
     - Agregar un nuevo emoji en `WeatherFormatter`
     - Agregar validación de temperatura negativa
     - Mejorar un mensaje de error
   - Ejecutar tests: `pytest`
   - Verificar coverage: `pytest --cov=src`
8. ✅ **Crear un commit y push** (5 minutos)
   ```powershell
   git checkout -b feature/mi-primer-cambio
   git add .
   git commit -m "Agrega nuevo emoji para nieve"
   git push origin feature/mi-primer-cambio
   ```

**Preguntas frecuentes**:

- **¿Cómo obtengo la API key?** → Ver sección "Obtener API Key de OpenWeatherMap"
- **¿Por qué los tests fallan?** → Ver "Troubleshooting - Problema 6"
- **¿Cómo ejecuto el proyecto?** → `python run.py` (no `python src/main.py`)
- **¿Cuál es la cobertura mínima?** → 80% (actualmente en 95.65%)
- **¿Puedo usar otra API?** → Sí, pero requiere modificar `weather_service.py`

---

## 🎯 Siguientes Pasos

Ahora que has leído esta guía:

1. **Setup inicial**: Sigue las instrucciones de instalación en la sección "Configuración del Entorno"

2. **Explora el código**: Comienza por los puntos de entrada:
   - `run.py` - Script de entrada
   - `src/main.py` - Función principal del CLI
   - `src/weather_service.py` - Integración con la API
   - `src/weather_formatter.py` - Formateo de salida

3. **Ejecuta los tests**: Familiarízate con la suite de tests
   ```powershell
   pytest -v
   pytest --cov=src --cov-report=html
   ```

4. **Tarea inicial recomendada**: Agrega soporte para mostrar la sensación térmica (feels_like)
   - El dato ya se parsea en `weather_service.py` (campo `feels_like`)
   - Agrégalo al output en `weather_formatter.py`
   - Escribe tests en `test_weather_formatter.py`
   - Verifica que la cobertura se mantenga >95%

5. **Experimenta**: Prueba diferentes ciudades, idiomas, y casos de error

**Ideas para contribuir**:
- Agregar caché de consultas recientes
- Soportar múltiples ciudades en una consulta
- Agregar pronóstico de 5 días (API diferente)
- Crear interfaz gráfica con Tkinter
- Agregar configuración de unidades (Celsius/Fahrenheit)
- Implementar logging con el módulo `logging`
- Agregar soporte para coordenadas GPS

**¡Bienvenido al proyecto!** 🚀

---

*Este documento fue generado automáticamente el 10 de noviembre de 2025 y debe actualizarse cuando haya cambios significativos en el proyecto.*
