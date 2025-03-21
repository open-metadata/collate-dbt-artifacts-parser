#
#  Licensed to the Apache Software Foundation (ASF) under one or more
#  contributor license agreements.  See the NOTICE file distributed with
#  this work for additional information regarding copyright ownership.
#  The ASF licenses this file to You under the Apache License, Version 2.0
#  (the "License"); you may not use this file except in compliance with
#  the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
from dataclasses import dataclass
from enum import Enum
from typing import Type

from collate_dbt_artifacts_parser.parsers.base import BaseParserModel
from collate_dbt_artifacts_parser.parsers.catalog.catalog_v1 import CatalogV1
from collate_dbt_artifacts_parser.parsers.manifest.manifest_v1 import ManifestV1
from collate_dbt_artifacts_parser.parsers.manifest.manifest_v2 import ManifestV2
from collate_dbt_artifacts_parser.parsers.manifest.manifest_v3 import ManifestV3
from collate_dbt_artifacts_parser.parsers.manifest.manifest_v4 import ManifestV4
from collate_dbt_artifacts_parser.parsers.manifest.manifest_v5 import ManifestV5
from collate_dbt_artifacts_parser.parsers.manifest.manifest_v6 import ManifestV6
from collate_dbt_artifacts_parser.parsers.manifest.manifest_v7 import ManifestV7
from collate_dbt_artifacts_parser.parsers.manifest.manifest_v8 import ManifestV8
from collate_dbt_artifacts_parser.parsers.manifest.manifest_v9 import ManifestV9
from collate_dbt_artifacts_parser.parsers.manifest.manifest_v10 import ManifestV10
from collate_dbt_artifacts_parser.parsers.manifest.manifest_v11 import ManifestV11
from collate_dbt_artifacts_parser.parsers.manifest.manifest_v12 import ManifestV12
from collate_dbt_artifacts_parser.parsers.run_results.run_results_v1 import RunResultsV1
from collate_dbt_artifacts_parser.parsers.run_results.run_results_v2 import RunResultsV2
from collate_dbt_artifacts_parser.parsers.run_results.run_results_v3 import RunResultsV3
from collate_dbt_artifacts_parser.parsers.run_results.run_results_v4 import RunResultsV4
from collate_dbt_artifacts_parser.parsers.run_results.run_results_v5 import RunResultsV5
from collate_dbt_artifacts_parser.parsers.run_results.run_results_v6 import RunResultsV6
from collate_dbt_artifacts_parser.parsers.sources.sources_v1 import SourcesV1
from collate_dbt_artifacts_parser.parsers.sources.sources_v2 import SourcesV2
from collate_dbt_artifacts_parser.parsers.sources.sources_v3 import SourcesV3


@dataclass
class ArtifactType:
    dbt_schema_version: str
    model_class: Type[BaseParserModel]


class ArtifactTypes(Enum):
    """Dbt artifacts types"""

    # Catalog
    CATALOG_V1 = ArtifactType(
        "https://schemas.getdbt.com/dbt/catalog/v1.json", CatalogV1
    )
    # Manifest
    MANIFEST_V1 = ArtifactType(
        "https://schemas.getdbt.com/dbt/manifest/v1.json", ManifestV1
    )
    MANIFEST_V2 = ArtifactType(
        "https://schemas.getdbt.com/dbt/manifest/v2.json", ManifestV2
    )
    MANIFEST_V3 = ArtifactType(
        "https://schemas.getdbt.com/dbt/manifest/v3.json", ManifestV3
    )
    MANIFEST_V4 = ArtifactType(
        "https://schemas.getdbt.com/dbt/manifest/v4.json", ManifestV4
    )
    MANIFEST_V5 = ArtifactType(
        "https://schemas.getdbt.com/dbt/manifest/v5.json", ManifestV5
    )
    MANIFEST_V6 = ArtifactType(
        "https://schemas.getdbt.com/dbt/manifest/v6.json", ManifestV6
    )
    MANIFEST_V7 = ArtifactType(
        "https://schemas.getdbt.com/dbt/manifest/v7.json", ManifestV7
    )
    MANIFEST_V8 = ArtifactType(
        "https://schemas.getdbt.com/dbt/manifest/v8.json", ManifestV8
    )
    MANIFEST_V9 = ArtifactType(
        "https://schemas.getdbt.com/dbt/manifest/v9.json", ManifestV9
    )
    MANIFEST_V10 = ArtifactType(
        "https://schemas.getdbt.com/dbt/manifest/v10.json", ManifestV10
    )
    MANIFEST_V11 = ArtifactType(
        "https://schemas.getdbt.com/dbt/manifest/v11.json", ManifestV11
    )
    MANIFEST_V12 = ArtifactType(
        "https://schemas.getdbt.com/dbt/manifest/v12.json", ManifestV12
    )
    # RunResults
    RUN_RESULTS_V1 = ArtifactType(
        "https://schemas.getdbt.com/dbt/run-results/v1.json", RunResultsV1
    )
    RUN_RESULTS_V2 = ArtifactType(
        "https://schemas.getdbt.com/dbt/run-results/v2.json", RunResultsV2
    )
    RUN_RESULTS_V3 = ArtifactType(
        "https://schemas.getdbt.com/dbt/run-results/v3.json", RunResultsV3
    )
    RUN_RESULTS_V4 = ArtifactType(
        "https://schemas.getdbt.com/dbt/run-results/v4.json", RunResultsV4
    )
    RUN_RESULTS_V5 = ArtifactType(
        "https://schemas.getdbt.com/dbt/run-results/v5.json", RunResultsV5
    )
    RUN_RESULTS_V6 = ArtifactType(
        "https://schemas.getdbt.com/dbt/run-results/v6.json", RunResultsV6
    )
    # Sources
    SOURCES_V1 = ArtifactType(
        "https://schemas.getdbt.com/dbt/sources/v1.json", SourcesV1
    )
    SOURCES_V2 = ArtifactType(
        "https://schemas.getdbt.com/dbt/sources/v2.json", SourcesV2
    )
    SOURCES_V3 = ArtifactType(
        "https://schemas.getdbt.com/dbt/sources/v3.json", SourcesV3
    )
