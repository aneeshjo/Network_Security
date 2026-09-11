import os
from pathlib import Path


PROJECT_NAME="Network_Security"
SRC="src"

list_of_files=[
    "Dockerfile",
    "setup.py",
    "main.py",
    "app.py",
    f"{PROJECT_NAME}/__init__.py",
    f"{PROJECT_NAME}/{SRC}/__init__.py",
    f"{PROJECT_NAME}/{SRC}/clouds/__init__.py",

    f"{PROJECT_NAME}/{SRC}/logging/__init__.py",
    f"{PROJECT_NAME}/{SRC}/logging/logger.py",
    f"{PROJECT_NAME}/{SRC}/exception/__init__.py",
    f"{PROJECT_NAME}/{SRC}/exception/exception.py",
    f"{PROJECT_NAME}/{SRC}/constant/__init__.py",
    f"{PROJECT_NAME}/{SRC}/entity/__init__.py",
    f"{PROJECT_NAME}/{SRC}/components/__init__.py",
    f"{PROJECT_NAME}/{SRC}/pipeline/__init__.py",
    f"{PROJECT_NAME}/{SRC}/utils/__init__.py",


]


for file_path in list_of_files:

    file_path = Path(file_path)

    file_directory = file_path.parent

    if file_directory != Path(""):
        os.makedirs(file_directory, exist_ok=True)

    if not file_path.exists():
        file_path.touch()

        print(f"Created: {file_path}")

    else:
        print(f"Already exists: {file_path}")