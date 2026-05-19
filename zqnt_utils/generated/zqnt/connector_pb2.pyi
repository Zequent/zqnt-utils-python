import datetime

from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from . import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TelemetryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TELEMETRY_TYPE_UNSPECIFIED: _ClassVar[TelemetryType]
    TELEMETRY_TYPE_ASSET: _ClassVar[TelemetryType]
    TELEMETRY_TYPE_SUBASSET: _ClassVar[TelemetryType]
TELEMETRY_TYPE_UNSPECIFIED: TelemetryType
TELEMETRY_TYPE_ASSET: TelemetryType
TELEMETRY_TYPE_SUBASSET: TelemetryType

class ConnectorDeleteSchedulersByTaskRequest(_message.Message):
    __slots__ = ("base", "task_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    task_id: str
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., task_id: _Optional[str] = ...) -> None: ...

class ConnectorCreateSchedulersRequest(_message.Message):
    __slots__ = ("base", "schedulers")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULERS_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    schedulers: _containers.RepeatedCompositeFieldContainer[_common_pb2.SchedulerProtoDTO]
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., schedulers: _Optional[_Iterable[_Union[_common_pb2.SchedulerProtoDTO, _Mapping]]] = ...) -> None: ...

class ConnectorDeleteSchedulersRequest(_message.Message):
    __slots__ = ("base", "ids")
    BASE_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., ids: _Optional[_Iterable[str]] = ...) -> None: ...

class ConnectorGetAssetByIdRequest(_message.Message):
    __slots__ = ("base", "id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    id: str
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class ConnectorGetWaypointsByTaskId(_message.Message):
    __slots__ = ("base", "task_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    task_id: str
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., task_id: _Optional[str] = ...) -> None: ...

class ConnectorDeleteSchedulerRequest(_message.Message):
    __slots__ = ("base", "scheduler_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULER_ID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    scheduler_id: str
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., scheduler_id: _Optional[str] = ...) -> None: ...

class ConnectorUpdateSchedulerRequest(_message.Message):
    __slots__ = ("base", "scheduler_dto", "scheduler_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULER_DTO_FIELD_NUMBER: _ClassVar[int]
    SCHEDULER_ID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    scheduler_dto: _common_pb2.SchedulerProtoDTO
    scheduler_id: str
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., scheduler_dto: _Optional[_Union[_common_pb2.SchedulerProtoDTO, _Mapping]] = ..., scheduler_id: _Optional[str] = ...) -> None: ...

class ConnectorCreateSchedulerRequest(_message.Message):
    __slots__ = ("base", "scheduler_dto")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULER_DTO_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    scheduler_dto: _common_pb2.SchedulerProtoDTO
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., scheduler_dto: _Optional[_Union[_common_pb2.SchedulerProtoDTO, _Mapping]] = ...) -> None: ...

class ConnectorGetSchedulerRequest(_message.Message):
    __slots__ = ("base", "scheduler_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULER_ID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    scheduler_id: str
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., scheduler_id: _Optional[str] = ...) -> None: ...

class ConnectorDeleteTaskRequest(_message.Message):
    __slots__ = ("base", "task_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    task_id: str
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., task_id: _Optional[str] = ...) -> None: ...

class ConnectorUpdateTaskRequest(_message.Message):
    __slots__ = ("base", "task_dto", "task_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TASK_DTO_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    task_dto: _common_pb2.TaskProtoDTO
    task_id: str
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., task_dto: _Optional[_Union[_common_pb2.TaskProtoDTO, _Mapping]] = ..., task_id: _Optional[str] = ...) -> None: ...

class AssetDTOList(_message.Message):
    __slots__ = ("assets",)
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    assets: _containers.RepeatedCompositeFieldContainer[_common_pb2.AssetProtoDTO]
    def __init__(self, assets: _Optional[_Iterable[_Union[_common_pb2.AssetProtoDTO, _Mapping]]] = ...) -> None: ...

class ConnectorRegisterAssetRequest(_message.Message):
    __slots__ = ("base", "asset_dto")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ASSET_DTO_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    asset_dto: _common_pb2.AssetProtoDTO
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., asset_dto: _Optional[_Union[_common_pb2.AssetProtoDTO, _Mapping]] = ...) -> None: ...

class ConnectorUpdateAssetRequest(_message.Message):
    __slots__ = ("base", "asset_dto", "asset_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ASSET_DTO_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    asset_dto: _common_pb2.AssetProtoDTO
    asset_id: str
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., asset_dto: _Optional[_Union[_common_pb2.AssetProtoDTO, _Mapping]] = ..., asset_id: _Optional[str] = ...) -> None: ...

class ConnectorUpdateSubAssetRequest(_message.Message):
    __slots__ = ("base", "sub_asset_dto", "sub_asset_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSET_DTO_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    sub_asset_dto: _common_pb2.SubAssetProtoDTO
    sub_asset_id: str
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., sub_asset_dto: _Optional[_Union[_common_pb2.SubAssetProtoDTO, _Mapping]] = ..., sub_asset_id: _Optional[str] = ...) -> None: ...

class WaypointsListDTO(_message.Message):
    __slots__ = ("waypoints",)
    WAYPOINTS_FIELD_NUMBER: _ClassVar[int]
    waypoints: _containers.RepeatedCompositeFieldContainer[_common_pb2.WaypointProtoDTO]
    def __init__(self, waypoints: _Optional[_Iterable[_Union[_common_pb2.WaypointProtoDTO, _Mapping]]] = ...) -> None: ...

class ConnectorResponse(_message.Message):
    __slots__ = ("tid", "id", "timestamp", "has_errors", "asset_id", "response_message", "empty", "error", "asset_dto", "sub_asset_dto", "organization_dto", "mission_dto", "task_dto", "scheduler_dto", "waypoint_dto_list", "scheduler_dto_list")
    TID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    EMPTY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ASSET_DTO_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSET_DTO_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_DTO_FIELD_NUMBER: _ClassVar[int]
    MISSION_DTO_FIELD_NUMBER: _ClassVar[int]
    TASK_DTO_FIELD_NUMBER: _ClassVar[int]
    SCHEDULER_DTO_FIELD_NUMBER: _ClassVar[int]
    WAYPOINT_DTO_LIST_FIELD_NUMBER: _ClassVar[int]
    SCHEDULER_DTO_LIST_FIELD_NUMBER: _ClassVar[int]
    tid: str
    id: str
    timestamp: _timestamp_pb2.Timestamp
    has_errors: bool
    asset_id: str
    response_message: str
    empty: _empty_pb2.Empty
    error: _common_pb2.GlobalErrorMessage
    asset_dto: _common_pb2.AssetProtoDTO
    sub_asset_dto: _common_pb2.SubAssetProtoDTO
    organization_dto: _common_pb2.OrganizationProtoDTO
    mission_dto: _common_pb2.MissionProtoDTO
    task_dto: _common_pb2.TaskProtoDTO
    scheduler_dto: _common_pb2.SchedulerProtoDTO
    waypoint_dto_list: WaypointsListDTO
    scheduler_dto_list: _common_pb2.SchedulerProtoDTOList
    def __init__(self, tid: _Optional[str] = ..., id: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., has_errors: bool = ..., asset_id: _Optional[str] = ..., response_message: _Optional[str] = ..., empty: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., error: _Optional[_Union[_common_pb2.GlobalErrorMessage, _Mapping]] = ..., asset_dto: _Optional[_Union[_common_pb2.AssetProtoDTO, _Mapping]] = ..., sub_asset_dto: _Optional[_Union[_common_pb2.SubAssetProtoDTO, _Mapping]] = ..., organization_dto: _Optional[_Union[_common_pb2.OrganizationProtoDTO, _Mapping]] = ..., mission_dto: _Optional[_Union[_common_pb2.MissionProtoDTO, _Mapping]] = ..., task_dto: _Optional[_Union[_common_pb2.TaskProtoDTO, _Mapping]] = ..., scheduler_dto: _Optional[_Union[_common_pb2.SchedulerProtoDTO, _Mapping]] = ..., waypoint_dto_list: _Optional[_Union[WaypointsListDTO, _Mapping]] = ..., scheduler_dto_list: _Optional[_Union[_common_pb2.SchedulerProtoDTOList, _Mapping]] = ...) -> None: ...

class AssetMonitoringResponse(_message.Message):
    __slots__ = ("tid", "timestamp", "has_errors", "empty", "error", "asset_list")
    TID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    EMPTY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ASSET_LIST_FIELD_NUMBER: _ClassVar[int]
    tid: str
    timestamp: _timestamp_pb2.Timestamp
    has_errors: bool
    empty: _empty_pb2.Empty
    error: _common_pb2.GlobalErrorMessage
    asset_list: AssetDTOList
    def __init__(self, tid: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., has_errors: bool = ..., empty: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., error: _Optional[_Union[_common_pb2.GlobalErrorMessage, _Mapping]] = ..., asset_list: _Optional[_Union[AssetDTOList, _Mapping]] = ...) -> None: ...

class ConnectorDeRegisterAssetRequest(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ...) -> None: ...

class ConnectorAssetMonitorRequest(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ...) -> None: ...

class ConnectorGetAssetBySnRequest(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ...) -> None: ...

class ConnectorGetSubAssetBySnRequest(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ...) -> None: ...

class ConnectorGetOrganizationRequest(_message.Message):
    __slots__ = ("base", "bind_code")
    BASE_FIELD_NUMBER: _ClassVar[int]
    BIND_CODE_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    bind_code: str
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., bind_code: _Optional[str] = ...) -> None: ...

class ConnectorGetMissionRequest(_message.Message):
    __slots__ = ("base", "mission_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    mission_id: str
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., mission_id: _Optional[str] = ...) -> None: ...

class ConnectorCreateMissionRequest(_message.Message):
    __slots__ = ("base", "mission_dto")
    BASE_FIELD_NUMBER: _ClassVar[int]
    MISSION_DTO_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    mission_dto: _common_pb2.MissionProtoDTO
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., mission_dto: _Optional[_Union[_common_pb2.MissionProtoDTO, _Mapping]] = ...) -> None: ...

class ConnectorUpdateMissionRequest(_message.Message):
    __slots__ = ("base", "mission_id", "mission_dto")
    BASE_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    MISSION_DTO_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    mission_id: str
    mission_dto: _common_pb2.MissionProtoDTO
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., mission_id: _Optional[str] = ..., mission_dto: _Optional[_Union[_common_pb2.MissionProtoDTO, _Mapping]] = ...) -> None: ...

class ConnectorDeleteMissionRequest(_message.Message):
    __slots__ = ("base", "mission_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    mission_id: str
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., mission_id: _Optional[str] = ...) -> None: ...

class ConnectorGetTaskRequest(_message.Message):
    __slots__ = ("base", "task_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    task_id: str
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., task_id: _Optional[str] = ...) -> None: ...

class ConnectorCreateTaskRequest(_message.Message):
    __slots__ = ("base", "task_dto")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TASK_DTO_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    task_dto: _common_pb2.TaskProtoDTO
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., task_dto: _Optional[_Union[_common_pb2.TaskProtoDTO, _Mapping]] = ...) -> None: ...

class ConnectorStoreTelemetryRequest(_message.Message):
    __slots__ = ("base", "type", "asset_telemetry", "sub_asset_telemetry")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ASSET_TELEMETRY_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSET_TELEMETRY_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    type: TelemetryType
    asset_telemetry: AssetTelemetryProto
    sub_asset_telemetry: SubAssetTelemetryProto
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., type: _Optional[_Union[TelemetryType, str]] = ..., asset_telemetry: _Optional[_Union[AssetTelemetryProto, _Mapping]] = ..., sub_asset_telemetry: _Optional[_Union[SubAssetTelemetryProto, _Mapping]] = ...) -> None: ...

class AssetTelemetryProto(_message.Message):
    __slots__ = ("asset_id", "timestamp", "latitude", "longitude", "altitude", "relative_altitude", "heading", "temperature", "humidity", "wind_speed", "battery_percentage", "network_type", "network_quality", "operational_mode", "is_online", "source_system", "telemetry_data")
    class TelemetryDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    HEADING_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    HUMIDITY_FIELD_NUMBER: _ClassVar[int]
    WIND_SPEED_FIELD_NUMBER: _ClassVar[int]
    BATTERY_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_TYPE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_QUALITY_FIELD_NUMBER: _ClassVar[int]
    OPERATIONAL_MODE_FIELD_NUMBER: _ClassVar[int]
    IS_ONLINE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    TELEMETRY_DATA_FIELD_NUMBER: _ClassVar[int]
    asset_id: str
    timestamp: _timestamp_pb2.Timestamp
    latitude: float
    longitude: float
    altitude: float
    relative_altitude: float
    heading: float
    temperature: float
    humidity: float
    wind_speed: float
    battery_percentage: float
    network_type: str
    network_quality: int
    operational_mode: str
    is_online: bool
    source_system: str
    telemetry_data: _containers.ScalarMap[str, str]
    def __init__(self, asset_id: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., altitude: _Optional[float] = ..., relative_altitude: _Optional[float] = ..., heading: _Optional[float] = ..., temperature: _Optional[float] = ..., humidity: _Optional[float] = ..., wind_speed: _Optional[float] = ..., battery_percentage: _Optional[float] = ..., network_type: _Optional[str] = ..., network_quality: _Optional[int] = ..., operational_mode: _Optional[str] = ..., is_online: bool = ..., source_system: _Optional[str] = ..., telemetry_data: _Optional[_Mapping[str, str]] = ...) -> None: ...

class SubAssetTelemetryProto(_message.Message):
    __slots__ = ("asset_id", "timestamp", "latitude", "longitude", "altitude", "relative_altitude", "heading", "horizontal_speed", "vertical_speed", "wind_speed", "battery_percentage", "operational_mode", "is_online", "source_system", "telemetry_data")
    class TelemetryDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    HEADING_FIELD_NUMBER: _ClassVar[int]
    HORIZONTAL_SPEED_FIELD_NUMBER: _ClassVar[int]
    VERTICAL_SPEED_FIELD_NUMBER: _ClassVar[int]
    WIND_SPEED_FIELD_NUMBER: _ClassVar[int]
    BATTERY_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    OPERATIONAL_MODE_FIELD_NUMBER: _ClassVar[int]
    IS_ONLINE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    TELEMETRY_DATA_FIELD_NUMBER: _ClassVar[int]
    asset_id: str
    timestamp: _timestamp_pb2.Timestamp
    latitude: float
    longitude: float
    altitude: float
    relative_altitude: float
    heading: float
    horizontal_speed: float
    vertical_speed: float
    wind_speed: float
    battery_percentage: float
    operational_mode: str
    is_online: bool
    source_system: str
    telemetry_data: _containers.ScalarMap[str, str]
    def __init__(self, asset_id: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., altitude: _Optional[float] = ..., relative_altitude: _Optional[float] = ..., heading: _Optional[float] = ..., horizontal_speed: _Optional[float] = ..., vertical_speed: _Optional[float] = ..., wind_speed: _Optional[float] = ..., battery_percentage: _Optional[float] = ..., operational_mode: _Optional[str] = ..., is_online: bool = ..., source_system: _Optional[str] = ..., telemetry_data: _Optional[_Mapping[str, str]] = ...) -> None: ...
