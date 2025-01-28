[![Test python](https://github.com/open-metadata/collate-dbt-artifacts-parser/actions/workflows/test.yml/badge.svg)](https://github.com/open-metadata/collate-dbt-artifacts-parser/actions/workflows/test.yml)
<a href="https://pypi.org/project/collate-dbt-artifacts-parser" target="_blank">
<img src="https://img.shields.io/pypi/v/collate-dbt-artifacts-parser?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
<a href="https://pypi.org/project/collate-dbt-artifacts-parser" target="_blank">
<img src="https://img.shields.io/pypi/pyversions/collate-dbt-artifacts-parser.svg?color=%2334D058" alt="Supported Python versions">
</a>

# collate-dbt-artifacts-parser

This is a dbt artifacts parse in python.
It enables us to deal with `catalog.json`, `manifest.json`, `run-results.json` and `sources.json` as python objects.

This package is primarily designed for dbt-core, enabling seamless interaction with dbt artifacts as Python objects. While dbt Cloud provides additional artifact types beyond those of dbt-core, this package offer comprehensive support for only `catalog.json`, `manifest.json`, `run-results.json` and `sources.json` of dbt Cloud.

## Supported Versions and Compatibility

> **⚠️ Important Note:**
>
> - **Pydantic v1 will not be supported for dbt 1.9 or later.**
> - **To parse dbt 1.9 or later, please migrate your code to pydantic v2.**
> - **We will reassess version compatibility upon the release of pydantic v3.**

| Version | Supported dbt Version | Supported pydantic Version |
|---------|-----------------------|----------------------------|
|  0.8    | dbt 1.5 to 1.9        | pydantic v2                |
|  0.7    | dbt 1.5 to 1.8        | pydantic v2                |
|  0.6    | dbt 1.5 to 1.8        | pydantic v1                |
|  0.5    | dbt 1.5 to 1.7        | pydantic v1                |

## Installation

```bash
pip install -U collate-dbt-artifacts-parser
```

## Python classes

Those are the classes to parse dbt artifacts.

### Catalog

- [CatalogV1](collate_dbt_artifacts_parser/parsers/catalog/catalog_v1.py) for catalog.json v1
- [CatalogCLOUD](collate_dbt_artifacts_parser/parsers/catalog/catalog_cloud.py) for catalog.json cloud

### Manifest

- [ManifestV1](collate_dbt_artifacts_parser/parsers/manifest/manifest_v1.py) for manifest.json v1
- [ManifestV2](collate_dbt_artifacts_parser/parsers/manifest/manifest_v2.py) for manifest.json v2
- [ManifestV3](collate_dbt_artifacts_parser/parsers/manifest/manifest_v3.py) for manifest.json v3
- [ManifestV4](collate_dbt_artifacts_parser/parsers/manifest/manifest_v4.py) for manifest.json v4
- [ManifestV5](collate_dbt_artifacts_parser/parsers/manifest/manifest_v5.py) for manifest.json v5
- [ManifestV6](collate_dbt_artifacts_parser/parsers/manifest/manifest_v6.py) for manifest.json v6
- [ManifestV7](collate_dbt_artifacts_parser/parsers/manifest/manifest_v7.py) for manifest.json v7
- [ManifestV8](collate_dbt_artifacts_parser/parsers/manifest/manifest_v8.py) for manifest.json v8
- [ManifestV9](collate_dbt_artifacts_parser/parsers/manifest/manifest_v9.py) for manifest.json v9
- [ManifestV10](collate_dbt_artifacts_parser/parsers/manifest/manifest_v10.py) for manifest.json v10
- [ManifestV11](collate_dbt_artifacts_parser/parsers/manifest/manifest_v11.py) for manifest.json v11
- [ManifestV12](collate_dbt_artifacts_parser/parsers/manifest/manifest_v12.py) for manifest.json v12
- [ManifestCLOUD](collate_dbt_artifacts_parser/parsers/manifest/manifest_cloud.py) for manifest.json cloud

### Run Results

- [RunResultsV1](collate_dbt_artifacts_parser/parsers/run_results/run_results_v1.py) for run_results.json v1
- [RunResultsV2](collate_dbt_artifacts_parser/parsers/run_results/run_results_v2.py) for run_results.json v2
- [RunResultsV3](collate_dbt_artifacts_parser/parsers/run_results/run_results_v3.py) for run_results.json v3
- [RunResultsV4](collate_dbt_artifacts_parser/parsers/run_results/run_results_v4.py) for run_results.json v4
- [RunResultsV5](collate_dbt_artifacts_parser/parsers/run_results/run_results_v5.py) for run_results.json v5
- [RunResultsV6](collate_dbt_artifacts_parser/parsers/run_results/run_results_v6.py) for run_results.json v6
- [RunResultsCLOUD](collate_dbt_artifacts_parser/parsers/run_results/run_results_cloud.py) for run_results.json cloud

### Sources

- [SourcesV1](collate_dbt_artifacts_parser/parsers/sources/sources_v1.py) for sources.json v1
- [SourcesV2](collate_dbt_artifacts_parser/parsers/sources/sources_v2.py) for sources.json v2
- [SourcesV3](collate_dbt_artifacts_parser/parsers/sources/sources_v3.py) for sources.json v3
- [SourcesCLOUD](collate_dbt_artifacts_parser/parsers/sources/sources_cloud.py) for sources.json cloud

## Examples

### Parse catalog.json

```python
import json

# parse any version of catalog.json
from collate_dbt_artifacts_parser.parser import parse_catalog

with open("path/to/catalog.json", "r") as fp:
    catalog_dict = json.load(fp)
    catalog_obj = parse_catalog(catalog=catalog_dict)

# parse catalog.json v1
from collate_dbt_artifacts_parser.parser import parse_catalog_v1

with open("path/to/catalog.json", "r") as fp:
    catalog_dict = json.load(fp)
    catalog_obj = parse_catalog_v1(catalog=catalog_dict)
```

### Parse manifest.json

```python
import json

# parse any version of manifest.json
from collate_dbt_artifacts_parser.parser import parse_manifest

with open("path/to/manifest.json", "r") as fp:
    manifest_dict = json.load(fp)
    manifest_obj = parse_manifest(manifest=manifest_dict)

# parse manifest.json v1
from collate_dbt_artifacts_parser.parser import parse_manifest_v1

with open("path/to/manifest.json", "r") as fp:
    manifest_dict = json.load(fp)
    manifest_obj = parse_manifest_v1(manifest=manifest_dict)

# parse manifest.json v2
from collate_dbt_artifacts_parser.parser import parse_manifest_v2

with open("path/to/manifest.json", "r") as fp:
    manifest_dict = json.load(fp)
    manifest_obj = parse_manifest_v2(manifest=manifest_dict)

# parse manifest.json v3
from collate_dbt_artifacts_parser.parser import parse_manifest_v3

with open("path/to/manifest.json", "r") as fp:
    manifest_dict = json.load(fp)
    manifest_obj = parse_manifest_v3(manifest=manifest_dict)

# parse manifest.json v4
from collate_dbt_artifacts_parser.parser import parse_manifest_v4

with open("path/to/manifest.json", "r") as fp:
    manifest_dict = json.load(fp)
    manifest_obj = parse_manifest_v4(manifest=manifest_dict)

# parse manifest.json v5
from collate_dbt_artifacts_parser.parser import parse_manifest_v5

with open("path/to/manifest.json", "r") as fp:
    manifest_dict = json.load(fp)
    manifest_obj = parse_manifest_v5(manifest=manifest_dict)

# parse manifest.json v6
from collate_dbt_artifacts_parser.parser import parse_manifest_v6

with open("path/to/manifest.json", "r") as fp:
    manifest_dict = json.load(fp)
    manifest_obj = parse_manifest_v6(manifest=manifest_dict)

# parse manifest.json v7
from collate_dbt_artifacts_parser.parser import parse_manifest_v7

with open("path/to/manifest.json", "r") as fp:
    manifest_dict = json.load(fp)
    manifest_obj = parse_manifest_v7(manifest=manifest_dict)

# parse manifest.json v8
from collate_dbt_artifacts_parser.parser import parse_manifest_v8

with open("path/to/manifest.json", "r") as fp:
    manifest_dict = json.load(fp)
    manifest_obj = parse_manifest_v8(manifest=manifest_dict)

# parse manifest.json v9
from collate_dbt_artifacts_parser.parser import parse_manifest_v9

with open("path/to/manifest.json", "r") as fp:
    manifest_dict = json.load(fp)
    manifest_obj = parse_manifest_v9(manifest=manifest_dict)

# parse manifest.json v10
from collate_dbt_artifacts_parser.parser import parse_manifest_v10

with open("path/to/manifest.json", "r") as fp:
    manifest_dict = json.load(fp)
    manifest_obj = parse_manifest_v10(manifest=manifest_dict)

# parse manifest.json v11
from collate_dbt_artifacts_parser.parser import parse_manifest_v11

with open("path/to/manifest.json", "r") as fp:
    manifest_dict = json.load(fp)
    manifest_obj = parse_manifest_v11(manifest=manifest_dict)

# parse manifest.json v12
from collate_dbt_artifacts_parser.parser import parse_manifest_v12

with open("path/to/manifest.json", "r") as fp:
    manifest_dict = json.load(fp)
    manifest_obj = parse_manifest_v12(manifest=manifest_dict)
```

### Parse run-results.json

```python
import json

# parse any version of run-results.json
from collate_dbt_artifacts_parser.parser import parse_run_results

with open("path/to/run-resultsjson", "r") as fp:
    run_results_dict = json.load(fp)
    run_results_obj = parse_run_results(run_results=run_results_dict)

# parse run-results.json v1
from collate_dbt_artifacts_parser.parser import parse_run_results_v1

with open("path/to/run-results.json", "r") as fp:
    run_results_dict = json.load(fp)
    run_results_obj = parse_run_results_v1(run_results=run_results_dict)

# parse run-results.json v2
from collate_dbt_artifacts_parser.parser import parse_run_results_v2

with open("path/to/run-results.json", "r") as fp:
    run_results_dict = json.load(fp)
    run_results_obj = parse_run_results_v2(run_results=run_results_dict)

# parse run-results.json v3
from collate_dbt_artifacts_parser.parser import parse_run_results_v3

with open("path/to/run-results.json", "r") as fp:
    run_results_dict = json.load(fp)
    run_results_obj = parse_run_results_v3(run_results=run_results_dict)

# parse run-results.json v4
from collate_dbt_artifacts_parser.parser import parse_run_results_v4

with open("path/to/run-results.json", "r") as fp:
    run_results_dict = json.load(fp)
    run_results_obj = parse_run_results_v4(run_results=run_results_dict)

# parse run-results.json v5
from collate_dbt_artifacts_parser.parser import parse_run_results_v5

with open("path/to/run-results.json", "r") as fp:
    run_results_dict = json.load(fp)
    run_results_obj = parse_run_results_v5(run_results=run_results_dict)

# parse run-results.json v6
from collate_dbt_artifacts_parser.parser import parse_run_results_v6

with open("path/to/run-results.json", "r") as fp:
    run_results_dict = json.load(fp)
    run_results_obj = parse_run_results_v6(run_results=run_results_dict)
```

### Parse sources.json

```python
import json

# parse any version of sources.json
from collate_dbt_artifacts_parser.parser import parse_sources

with open("path/to/sources.json", "r") as fp:
    sources_dict = json.load(fp)
    sources_obj = parse_sources(sources=sources_dict)

# parse sources.json v1
from collate_dbt_artifacts_parser.parser import parse_sources_v1

with open("path/to/sources.json", "r") as fp:
    sources_dict = json.load(fp)
    sources_obj = parse_sources_v1(sources=sources_dict)

# parse sources.json v2
from collate_dbt_artifacts_parser.parser import parse_sources_v2

with open("path/to/sources.json", "r") as fp:
    sources_dict = json.load(fp)
    sources_obj = parse_sources_v2(sources=sources_dict)

# parse sources.json v3
from collate_dbt_artifacts_parser.parser import parse_sources_v3

with open("path/to/sources.json", "r") as fp:
    sources_dict = json.load(fp)
    sources_obj = parse_sources_v3(sources=sources_dict)
```

## Contributors

Thank you for your contributions!

If you are interested in contributing to this package, please check out the [CONTRIBUTING.md](./CONTRIBUTING.md).
