<p align="center">
  <a href="README.md">English</a> | <strong>Español</strong>
</p>

<h1 align="center">⚙️ GitHub Actions Lab</h1>

<p align="center">
  <strong>Aprende GitHub Actions con código, pruebas y automatización.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/GitHub_Actions-CI%2FCD-2088FF?logo=githubactions&amp;logoColor=white" alt="GitHub Actions: CI/CD">
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?logo=python&amp;logoColor=white" alt="Python 3.12">
  <img src="https://img.shields.io/badge/Status-Learning_Project-6A9955" alt="Estado: Proyecto de aprendizaje">
  <a href="https://github.com/AstronomicalDeveloper/github-actions-lab/actions/workflows/ci.yml"><img src="https://github.com/AstronomicalDeveloper/github-actions-lab/actions/workflows/ci.yml/badge.svg" alt="Estado del workflow MiniCalc CI"></a>
</p>

<p align="center">
  <strong>🧪 Python · Pruebas unitarias · Integración continua</strong>
</p>

La idea es sencilla: una calculadora en Python, dos tests y un workflow que los ejecuta con cada `push` o `pull_request`. Un punto de partida para practicar integración continua y entender qué pasa entre subir código y ver el check verde. ✅

## 🎯 ¿Qué se practica aquí?

- Configuración de workflows con YAML.
- Eventos que disparan una ejecución: `push` y `pull_request`.
- Organización de jobs y steps.
- Preparación de Python en un runner de GitHub Actions.
- Ejecución automática de pruebas con `unittest`.
- Lectura de resultados y diagnóstico de fallos en CI.

## 📁 Estructura del proyecto

```text
github-actions-lab/
├── .github/
│   └── workflows/
│       └── ci.yml           # Workflow de integración continua
├── py/
│   ├── calculadora.py       # Función sumar(a, b)
│   └── test_calculadora.py  # Pruebas unitarias
├── .gitignore
├── README.md               # Inglés (predeterminado)
└── README.es.md            # Español
```

## 🚀 Ejecutar las pruebas localmente

Usa **Python 3.12** para trabajar con la misma versión que el workflow. Las pruebas usan `unittest`, incluido en Python, así que no hace falta instalar dependencias externas. 📦

Clona el repositorio y entra en su carpeta:

```bash
git clone https://github.com/AstronomicalDeveloper/github-actions-lab.git
cd github-actions-lab
```

Ejecuta este comando desde la raíz del proyecto:

```bash
python -m unittest discover -s py -v
```

Las pruebas comprueban la suma de números positivos y negativos. Si todo va bien, verás un resultado como este:

```text
test_numeros_negativos (test_calculadora.TestCalculadora.test_numeros_negativos) ... ok
test_suma (test_calculadora.TestCalculadora.test_suma) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

> 💡 El argumento `-s py` indica dónde buscar las pruebas. Con la estructura actual, ejecutar `discover` desde la raíz sin ese argumento no encuentra los tests de esa carpeta.

## ⚙️ ¿Cómo funciona el workflow?

El archivo [`.github/workflows/ci.yml`](.github/workflows/ci.yml) define **MiniCalc CI**, que se ejecuta con cada `push` y `pull_request`.

El job `test` usa un runner `ubuntu-latest` y realiza tres pasos:

1. **📥 Obtener el código:** descarga el repositorio con `actions/checkout`.
2. **🐍 Configurar Python:** prepara Python 3.12 con `actions/setup-python`.
3. **🧪 Ejecutar las pruebas:** lanza `python -m unittest discover -s py -v`.

Puedes consultar las ejecuciones y sus logs en la pestaña [**Actions**](https://github.com/AstronomicalDeveloper/github-actions-lab/actions). Si una prueba falla, el comando devuelve un código de salida distinto de cero y el job queda marcado como fallido. 🔴

## 🔬 Un experimento para aprender

1. Cambia temporalmente `return a + b` por `return a - b` en `py/calculadora.py`.
2. Ejecuta las pruebas localmente y observa los errores.
3. Si quieres comprobarlo en GitHub, sube el cambio a una rama de prueba y revisa la ejecución en **Actions**.
4. Restaura la suma y ejecuta las pruebas otra vez para recuperar el verde. 🟢

---

Hecho para aprender, romper cosas y entender por qué funcionan. 🛠️✨
