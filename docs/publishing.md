# Publish a searchable mathematics book

[Home](../README.md) · [Git and GitHub](git-and-github.md)

The Markdown repository works on its own. This optional route builds a
searchable book with Jupyter Book 2 / MyST and can publish it through GitHub Pages.

## Install and preview

Use Python 3.11+ and a supported Node.js installation; Node.js 24 is the baseline
used by the verification workflow. Install Node from its official distribution
if `node --version` is unavailable. Then, from the repository root:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt -r requirements-book.txt
node --version
.\.venv\Scripts\python.exe scripts/build_book.py
.\.venv\Scripts\python.exe -m http.server 8765 --bind 127.0.0.1 --directory _build/html
```

Open `http://127.0.0.1:8765`. Stop the preview with Ctrl+C. The first build
downloads the theme and needs internet. Generated static files are written to
`_build/html`; do not commit `_build`.

The [build helper](../scripts/build_book.py) copies public source directories into
local temporary storage, builds there with strict checking, then copies the HTML
back. This avoids the npm extraction errors observed when building directly on
the mounted Google Drive. If you add a new top-level source directory, add it to
`SOURCE_DIRS` in the helper. It does not copy `.git`, environments, or private notes.
After a successful build, it replaces only the generated `_build/html` directory
so removed pages do not leave obsolete HTML behind. Keep personal files outside
that generated directory.

For a normal local checkout, the direct commands also work:

```powershell
.\.venv\Scripts\jupyter-book.exe build --html --strict
.\.venv\Scripts\jupyter-book.exe start
```

The local verification used Node.js 22.16.0; the workflow selects Node.js 24.

`myst.yml` is the publication configuration. The explicit TOC contains only real
pages. `--strict` turns warnings into failures; fix missing links or metadata
before publishing. Notebook outputs are committed, so a book build need not
silently run mathematical code. Execute the notebook explicitly with
`python scripts/execute_notebook.py` whenever changing its code.

## GitHub Pages

First follow the Git guide to create and push your GitHub repository. With an
active environment, ask Jupyter Book to generate its deployment workflow:

```powershell
.\.venv\Scripts\jupyter-book.exe init --gh-pages
```

Select branch `main` and a filename such as `deploy.yml`. Review the generated
file in `.github/workflows/`; keep the existing `check.yml` validation workflow.
Add `--strict` to the generated HTML build command if it is absent.

In the GitHub repository, choose **Settings → Pages → Source → GitHub Actions**.
Commit and push the generated workflow after reviewing it:

```powershell
git add .github/workflows/deploy.yml
git diff --cached
git commit -m "Configure mathematics book publication"
git push
```

Check the Actions run and the resulting Pages URL. A project repository is
normally served beneath `/repository-name`; the generated workflow handles the
base path. A user site named `YOUR-USERNAME.github.io` or a custom domain needs
different base-path settings. Use the official deployment guide if changing that.

No deployment workflow is enabled by this initial setup, and nothing has been
published. The supplied workflow verifies changes without publishing them.

## Official references

- [Jupyter Book installation](https://jupyterbook.org/stable/get-started/install/)
- [Jupyter Book website build and strict mode](https://jupyterbook.org/stable/build-and-publish/website)
- [MyST table of contents](https://mystmd.org/guide/table-of-contents)
- [MyST GitHub Pages deployment and base paths](https://mystmd.org/guide/deployment-github-pages)
