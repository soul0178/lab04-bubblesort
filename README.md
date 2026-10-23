# Laboratorio 04 - Pruebas unitarias con unittest y cobertura (Python)

Ingeniería de Software II - bubbleSort con 4 casos de prueba (V(G) = 4).

## Herramientas
- Python 3, unittest (xUnit), Coverage.py (vía pytest-cov), pytest-html

## Cómo ejecutar
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Pruebas
python -m pytest -v --html=reports/reporte_ejecucion.html --self-contained-html

# Cobertura (líneas + ramas)
python -m pytest --cov=src --cov-branch --cov-report=term-missing --cov-report=html:reports/cobertura_html
```

## Estructura
- `src/ordenador.py`: implementación de bubble_sort
- `tests/test_ordenador.py`: CP1 a CP4 (un test por camino independiente)
- `reports/`: reporte de ejecución y de cobertura (HTML)
