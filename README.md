
# Console Tasker - README

## Description

Console Tasker is a command-line interface (CLI) tool written in Python that helps you manage and automate tasks directly from your terminal. It provides functions to add, list, and mark tasks as completed. You can customize and extend it as needed.

---

## Installation

### Python Installation

1. Make sure you have Python 3.8 or higher installed. You can download it from [python.org](https://www.python.org/downloads/).
2. (Optional) Create and activate a virtual environment:
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  ```
4. Run the CLI:
  ```bash
  python app.py
  ```

### Docker Installation

1. Make sure you have Docker installed. You can download it from [docker.com](https://www.docker.com/get-started).
2. Build the Docker image:
  ```bash
  docker build -t console-tasker .
  ```
3. Run the CLI in a container:
  ```bash
  docker run --rm -it console-tasker
  ```


## Usage Examples

### Add a new task
```bash
python app.py add "Buy groceries"
```

### List all tasks
```bash
python app.py list
```

### Mark a task as completed
```bash
python app.py complete 1
```

### Remove a task
```bash
python app.py remove 1
```


For more details, check the code or contact the project maintainer.
