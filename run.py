#!/usr/bin/env python
"""
Script de entrada para ejecutar Weather CLI.

Este script actúa como wrapper para ejecutar el módulo src.main como paquete
Python, permitiendo que los imports relativos funcionen correctamente.

El problema que resuelve:
    - src/main.py usa imports relativos (.weather_service, .weather_formatter)
    - Los imports relativos requieren que el código se ejecute como módulo
    - Ejecutar directamente "python src/main.py" causa ImportError
    - Este script ejecuta "src.main" como módulo usando runpy.run_module()

Uso:
    python run.py

Alternativa:
    python -m src.main

Note:
    NO ejecutar directamente "python src/main.py" porque fallará con ImportError
    debido a los imports relativos.
"""

if __name__ == "__main__":
    # Ejecutar src.main como módulo preservando la estructura de paquete
    # Esto permite que los imports relativos (.weather_service, etc.) funcionen
    import runpy
    runpy.run_module("src.main", run_name="__main__")
