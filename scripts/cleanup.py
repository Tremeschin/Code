import shutil
from pathlib import Path

# Caches, artifacts
unwanted: list[str] = [
    "__pycache__",
    ".cache",
    "*.pyc",
    "site",
    "target",
]

for path in Path.cwd().glob("*"):
    if path.name == ".venv":
        continue
    if path.is_file():
        continue

    for pattern in unwanted:
        for path in path.rglob(pattern):
            if input(f"Enter to remove ({path}) ") == "":
                if path.is_dir():
                    shutil.rmtree(path, ignore_errors=True)
                else:
                    path.unlink(missing_ok=True)
