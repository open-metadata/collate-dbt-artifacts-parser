# generated by datamodel-codegen:
#   filename:  sources_cloud_v1.json

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import ConfigDict, Field

from collate_dbt_artifacts_parser.parsers.base import BaseParserModel


class Metadata(BaseParserModel):
    model_config = ConfigDict(extra='allow',)
    dbt_schema_version: Optional[str] = None
    dbt_version: Optional[str] = '1.10.0a1'
    generated_at: Optional[str] = None
    invocation_id: Optional[str] = None
    env: Optional[Dict[str, str]] = None


class Status(Enum):
    runtime_error = 'runtime error'


class Result(BaseParserModel):
    model_config = ConfigDict(extra='allow',)
    unique_id: str
    error: Optional[Union[str, int]] = None
    status: Status


class Status1(Enum):
    pass_ = 'pass'
    warn = 'warn'
    error = 'error'
    runtime_error = 'runtime error'


class PeriodEnum(Enum):
    minute = 'minute'
    hour = 'hour'
    day = 'day'


class WarnAfterItem(BaseParserModel):
    model_config = ConfigDict(extra='allow',)
    count: Optional[int] = None
    period: Optional[PeriodEnum] = None


class ErrorAfterItem(BaseParserModel):
    model_config = ConfigDict(extra='allow',)
    count: Optional[int] = None
    period: Optional[PeriodEnum] = None


class Criteria(BaseParserModel):
    model_config = ConfigDict(extra='allow',)
    warn_after: Optional[WarnAfterItem] = None
    error_after: Optional[ErrorAfterItem] = None
    filter: Optional[str] = None


class TimingItem(BaseParserModel):
    model_config = ConfigDict(extra='allow',)
    name: str
    started_at: Optional[str] = None
    completed_at: Optional[str] = None


class Result1(BaseParserModel):
    model_config = ConfigDict(extra='allow',)
    unique_id: str
    max_loaded_at: str
    snapshotted_at: str
    max_loaded_at_time_ago_in_s: float
    status: Status1
    criteria: Criteria = Field(..., title='FreshnessThreshold')
    adapter_response: Dict[str, Any]
    timing: List[TimingItem]
    thread_id: str
    execution_time: float


class SourcesCLOUDV1(BaseParserModel):
    model_config = ConfigDict(extra='allow',)
    metadata: Metadata = Field(..., title='FreshnessMetadata')
    results: List[Union[Result, Result1]]
    elapsed_time: float
