<div align="center">
  <h1>Tremeschin's</h1>
  <span>📦 Main development workspace 📦</span>
  <br><br>
</div>

A monorepo to organize all my professional and personal projects, including libraries, applications, infrastructure and some private components - mainly powered by uv workspaces and python management.

_Not intended for public use or contributions, though may contain useful snippets._

## Setup

For self reference, in case of memory loss:

- Clone the repository, add others at `code/$area/*` as needed (no submodules!)
- Always include .gitignore in Syncthing via `#include` macro before installing
- For non-nvidia, use `uv run poe sync` until it respects auto torch backend
- Open the code-workspace and install recommended extensions
