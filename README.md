# zqnt-utils

Shared utilities for ZQNT services and adapters. Published to GitHub Packages (private registry).

## Installation

### 1. GitHub Token erstellen

Gehe zu [GitHub → Settings → Developer settings → Personal access tokens (classic)](https://github.com/settings/tokens) und erstelle einen Token mit dem Scope:

- `read:packages`

### 2. Token konfigurieren

**Option A – global für uv** (`~/.config/uv/uv.toml`):

```toml
[[index]]
name = "zequent"
url = "https://pypi.pkg.github.com/ZEQUENT_ORG/simple/"
authenticate = true
```

Dann den Token als Umgebungsvariable setzen (z.B. in `.bashrc` / `.zshrc`):

```bash
export UV_INDEX_ZEQUENT_USERNAME=__token__
export UV_INDEX_ZEQUENT_PASSWORD=ghp_deintoken
```

---

**Option B – direkt im Projekt** (`pyproject.toml`):

```toml
[[tool.uv.index]]
name = "zequent"
url = "https://pypi.pkg.github.com/ZEQUENT_ORG/simple/"
authenticate = true
```

Token ebenfalls als Umgebungsvariable (siehe oben) oder in `.env`.

---

**Option C – Token direkt in der URL** (nicht für `.env`-lose CI empfohlen):

```bash
uv add zqnt-utils \
  --index https://__token__:ghp_deintoken@pypi.pkg.github.com/ZEQUENT_ORG/simple/
```

### 3. Package installieren

```bash
uv add zqnt-utils
```

Für eine bestimmte Version:

```bash
uv add zqnt-utils==0.1.0
```

Pre-release (z.B. von einem PR):

```bash
uv add "zqnt-utils==0.1.0.post42.devABC123" --prerelease=allow
```

---

## Verwendung

```python
from zqnt_utils.caching import CachingService, CacheKeys
from zqnt_utils.core import EdgeEndpointDTO
```

### CachingService

Async Redis-Client, der den Java `CachingService` spiegelt.

**Kurzlebig (context manager):**

```python
async with CachingService("redis://localhost:6379") as cache:
    await cache.register_edge_endpoint("DJI", dto)
```

**Langlebig (Adapter-Lifecycle):**

```python
cache = CachingService.from_env()   # liest REDIS_URL aus der Umgebung
await cache.connect()

await cache.register_edge_endpoint("DJI", dto)
await cache.register_asset_vendor("SN-001", "DJI")

await cache.close()
```

### EdgeEndpointDTO

Spiegelt das Java `EdgeEndpointDTO` und serialisiert in dasselbe JSON-Format:

```python
dto = EdgeEndpointDTO(
    endpoint="grpc://adapter.internal:50051",
    online=True,
    asset_type="DOCK",
    asset_vendor="DJI",
)

json_str = dto.to_json()
dto2 = EdgeEndpointDTO.from_json(json_str)
```

### Verfügbare Operationen

| Methode | Beschreibung |
|---|---|
| `register_edge_endpoint(vendor, dto)` | Edge-Endpoint registrieren |
| `get_edge_endpoint(vendor)` | Edge-Endpoint abrufen |
| `deregister_edge_endpoint(vendor)` | Endpoint als offline markieren |
| `delete_edge_endpoint(vendor)` | Endpoint vollständig löschen |
| `register_asset_vendor(sn, vendor)` | Asset-SN → Vendor mappen |
| `get_asset_vendor(sn)` | Vendor für eine Asset-SN abrufen |
| `set(key, value)` | Generisches Redis SET |
| `setex(key, ttl, value)` | Redis SET mit TTL |
| `get(key)` | Generisches Redis GET |
| `delete(*keys)` | Redis DEL |

---

## Umgebungsvariablen

| Variable | Standard | Beschreibung |
|---|---|---|
| `REDIS_URL` | `redis://localhost:6379` | Redis-Verbindungs-URL |
