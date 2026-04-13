> [!IMPORTANT]
> This repository is the main development environment for all my professional and personal projects, including libraries, applications, infrastructure and some private components.

## Setup

> [!NOTE]
> Submodules are discouraged as their metadata exists on the origin:
> - Better flexibility to structure and move directories around.
> - Avoids misuse and issues when renaming or syncing-hell.

Clone the repository and others as needed under `meta/*/*`:

```bash
$ git clone https://github.com/Tremeschin/Code && cd Code
$ git clone https://github.com/BrokenSource/Pyaket meta/broken/Pyaket
$ git clone https://github.com/Tremeschin/nvibrant meta/personal/nvibrant
...
```

- **Python**: `uv sync --all-packages`
