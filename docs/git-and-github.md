# Save changes with Git and GitHub

[Home](../README.md) · [Publishing](publishing.md)

The encyclopedia belongs in the existing GitHub repository
[aniltheengh/Mathematics-](https://github.com/aniltheengh/Mathematics-), on branch
`main`. The local working copy uses this URL as `origin`:

```text
https://github.com/aniltheengh/Mathematics-.git
```

The repository's original Python `.gitignore` and initial commit history are
preserved. Encyclopedia-specific exclusions cover local tools, caches, generated
book builds, and private notes. Website hosting is optional; storing the files
on GitHub does not automatically deploy a website.

## Open this working copy

From VS Code's PowerShell terminal:

```powershell
Set-Location -LiteralPath 'G:\My Drive\co-ordinates of Geometry'
git status --short --branch
git remote -v
```

Do not run `git init` or add a second `origin` in an already connected working copy.
The remote listing should show the Mathematics- URL for fetch and push.

## Get a fresh copy on another computer

Run this in the parent folder where you want to store the repository:

```powershell
git clone https://github.com/aniltheengh/Mathematics-.git
Set-Location -LiteralPath '.\Mathematics-'
```

Do not clone into an existing working copy. To read the mathematics, open
`README.md`; Python installation is optional.

## Save and upload an edit

First inspect what changed and run the relevant checks:

```powershell
git status
git diff
python scripts/check_repository.py
python scripts/verify_mathematics.py
```

Stage only the files you intended to edit. For example, if you changed only the
progress tracker:

```powershell
git add learning/progress.csv
git diff --cached
git diff --cached --check
git commit -m "Record coordinate geometry revision"
git push origin main
```

For a different change, substitute its actual filenames and describe the result
in the commit message. `git add` selects files for the next commit; `git commit`
saves a local checkpoint; `git push` uploads the commits. A local commit alone
does not update GitHub.

## Confirm synchronization

```powershell
git status --short --branch
git log -1 --oneline
git ls-remote origin refs/heads/main
```

After a successful push, local `main` and `origin/main` should match. The SHA
returned by `git ls-remote` should match the local commit reported by
`git rev-parse HEAD`. If a push is rejected because GitHub has newer commits,
inspect and reconcile the changes; do not force-push to discard history.

If Git asks for identity or sign-in, use your own established Git configuration
and the supported sign-in prompt. Never commit passwords or access tokens.
Keep `.venv`, `.tools`, `.cache`, `_build`, credentials, and private notes out
of version control.

Cloud synchronization is convenient, but Git commits and the GitHub remote
provide deliberate history. Wait for syncing before opening the same working
copy from another computer. For optional book hosting, see [Publishing](publishing.md).
