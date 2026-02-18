### pydofus3

Extract and process data from Dofus Unity.

#### Key features

- Unified CLI via `typer` (`pydofus3` entry point)
- Unity asset extraction (images, sprites, maps, picto, skins, bones, etc.)
- Datacenter processing with optional i18n enrichment and flags expansion
- JSON outputs, with options for compression and reference resolution
- Typed code generation from Unity typetrees (stubs, typed dicts)
- Audio `.bank` event extraction
- Ornament rendering
- obfu Proto
- OpenAPI schema generation
- IL2CPP `dump.cs` extraction (redux)
- PostgreSQL export with foreign keys and many‑to‑many tables
- Auto-generated datacenter pydantic model and enums (deprecated for now, needs to be updated for Redux)

---

### Requirements
- Python 3.14+
- Recommended: `uv`
- Optional: Docker (to quickly spin up PostgreSQL via `docker-compose.yml`)

Note: The project pins/builds with `uv_build`. Standard `pip` also works as long as dependencies resolve on your platform.

---

### Install

Using uv (recommended):
- If you don't have uv: https://docs.astral.sh/uv/
- Install the CLI directly from GitHub (no clone):

```
uv tool install git+ssh://git@github.com/PyDofus/pydofus3.git
# then:
pydofus3 --help
```

- from the repo root:
```
uv sync
```

This creates a virtualenv and installs all dependencies. Then run the CLI with:

```
uv run pydofus3 --help
```

- To add as a dependency in another uv project:

```
uv add "git+ssh://git@github.com/PyDofus/pydofus3.git" --raw
```

---

### Conventions and paths
- Default output directory: `output/`
- Default game folder path: `output/dofus_unity`
- Many commands accept either a root `dofus_path` or a list of changed files (JSON) to minimize work

You can override any of these paths via environment variables (cf  `pydofus3.config`) or cli options.

---

### Outputs
Depending on the command, artifacts are written under `output/` with subfolders per `TypeData`/`TypeDataOther`. Typical layout:
- `output/dofus_unity/` the game data root you point commands at
- `output/dummyDLL/` IL2CPP `dump.cs`
- `output/proto/` generated proto files
- `pydofus3/generated/` codegen (stubs/typed dicts) when using `stub`/`process`

---

### CLI overview
The CLI groups commands under the main app and a `data` sub‑app.

List all commands:
```
pydofus3 --help
pydofus3 data --help
```

#### Data extraction subcommands
- Extract a single file (auto‑detect its catalog):
```
pydofus3 data file /path/to/SomeAssetFile
```

- Extract an entire catalog (see `pydofus3/enum_data.py` `TypeData` for names):
```
pydofus3 data catalog <CATALOG_NAME> [DOFUS_PATH]
```

- Extract a set of files described by JSON:
  - The JSON can be:
    - a list of relative paths, or
    - a dict with `new`, `change`, `remove` (lists of relative paths)
```
pydofus3 data json change.json output/dofus_unity
```

Common options available on `pydofus3 data ...` commands (see `pydofus3/cli/data_extract.py` for full list):
- `--compress` compress monobehaviour payloads with zstd
- `--force-texture2d` render sprites as Texture2D
- `--add-typetree` include typetree data
- `--add-script` add scripts in monobehaviours
- `--process-reference` resolve references in monobehaviours
- `--sprite-rect` use `m_Rect` to resize sprite (atlas cases)
- `--process-datacenter` enrich datacenter with i18n, flags
- `--load-all-files` load all files at once (faster, more RAM)
- `--force-gc-collect` force GC on each file (useful for map textures)

#### Other top‑level commands
- Generate Unity typetree based Python stubs and typed dicts:
```
pydofus3 stub [DOFUS_PATH] [OUTPUT_GENERATED]
```

- Extract ornaments (PNG/WebM):
```
pydofus3 ornament [DOFUS_PATH] [OUTPUT_DIR]
```

- Extract i18n to JSON:
```
pydofus3 i18n [OUTPUT_DIR] [I18N_FOLDER] [--compress/--no-compress]
```

- Extract audio bank events:
```
pydofus3 audio [DOFUS_PATH] [OUTPUT_DIR] [--file-change path/to/changes.json]
```

- Generate OpenAPI schema from the extracted data:
```
pydofus3 open-api [OUTPUT_DIR]
```

- Produce IL2CPP `dump.cs` via redux:
```
pydofus3 dumpcs [DOFUS_PATH] [OUTPUT_DIR] [--ida-script]
```

- End‑to‑end incremental processing after an update:
```
pydofus3 process [OUTPUT_DIR] [OUTPUT_GENERATED]
```
This command will:
  - read `output/dofus_unity/change.json`
  - group changed files by catalog and run targeted extractions
  - adjust extractor options per catalog heuristics (textures, datacenter, maps, audio, etc.)
  - regenerate stubs for typetrees
  - dump game data to PostgreSQL (see DB section)
  - run `redux` to refresh `dump.cs`
  - regenerate `proto`

- Validate/process datacenter only with Pydantic checks:
```
pydofus3 process-data [OUTPUT_DIR]
```

---

### Database export (PostgreSQL)
The DB export is handled by `pydofus3.db_dump`. It turns JSON outputs (datacenter and i18n) into PostgreSQL tables, handling:
- primary keys (adds `id_m` when missing or non‑unique `id`)
- one‑to‑many tables from embedded lists of dicts (as `custom_<table>_<field>`)
- many‑to‑many junction tables prefixed with `many_` according to `db_dump.config`
- foreign keys on configured relations

Run a local PostgreSQL with Docker:
```
docker compose up -d db
```
Set env variables (or a `.env` file) consumed by `pydofus3.config.Settings`:
```
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
```
pydofus3 process
```
Or call it programmatically:
```python
from pydofus3.db_dump.process import Processor
Processor().db_dump()
```

---
