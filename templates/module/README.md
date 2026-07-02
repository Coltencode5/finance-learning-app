# Module template

Scaffold files for a new five-zone module. Placeholders use `{{TOKEN}}` syntax.

## Files

| File | Purpose |
|---|---|
| `module.template.json` | Module metadata (`module.json`) |
| `zone.template.json` | One zone file (`zones/zN.json`) — array of nodes |

## Placeholders

| Token | Example | Notes |
|---|---|---|
| `{{MODULE_SLUG}}` | `corporate-finance` | Lowercase, hyphens; becomes node ID prefix |
| `{{MODULE_TITLE}}` | `Corporate Finance` | Display title |
| `{{BUILD_ORDER}}` | `10` | Auto-assigned by scaffold script |
| `{{ZONE_NUM}}` | `1` | Zone number 1–5 |
| `{{ZONE_TITLE}}` | `The Ecosystem` | Zone heading in module.json |
| `{{LOCAL_ID}}` | `Z1.1` | Human-facing node ID |
| `{{NODE_TITLE}}` | `PLACEHOLDER — Zone 1 front door` | Node title |

## Required node fields (canonical)

Every node must include: `id`, `local_id`, `module`, `zone`, `ordinal`, `title`,
`tag`, `global_id`, `quick_definition`, `explainer_covers`, `connects_to`,
`gaps`, `status`.

- **Node ID:** `{slug}.z{zone}.{ordinal}` e.g. `corporate-finance.z1.1`
- **Global refs:** `G{n}` in `connects_to` — must exist in `globals.json`
- **Cross-module refs:** `{other-slug}.z{zone}.{n}` — target must exist when module is active
- **Gaps:** structured `{ "kind": "source"|"recency", "note": "..." }` objects

## New module globals

When a module mints new globals, they must start at **G236** (next after G235)
and be contiguous. Run the validator after adding globals.

## Visibility

New scaffolds default to `"visibility": "draft"`. Draft modules are excluded
from strict validation, graph build, and the app until promoted:

```json
"visibility": "active"
```

## Do not

- Hand-edit `derived` counts in `module.json` (build pipeline owns these)
- Add finance content in the scaffold step — use placeholders only
- Set `visibility: active` until content passes validation
