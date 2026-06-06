import datetime

from . import common_pb2 as _common_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StartTaskRequest(_message.Message):
    __slots__ = ("base", "task_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    task_id: str
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., task_id: _Optional[str] = ...) -> None: ...

class StopTaskRequest(_message.Message):
    __slots__ = ("base", "task_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    task_id: str
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., task_id: _Optional[str] = ...) -> None: ...

class GetMissionRequest(_message.Message):
    __slots__ = ("base", "mission_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    mission_id: str
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., mission_id: _Optional[str] = ...) -> None: ...

class CreateMissionRequest(_message.Message):
    __slots__ = ("base", "mission_dto")
    BASE_FIELD_NUMBER: _ClassVar[int]
    MISSION_DTO_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    mission_dto: _common_pb2.MissionProtoDTO
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., mission_dto: _Optional[_Union[_common_pb2.MissionProtoDTO, _Mapping]] = ...) -> None: ...

class UpdateMissionRequest(_message.Message):
    __slots__ = ("base", "mission_dto", "mission_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    MISSION_DTO_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    mission_dto: _common_pb2.MissionProtoDTO
    mission_id: str
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., mission_dto: _Optional[_Union[_common_pb2.MissionProtoDTO, _Mapping]] = ..., mission_id: _Optional[str] = ...) -> None: ...

class DeleteMissionRequest(_message.Message):
    __slots__ = ("base", "mission_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    mission_id: str
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., mission_id: _Optional[str] = ...) -> None: ...

class GetTaskRequest(_message.Message):
    __slots__ = ("base", "task_id", "flight_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    FLIGHT_ID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    task_id: str
    flight_id: str
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., task_id: _Optional[str] = ..., flight_id: _Optional[str] = ...) -> None: ...

class CreateTaskRequest(_message.Message):
    __slots__ = ("base", "task_dto")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TASK_DTO_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    task_dto: _common_pb2.TaskProtoDTO
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., task_dto: _Optional[_Union[_common_pb2.TaskProtoDTO, _Mapping]] = ...) -> None: ...

class UpdateTaskRequest(_message.Message):
    __slots__ = ("base", "task_id", "task_dto")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_DTO_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    task_id: str
    task_dto: _common_pb2.TaskProtoDTO
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., task_id: _Optional[str] = ..., task_dto: _Optional[_Union[_common_pb2.TaskProtoDTO, _Mapping]] = ...) -> None: ...

class DeleteTaskRequest(_message.Message):
    __slots__ = ("base", "task_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    task_id: str
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., task_id: _Optional[str] = ...) -> None: ...

class CreateSchedulerRequest(_message.Message):
    __slots__ = ("base", "scheduler_dto")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULER_DTO_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    scheduler_dto: _common_pb2.SchedulerProtoDTO
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., scheduler_dto: _Optional[_Union[_common_pb2.SchedulerProtoDTO, _Mapping]] = ...) -> None: ...

class CreateSchedulersRequest(_message.Message):
    __slots__ = ("base", "scheduler_dtos")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULER_DTOS_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    scheduler_dtos: _containers.RepeatedCompositeFieldContainer[_common_pb2.SchedulerProtoDTO]
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., scheduler_dtos: _Optional[_Iterable[_Union[_common_pb2.SchedulerProtoDTO, _Mapping]]] = ...) -> None: ...

class UpdateSchedulerRequest(_message.Message):
    __slots__ = ("base", "scheduler_dto", "scheduler_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULER_DTO_FIELD_NUMBER: _ClassVar[int]
    SCHEDULER_ID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    scheduler_dto: _common_pb2.SchedulerProtoDTO
    scheduler_id: str
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., scheduler_dto: _Optional[_Union[_common_pb2.SchedulerProtoDTO, _Mapping]] = ..., scheduler_id: _Optional[str] = ...) -> None: ...

class DeleteSchedulerRequest(_message.Message):
    __slots__ = ("base", "scheduler_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULER_ID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    scheduler_id: str
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., scheduler_id: _Optional[str] = ...) -> None: ...

class DeleteSchedulersRequest(_message.Message):
    __slots__ = ("base", "scheduler_ids")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULER_IDS_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    scheduler_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., scheduler_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class DeleteSchedulersByTaskRequest(_message.Message):
    __slots__ = ("base", "task_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    task_id: str
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., task_id: _Optional[str] = ...) -> None: ...

class GetSchedulerRequest(_message.Message):
    __slots__ = ("base", "scheduler_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULER_ID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    scheduler_id: str
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., scheduler_id: _Optional[str] = ...) -> None: ...

class MissionResponse(_message.Message):
    __slots__ = ("has_errors", "tid", "mission_id", "timestamp", "empty", "error", "progress", "mission_dto")
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TID_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    EMPTY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    MISSION_DTO_FIELD_NUMBER: _ClassVar[int]
    has_errors: bool
    tid: str
    mission_id: str
    timestamp: _timestamp_pb2.Timestamp
    empty: _empty_pb2.Empty
    error: _common_pb2.GlobalErrorMessage
    progress: _common_pb2.CommandProgress
    mission_dto: _common_pb2.MissionProtoDTO
    def __init__(self, has_errors: bool = ..., tid: _Optional[str] = ..., mission_id: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., empty: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., error: _Optional[_Union[_common_pb2.GlobalErrorMessage, _Mapping]] = ..., progress: _Optional[_Union[_common_pb2.CommandProgress, _Mapping]] = ..., mission_dto: _Optional[_Union[_common_pb2.MissionProtoDTO, _Mapping]] = ...) -> None: ...

class TaskResponse(_message.Message):
    __slots__ = ("has_errors", "tid", "task_id", "timestamp", "empty", "error", "progress", "task_dto")
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    EMPTY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    TASK_DTO_FIELD_NUMBER: _ClassVar[int]
    has_errors: bool
    tid: str
    task_id: str
    timestamp: _timestamp_pb2.Timestamp
    empty: _empty_pb2.Empty
    error: _common_pb2.GlobalErrorMessage
    progress: _common_pb2.CommandProgress
    task_dto: _common_pb2.TaskProtoDTO
    def __init__(self, has_errors: bool = ..., tid: _Optional[str] = ..., task_id: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., empty: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., error: _Optional[_Union[_common_pb2.GlobalErrorMessage, _Mapping]] = ..., progress: _Optional[_Union[_common_pb2.CommandProgress, _Mapping]] = ..., task_dto: _Optional[_Union[_common_pb2.TaskProtoDTO, _Mapping]] = ...) -> None: ...

class SchedulerResponse(_message.Message):
    __slots__ = ("has_errors", "tid", "scheduler_id", "timestamp", "empty", "error", "progress", "scheduler_dto", "scheduler_dto_list")
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULER_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    EMPTY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULER_DTO_FIELD_NUMBER: _ClassVar[int]
    SCHEDULER_DTO_LIST_FIELD_NUMBER: _ClassVar[int]
    has_errors: bool
    tid: str
    scheduler_id: str
    timestamp: _timestamp_pb2.Timestamp
    empty: _empty_pb2.Empty
    error: _common_pb2.GlobalErrorMessage
    progress: _common_pb2.CommandProgress
    scheduler_dto: _common_pb2.SchedulerProtoDTO
    scheduler_dto_list: _common_pb2.SchedulerProtoDTOList
    def __init__(self, has_errors: bool = ..., tid: _Optional[str] = ..., scheduler_id: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., empty: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., error: _Optional[_Union[_common_pb2.GlobalErrorMessage, _Mapping]] = ..., progress: _Optional[_Union[_common_pb2.CommandProgress, _Mapping]] = ..., scheduler_dto: _Optional[_Union[_common_pb2.SchedulerProtoDTO, _Mapping]] = ..., scheduler_dto_list: _Optional[_Union[_common_pb2.SchedulerProtoDTOList, _Mapping]] = ...) -> None: ...

class EvaluateDetectionRequest(_message.Message):
    __slots__ = ("base", "detection_id", "asset_sn", "object_type", "confidence", "detection_latitude", "detection_longitude", "detection_altitude", "mission_id", "organization_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    DETECTION_ID_FIELD_NUMBER: _ClassVar[int]
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    DETECTION_LATITUDE_FIELD_NUMBER: _ClassVar[int]
    DETECTION_LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    DETECTION_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    detection_id: str
    asset_sn: str
    object_type: str
    confidence: float
    detection_latitude: float
    detection_longitude: float
    detection_altitude: float
    mission_id: str
    organization_id: str
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., detection_id: _Optional[str] = ..., asset_sn: _Optional[str] = ..., object_type: _Optional[str] = ..., confidence: _Optional[float] = ..., detection_latitude: _Optional[float] = ..., detection_longitude: _Optional[float] = ..., detection_altitude: _Optional[float] = ..., mission_id: _Optional[str] = ..., organization_id: _Optional[str] = ...) -> None: ...

class DecisionResultProto(_message.Message):
    __slots__ = ("decision_id", "detection_id", "selected_asset_sn", "strategy_used", "status", "considered_asset_sns", "rejection_reasons", "decided_at")
    class RejectionReasonsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    DECISION_ID_FIELD_NUMBER: _ClassVar[int]
    DETECTION_ID_FIELD_NUMBER: _ClassVar[int]
    SELECTED_ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    STRATEGY_USED_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CONSIDERED_ASSET_SNS_FIELD_NUMBER: _ClassVar[int]
    REJECTION_REASONS_FIELD_NUMBER: _ClassVar[int]
    DECIDED_AT_FIELD_NUMBER: _ClassVar[int]
    decision_id: str
    detection_id: str
    selected_asset_sn: str
    strategy_used: str
    status: str
    considered_asset_sns: _containers.RepeatedScalarFieldContainer[str]
    rejection_reasons: _containers.ScalarMap[str, str]
    decided_at: _timestamp_pb2.Timestamp
    def __init__(self, decision_id: _Optional[str] = ..., detection_id: _Optional[str] = ..., selected_asset_sn: _Optional[str] = ..., strategy_used: _Optional[str] = ..., status: _Optional[str] = ..., considered_asset_sns: _Optional[_Iterable[str]] = ..., rejection_reasons: _Optional[_Mapping[str, str]] = ..., decided_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DecisionResponse(_message.Message):
    __slots__ = ("has_errors", "tid", "timestamp", "error", "decision_result")
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DECISION_RESULT_FIELD_NUMBER: _ClassVar[int]
    has_errors: bool
    tid: str
    timestamp: _timestamp_pb2.Timestamp
    error: _common_pb2.GlobalErrorMessage
    decision_result: DecisionResultProto
    def __init__(self, has_errors: bool = ..., tid: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_common_pb2.GlobalErrorMessage, _Mapping]] = ..., decision_result: _Optional[_Union[DecisionResultProto, _Mapping]] = ...) -> None: ...
