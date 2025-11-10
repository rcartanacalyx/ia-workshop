# 🔒 Política de Seguridad

## Reporte de Vulnerabilidades de Seguridad

Si descubres una vulnerabilidad de seguridad en este proyecto, por favor repórtala de forma responsable:

1. **NO** abras un issue público en GitHub
2. Contacta al mantenedor directamente: [@rcartanacalyx](https://github.com/rcartanacalyx)
3. Proporciona detalles sobre la vulnerabilidad
4. Espera una respuesta en un plazo de 48 horas

## ⚠️ API Key Expuesta - Acción Inmediata Requerida

### Situación Detectada

Se detectó que la API key de OpenWeatherMap puede estar expuesta. Si has compartido tu archivo `.env` o has commiteado credenciales, sigue estos pasos **INMEDIATAMENTE**.

### 🚨 Pasos de Remediación (URGENTE)

#### 1. Revocar API Key Comprometida

```
1. Ir a: https://home.openweathermap.org/api_keys
2. Iniciar sesión con tu cuenta
3. Localizar la API key que aparezca en tu archivo .env
4. Hacer clic en el botón "Delete" o "Revoke"
5. Confirmar la eliminación
```

#### 2. Generar Nueva API Key

```
1. En la misma página: https://home.openweathermap.org/api_keys
2. Hacer clic en "Create Key"
3. Dar un nombre descriptivo (ej: "Weather CLI - Nov 2025")
4. Copiar la nueva API key generada
5. Esperar 10-30 minutos para activación
```

#### 3. Actualizar Configuración Local

```powershell
# 1. Abrir el archivo .env
code .env
# o
notepad .env

# 2. Reemplazar la API key antigua con la nueva
OPENWEATHER_API_KEY=tu_nueva_api_key_aqui

# 3. Guardar y cerrar
```

#### 4. Verificar que .env NO esté en Git

```powershell
# Verificar que .env esté en .gitignore
Select-String -Path .gitignore -Pattern "\.env"
# Debe mostrar: .env

# Verificar que .env NO esté siendo trackeado
git ls-files | Select-String "\.env"
# NO debe mostrar resultados

# Verificar el status
git status
# .env NO debe aparecer en "Changes to be committed" ni "Untracked files"
```

#### 5. Limpiar Historial de Git (Si Fue Commiteado)

**⚠️ ADVERTENCIA: Esto reescribe el historial de git**

```powershell
# Verificar si .env está en el historial
git log --all --full-history -- .env

# Si muestra commits, ejecutar:
git filter-branch --force --index-filter `
  "git rm --cached --ignore-unmatch .env" `
  --prune-empty --tag-name-filter cat -- --all

# Forzar actualización de referencias
git for-each-ref --format="delete %(refname)" refs/original | git update-ref --stdin

# Garbage collection agresivo
git reflog expire --expire=now --all
git gc --prune=now --aggressive

# Si ya fue pusheado a GitHub, forzar push (PELIGROSO)
# git push origin --force --all
# git push origin --force --tags
```

#### 6. Verificar en GitHub

```
1. Ir a: https://github.com/rcartanacalyx/ia-workshop
2. Buscar archivos con Ctrl+F o la barra de búsqueda
3. Buscar: "OPENWEATHER_API_KEY"
4. Buscar tu API key específica
5. Si aparecen resultados, el archivo fue pusheado
6. Seguir pasos de limpieza de historial arriba
```

## 🛡️ Prevención de Exposición de Credenciales

### Configuración Correcta del Proyecto

#### 1. Archivo `.gitignore` (✅ Ya configurado)

```gitignore
# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/
```

#### 2. Archivo `.env.example` (Plantilla sin secretos)

```bash
# OpenWeatherMap API Configuration
OPENWEATHER_API_KEY=your_api_key_here
WEATHER_LANG=es
REQUEST_TIMEOUT=10
```

#### 3. Archivo `.env` (Local, NO versionado)

```bash
# OpenWeatherMap API Configuration
OPENWEATHER_API_KEY=abc123tu_api_key_real_aqui
WEATHER_LANG=es
REQUEST_TIMEOUT=10
```

### Herramientas de Prevención

#### Git Secrets

Previene que commits con secretos lleguen al repositorio.

```powershell
# Instalar git-secrets (requiere Homebrew o manual)
# En Windows, descargar desde: https://github.com/awslabs/git-secrets

# Configurar en el repositorio
cd C:\Projects\ia-workshop
git secrets --install

# Agregar patrones para detectar
git secrets --add 'OPENWEATHER_API_KEY=[^y][^o][^u][^r].*'
git secrets --add '[0-9a-f]{32}'

# Escanear commits existentes
git secrets --scan-history
```

#### Pre-commit Hooks

Crear `.git/hooks/pre-commit`:

```bash
#!/bin/sh
# Verificar que .env no esté siendo commiteado

if git diff --cached --name-only | grep -E '^\.env$'; then
    echo "❌ ERROR: Intentando commitear archivo .env"
    echo "Este archivo contiene secretos y NO debe ser versionado."
    echo "Usa .env.example en su lugar."
    exit 1
fi

# Buscar patrones de API keys en archivos staged
if git diff --cached | grep -E 'OPENWEATHER_API_KEY=[^y][^o][^u]'; then
    echo "❌ ERROR: API key detectada en archivos staged"
    echo "Remueve la API key antes de commitear."
    exit 1
fi

exit 0
```

#### TruffleHog (Buscar secretos en historial)

```powershell
# Instalar
pip install trufflehog3

# Escanear repositorio
trufflehog --regex --entropy=True .
```

## ✅ Checklist de Seguridad

Antes de hacer push a GitHub:

- [ ] `.env` está en `.gitignore`
- [ ] `.env` NO aparece en `git status`
- [ ] `.env` NO aparece en `git ls-files`
- [ ] No hay API keys hardcodeadas en código fuente
- [ ] Usas `.env.example` como plantilla pública
- [ ] Has escaneado con `git secrets --scan-history`
- [ ] Has revisado el diff: `git diff HEAD`
- [ ] Has configurado pre-commit hooks

## 📚 Recursos Adicionales

- [OpenWeatherMap API Security Best Practices](https://openweathermap.org/faq#error401)
- [GitHub: Removing sensitive data from a repository](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)
- [Git Secrets Tool](https://github.com/awslabs/git-secrets)
- [TruffleHog - Find secrets in Git](https://github.com/trufflesecurity/trufflehog)
- [OWASP: Key Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html)

## 🔄 Rotación de API Keys (Recomendado)

**Frecuencia sugerida**: Cada 90 días o inmediatamente si hay sospecha de compromiso.

**Proceso**:
1. Generar nueva API key en OpenWeatherMap
2. Actualizar `.env` con nueva key
3. Probar que la aplicación funciona: `python run.py`
4. Revocar API key antigua después de confirmar que la nueva funciona
5. Documentar la rotación (fecha, razón)

---

**Última actualización**: 10 de noviembre de 2025  
**Mantenedor**: [@rcartanacalyx](https://github.com/rcartanacalyx)
