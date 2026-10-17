"""Build Jupyter Book in local temporary storage, then copy HTML to the project.

This avoids dependency-extraction failures on some cloud-mounted filesystems.
Install requirements-book.txt in the active Python environment first.
"""

from pathlib import Path
import os
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIRS = (
    "subjects", "indexes", "exercises", "solutions", "assets", "notebooks",
    "scripts", "references", "learning", "templates", "docs",
)


def main():
    with tempfile.TemporaryDirectory(prefix="mathematics-book-") as directory:
        local = Path(directory)
        for item in ROOT.iterdir():
            if item.is_file() and item.suffix in {".md", ".yml", ".yaml", ".txt"}:
                shutil.copy2(item, local / item.name)
        for name in SOURCE_DIRS:
            source = ROOT / name
            if source.is_dir():
                shutil.copytree(source, local / name,
                                ignore=shutil.ignore_patterns("__pycache__", ".ipynb_checkpoints"))
        env = dict(os.environ)
        env["npm_config_cache"] = str(local / ".npm-cache")
        print(f"Building in temporary local storage: {local}", flush=True)
        subprocess.run([sys.executable, "-m", "jupyter_book", "build", "--html", "--strict"],
                       cwd=local, env=env, check=True)
        destination = (ROOT / "_build" / "html").resolve()
        expected_parent = (ROOT / "_build").resolve()
        if destination.parent != expected_parent or expected_parent.parent != ROOT:
            raise RuntimeError("Generated HTML destination must stay inside this project's _build folder.")
        if destination.exists():
            shutil.rmtree(destination)  # Only the verified, generated HTML directory.
        shutil.copytree(local / "_build" / "html", destination)
        print(f"Book copied to {destination}", flush=True)
        print("Preview: python -m http.server 8765 --bind 127.0.0.1 --directory _build/html")


if __name__ == "__main__":
    main()
