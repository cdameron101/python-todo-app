<img width="960" height="540" alt="image" src="https://github.com/user-attachments/assets/c2eaeddb-fca4-4fab-8400-d9c97524974e" />
# Python To-Do Application

A Python-based task management application featuring three different interfaces: command-line (CLI), desktop GUI, and Streamlit web application.

## Features

- Add new tasks
- View existing tasks
- Edit tasks using the CLI or desktop GUI
- Mark tasks as completed and remove them
- Save tasks locally using text-file storage
- Access tasks through three different interfaces

## Technologies Used

- **Python** — Core application logic
- **Streamlit** — Web interface
- **FreeSimpleGUI** — Desktop interface
- **Python File I/O** — Persistent task storage
- **Git & GitHub** — Version control and project hosting

## Project Structure

```text
todo-webapp/
├── cli.py
├── gui.py
├── streamlit_app.py
├── functions.py
├── add.png
├── complete.png
├── requirements.txt
├── README.md
└── .gitignore
```

The project also uses a local `todos.txt` file for task storage. Virtual environments, generated files, and personal task data are excluded from GitHub.

## Installation

Clone the repository and navigate into the project directory.

Create and activate a Python virtual environment:

```bash
python -m venv .venv
```

On Windows:

```powershell
.venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create an empty `todos.txt` file in the project directory before running the CLI or Streamlit application.

## Running the Applications

### Streamlit Web App

```bash
python -m streamlit run streamlit_app.py
```

### Desktop GUI

```bash
python gui.py
```

### Command-Line Interface

```bash
python cli.py
```

## What I Learned

This project helped me develop practical experience with:

- Python functions, loops, and conditionals
- Lists and list manipulation
- Reading and writing files
- Importing and organizing Python modules
- Exception handling
- Building desktop and web interfaces
- Managing application state and user interactions

## Future Improvements

- Add task deadlines and priorities
- Improve input validation
- Replace text-file storage with a database
- Add automated tests
- Improve the web interface design

## Project Status

Functional learning project with CLI, desktop GUI, and Streamlit interfaces. Additional improvements are planned.
