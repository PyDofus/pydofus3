### pydofus3

Extract and process data from Dofus Unity.

> **Heads up.** This project was not initially designed to be public. It is only tested
> on **Linux**, against both the **Windows** and the **Linux** Dofus client.

#### Key features

- Unified CLI via `typer` (`pydofus3` entry point)
- Unity asset extraction (texture, picto, skins, bones, etc.)
- Datacenter processing with optional i18n enrichment and flags expansion
- Audio `.bank` event extraction
- Ornament rendering
- Obfuscated proto extraction
- OpenAPI schema generation
- IL2CPP `dump.cs` extraction (redux)
- PostgreSQL export with foreign keys and many‑to‑many tables
- Auto-generated datacenter Pydantic model and enums
- Typed code generation from Unity typetrees (stubs, typed dicts)


---

### Requirements

- [`uv`](https://docs.astral.sh/uv/) (recommended)
- Optional: PostgreSQL
- dotnet 10 to run (redux, audio extraction and proto generation)


---

### Install

the project use [`uv`](https://docs.astral.sh/uv/) — [install](https://docs.astral.sh/uv/#installation) it first if you don't have
it. 

macOs and linux
```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

There are two ways to use `pydofus3`, depending on whether
you only want the CLI or also want to use the library inside another project.

#### 1. CLI only — `uv tool install`

Install the `pydofus3` CLI as a globally-available tool, isolated in its own
environment:

```sh
uv tool install git+https://git@github.com/PyDofus/pydofus3.git
pydofus3 --help
```

To pick up a new version later:

```sh
uv tool upgrade pydofus3
```

#### 2. As a dependency of another project — `uv add`

If you want to import `pydofus3` from your own code add it as a dependency:

```sh
uv add "git+https://git@github.com/PyDofus/pydofus3.git" --raw
```

Then run the CLI from the project's environment:

```sh
uv run pydofus3 --help
```


### Shell completion

Enable shell completion (optional but recommended):

```sh
pydofus3 --install-completion
```

### Optional: faster PNG export with `fpng`

PNG writes go through `pydofus3.tools.save_img`, which can use
[`fpng-py`](https://github.com/K0lb3/fpng_py) for much faster encoding. If
`fpng-py` is not installed, the code transparently falls back to Pillow.

`fpng-py` is built from C++ sources at install time, so you need a C++
compiler available on your system (for example `build-essential` on Debian /
Ubuntu, Xcode command line tools on macOS, or MSVC Build Tools on Windows).

Install it via the optional `[fpng]` extra:

```sh
# CLI tool install
uv tool install "git+https://git@github.com/PyDofus/pydofus3.git[fpng]"

# Or as a project dependency
uv add "git+https://git@github.com/PyDofus/pydofus3.git[fpng]" --raw
```

---

### Conventions and paths

- Default output directory: `output/`
- Default game folder path: `output/dofus_unity`
- Many commands accept either a root `dofus_path` or a JSON manifest of
  changed files to minimize work

You can override paths via environment variables (see `pydofus3.config`) or CLI options.

---

### Outputs

Depending on the command, artifacts are written under `output/` with subfolders
per `TypeData` / `TypeDataOther`. Typical layout:

- `output/dofus_unity/` — the game data root you point commands at
- `output/Dofus_Data` - folder where game asset are extracted
- `output/dummyDLL/` — IL2CPP `dump.cs`
- `output/proto/` — generated proto files
- `pydofus3/generated/` — codegen (stubs/typed dicts) when using `stub`/`process`

---

### CLI overview

The CLI groups commands under the main app and a `data` sub‑app.

```sh
pydofus3 --help
pydofus3 data --help
```

#### Data extraction subcommands

The `data` group exposes three subcommands — `file`, `catalog`, `json` — and a
set of **common options that live on the `data` group itself**, not on the
subcommands. They must therefore be passed *before* the subcommand name:

```sh
pydofus3 data [COMMON_OPTIONS]... <file|catalog|json> [SUBCOMMAND_ARGS]...
```

For example:

```sh
pydofus3 data --compress --process-datacenter catalog Data
pydofus3 data --skin-webp catalog Skins output/dofus_unity
pydofus3 data --force-texture2d file /path/to/SomeAssetFile
```

Common options (see `pydofus3/cli/data_extract.py` for the full list):

- `--compress` — compress MonoBehaviour with zstd
- `--force-texture2d` — render sprites as Texture2D
- `--add-script` — add MonoScript class info in MonoBehaviours
- `--process-reference` — resolve references in MonoBehaviours
- `--sprite-rect` — use `m_Rect` to resize sprites (atlas cases)
- `--process-datacenter` — enrich datacenter with i18n + flags
- `--load-all-files` — load all bundles at once (faster, more RAM)
- `--force-gc-collect` — force GC after each file (useful for map textures)
- `--skin-png` — export skin texture as PNG
- `--skin-webp` — export skin texture as WebP (very slow but smaller files)

Subcommands:

Extract a single file (catalog auto-detected from the file path):

```sh
pydofus3 data file /path/to/SomeAssetFile
```

Extract an entire catalog (see `pydofus3/enum_data.py` `TypeData` for names —
`Skins`, `Bones`, `Data`, `Map_Data`, `Picto_Items`, ...):

```sh
pydofus3 data catalog Skins [DOFUS_PATH]
```

Extract a set of files described by a JSON manifest. The JSON can be either:
- a list of relative paths, or
- a dict with `new`, `change`, `remove` keys (lists of relative paths).

```sh
pydofus3 data json change.json output/dofus_unity
```

#### Other top‑level commands

Generate Unity typetree-based Python stubs and TypedDicts:

```sh
pydofus3 stub [DOFUS_PATH] [OUTPUT_GENERATED]
```

Extract ornaments (PNG/WebM):

```sh
pydofus3 ornament [DOFUS_PATH] [OUTPUT_DIR]
```

Extract i18n to JSON:

```sh
pydofus3 i18n [DOFUS_PATH] [OUTPUT_DIR] [--compress/--no-compress]
```

Extract audio bank events:

```sh
pydofus3 audio [DOFUS_PATH] [OUTPUT_DIR] [--file-change path/to/changes.json]
```

Generate an OpenAPI schema from the extracted data:

```sh
pydofus3 open-api [OUTPUT_DIR]
```

Produce IL2CPP `dump.cs` and `dummyDll` via redux:

```sh
pydofus3 dumpcs [DOFUS_PATH] [OUTPUT_DIR]
```

---

### Generated Code

There are several types of generated code: typed dictionaries, stubs designed for direct use with UnityPy classes, and Pydantic models

Pydantic models have been generated for Animator2D, map rendering, and the datacenter. 
However, they are currently only tested and fully functional for the datacenter. For the other parts, they should be considered more as a draft—useful if you want to implement data validation, but likely requiring adjustments.

### Database export (PostgreSQL)

The DB export is handled by `pydofus3.db_dump`. It turns JSON outputs (datacenter and i18n) into PostgreSQL tables, handling:

- primary keys (adds `id_m` when missing or non‑unique `id`)
- one‑to‑many tables from embedded lists of dicts (as `custom_<table>_<field>`)
- many‑to‑many junction tables prefixed with `many_` according to `db_dump.config`
- foreign keys on configured relations

Run a local PostgreSQL with Docker:

```sh
docker compose up -d db
```

Set env variables (or a `.env` file) consumed by `pydofus3.config.Settings`:

```env
DB_USER=postgres
DB_PASSWORD=postgres
DB_NAME=dofus
DB_HOST=localhost
DB_PORT=5432
# optional overrides
DB_CONNECTOR=psycopg
DB_TYPE=postgresql
```

The effective SQLAlchemy DSN is built as:

```
{DB_TYPE}+{DB_CONNECTOR}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}
```

Trigger the export as part of the end‑to‑end pipeline:

```sh
pydofus3 process
```

Or call it programmatically:

```python
from pydofus3.db_dump.process import Processor
Processor().db_dump()
```

---

### Acknowledgements

This project stands on the shoulders of several open-source projects. See [ACKNOWLEDGEMENTS.md](ACKNOWLEDGEMENTS.md) for the full list.
