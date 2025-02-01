# Setup Environments

## Python

> Install Python from **[python.org](https://www.python.org/downloads/)**

### Virtual Environment

- Setup Virtual Environment

```bash
python -m venv $(VENV_NAME)
```

- Activate Virtual Environment

```bash
source $(PATH_TO_BIN)/activate
```

- Deactivate Virtual Environment

```bash
deactivate
```

### Dependencies

- Setup Custom Module

```bash
pip install -e .
```

- Install Dependencies in requirements.txt

```bash
pip install -r requirements.txt
```

- Export Dependencies to requirements.txt

```bash
# Exclude custom module
pip freeze | grep -v "^-e" > requirements.txt
```
