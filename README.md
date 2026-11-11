<p align="center">
  <strong>English</strong> | <a href="README.es.md">Español</a>
</p>

<h1 align="center">⚙️ GitHub Actions Lab</h1>

<p align="center">
  <strong>Learn GitHub Actions through code, tests, and automation.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/GitHub_Actions-CI%2FCD-2088FF?logo=githubactions&amp;logoColor=white" alt="GitHub Actions: CI/CD">
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?logo=python&amp;logoColor=white" alt="Python 3.12">
  <img src="https://img.shields.io/badge/Status-Learning_Project-6A9955" alt="Status: Learning Project">
  <a href="https://github.com/AstronomicalDeveloper/github-actions-lab/actions/workflows/ci.yml"><img src="https://github.com/AstronomicalDeveloper/github-actions-lab/actions/workflows/ci.yml/badge.svg" alt="MiniCalc CI workflow status"></a>
</p>

<p align="center">
  <strong>🧪 Python · Unit testing · Continuous integration</strong>
</p>

The idea is simple: a Python calculator, two tests, and a workflow that runs them on every `push` or `pull_request`. A starting point for practicing continuous integration and understanding what happens between pushing code and seeing that green check. ✅

## 🎯 What you'll practice

- Configuring workflows with YAML.
- Triggering workflow runs with `push` and `pull_request` events.
- Organizing jobs and steps.
- Setting up Python on a GitHub Actions runner.
- Running tests automatically with `unittest`.
- Reading results and troubleshooting CI failures.

## 📁 Project structure

```text
github-actions-lab/
├── .github/
│   └── workflows/
│       └── ci.yml           # Continuous integration workflow
├── py/
│   ├── calculadora.py       # sumar(a, b) function
│   └── test_calculadora.py  # Unit tests
├── .gitignore
├── README.md               # English (default)
└── README.es.md            # Spanish
```

## 🚀 Run the tests locally

Use **Python 3.12** to match the workflow's version. The tests use Python's built-in `unittest` module, so there's no need to install any external dependencies. 📦

Clone the repository and open its directory:

```bash
git clone https://github.com/AstronomicalDeveloper/github-actions-lab.git
cd github-actions-lab
```

Run this command from the project root:

```bash
python -m unittest discover -s py -v
```

The tests check addition with positive and negative numbers. If everything works, you'll see output like this:

```text
test_numeros_negativos (test_calculadora.TestCalculadora.test_numeros_negativos) ... ok
test_suma (test_calculadora.TestCalculadora.test_suma) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

> 💡 The `-s py` argument tells `unittest` where to look for tests. With the current project structure, running `discover` from the root without this argument won't find the tests in that folder.

## ⚙️ How the workflow works

The [`.github/workflows/ci.yml`](.github/workflows/ci.yml) file defines **MiniCalc CI**, which runs on every `push` and `pull_request`.

The `test` job uses an `ubuntu-latest` runner and performs three steps:

1. **📥 Check out the code:** fetches the repository using `actions/checkout`.
2. **🐍 Set up Python:** prepares Python 3.12 using `actions/setup-python`.
3. **🧪 Run the tests:** executes `python -m unittest discover -s py -v`.

You can view workflow runs and their logs in the [**Actions** tab](https://github.com/AstronomicalDeveloper/github-actions-lab/actions). If a test fails, the command returns a nonzero exit code and the job is marked as failed. 🔴

## 🔬 Try a little experiment

1. Temporarily change `return a + b` to `return a - b` in `py/calculadora.py`.
2. Run the tests locally and inspect the failures.
3. To try it on GitHub, push the change to a test branch and check the run in **Actions**.
4. Restore the addition and run the tests again to get back to green. 🟢

---

Built to learn, break things, and figure out how they work. 🛠️✨
