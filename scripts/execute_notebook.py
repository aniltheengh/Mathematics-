"""Execute the example in a fresh kernel and save outputs only after success."""

from pathlib import Path
import os

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".cache" / "matplotlib"))
os.environ.setdefault("IPYTHONDIR", str(ROOT / ".cache" / "ipython"))
os.environ.setdefault("JUPYTER_RUNTIME_DIR", str(ROOT / ".cache" / "jupyter"))

import nbformat
from nbclient import NotebookClient


def main():
    path = ROOT / "notebooks" / "coordinate-geometry.ipynb"
    notebook = nbformat.read(path, as_version=4)
    nbformat.validate(notebook)
    client = NotebookClient(notebook, timeout=120, kernel_name="python3",
                            resources={"metadata": {"path": str(path.parent)}})
    client.execute()
    for cell in notebook.cells:
        cell.metadata.pop("execution", None)  # Keep diffs free of run timestamps.
    nbformat.validate(notebook)
    path.write_text(nbformat.writes(notebook), encoding="utf-8", newline="\n")
    code_cells = sum(c.cell_type == "code" for c in notebook.cells)
    print(f"Executed {code_cells} code cells successfully; saved {path.name}")


if __name__ == "__main__":
    main()
