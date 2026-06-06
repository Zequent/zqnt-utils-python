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

class NotificationEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NOTIFICATION_EVENT_UNSPECIFIED: _ClassVar[NotificationEventType]
    NOTIFICATION_EVENT_ASSET_STATUS: _ClassVar[NotificationEventType]
    NOTIFICATION_EVENT_TASK: _ClassVar[NotificationEventType]
    NOTIFICATION_EVENT_OPERATION: _ClassVar[NotificationEventType]
NOTIFICATION_EVENT_UNSPECIFIED: NotificationEventType
NOTIFICATION_EVENT_ASSET_STATUS: NotificationEventType
NOTIFICATION_EVENT_TASK: NotificationEventType
NOTIFICATION_EVENT_OPERATION: NotificationEventType

class LiveDataResponse(_message.Message):
    __slots__ = ("tid", "timestamp", "has_errors", "sn", "asset_id", "response_message", "asset_telemetry", "sub_asset_telemetry", "empty", "error", "live_stream_start_response")
    TID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    SN_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ASSET_TELEMETRY_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSET_TELEMETRY_FIELD_NUMBER: _ClassVar[int]
    EMPTY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    LIVE_STREAM_START_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    tid: str
    timestamp: _timestamp_pb2.Timestamp
    has_errors: bool
    sn: str
    asset_id: str
    response_message: str
    asset_telemetry: AssetTelemetry
    sub_asset_telemetry: SubAssetTelemetry
    empty: _empty_pb2.Empty
    error: _common_pb2.GlobalErrorMessage
    live_stream_start_response: _common_pb2.LiveStreamStartResponse
    def __init__(self, tid: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., has_errors: bool = ..., sn: _Optional[str] = ..., asset_id: _Optional[str] = ..., response_message: _Optional[str] = ..., asset_telemetry: _Optional[_Union[AssetTelemetry, _Mapping]] = ..., sub_asset_telemetry: _Optional[_Union[SubAssetTelemetry, _Mapping]] = ..., empty: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., error: _Optional[_Union[_common_pb2.GlobalErrorMessage, _Mapping]] = ..., live_stream_start_response: _Optional[_Union[_common_pb2.LiveStreamStartResponse, _Mapping]] = ...) -> None: ...

class LiveDataStreamTelemetryRequest(_message.Message):
    __slots__ = ("base", "frequency_ms", "duration", "command")
    BASE_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_MS_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    frequency_ms: int
    duration: int
    command: _common_pb2.LiveDataServiceCommand
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., frequency_ms: _Optional[int] = ..., duration: _Optional[int] = ..., command: _Optional[_Union[_common_pb2.LiveDataServiceCommand, str]] = ...) -> None: ...

class ProduceTelemetryRequest(_message.Message):
    __slots__ = ("base", "type", "asset_telemetry", "sub_asset_telemetry", "live_stream_state", "error")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ASSET_TELEMETRY_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSET_TELEMETRY_FIELD_NUMBER: _ClassVar[int]
    LIVE_STREAM_STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    type: _common_pb2.LiveDataType
    asset_telemetry: AssetTelemetry
    sub_asset_telemetry: SubAssetTelemetry
    live_stream_state: _common_pb2.LiveStreamState
    error: _common_pb2.GlobalErrorMessage
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., type: _Optional[_Union[_common_pb2.LiveDataType, str]] = ..., asset_telemetry: _Optional[_Union[AssetTelemetry, _Mapping]] = ..., sub_asset_telemetry: _Optional[_Union[SubAssetTelemetry, _Mapping]] = ..., live_stream_state: _Optional[_Union[_common_pb2.LiveStreamState, _Mapping]] = ..., error: _Optional[_Union[_common_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...

class LiveDataTelemetryResponse(_message.Message):
    __slots__ = ("tid", "timestamp", "has_errors", "sn", "asset_id", "asset_telemetry", "sub_asset_telemetry", "error", "live_stream_state")
    TID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    SN_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    ASSET_TELEMETRY_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSET_TELEMETRY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    LIVE_STREAM_STATE_FIELD_NUMBER: _ClassVar[int]
    tid: str
    timestamp: _timestamp_pb2.Timestamp
    has_errors: bool
    sn: str
    asset_id: str
    asset_telemetry: AssetTelemetry
    sub_asset_telemetry: SubAssetTelemetry
    error: _common_pb2.GlobalErrorMessage
    live_stream_state: _common_pb2.LiveStreamState
    def __init__(self, tid: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., has_errors: bool = ..., sn: _Optional[str] = ..., asset_id: _Optional[str] = ..., asset_telemetry: _Optional[_Union[AssetTelemetry, _Mapping]] = ..., sub_asset_telemetry: _Optional[_Union[SubAssetTelemetry, _Mapping]] = ..., error: _Optional[_Union[_common_pb2.GlobalErrorMessage, _Mapping]] = ..., live_stream_state: _Optional[_Union[_common_pb2.LiveStreamState, _Mapping]] = ...) -> None: ...

class LiveStreamStartRequest(_message.Message):
    __slots__ = ("video_id", "stream_server", "stream_type", "asset_type")
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    STREAM_SERVER_FIELD_NUMBER: _ClassVar[int]
    STREAM_TYPE_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    video_id: str
    stream_server: str
    stream_type: _common_pb2.LiveStreamTypeEnum
    asset_type: _common_pb2.AssetTypeEnum
    def __init__(self, video_id: _Optional[str] = ..., stream_server: _Optional[str] = ..., stream_type: _Optional[_Union[_common_pb2.LiveStreamTypeEnum, str]] = ..., asset_type: _Optional[_Union[_common_pb2.AssetTypeEnum, str]] = ...) -> None: ...

class LiveStreamStopRequest(_message.Message):
    __slots__ = ("video_id",)
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    video_id: str
    def __init__(self, video_id: _Optional[str] = ...) -> None: ...

class LiveDataStartLiveStreamRequest(_message.Message):
    __slots__ = ("base", "request")
    BASE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    request: LiveStreamStartRequest
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., request: _Optional[_Union[LiveStreamStartRequest, _Mapping]] = ...) -> None: ...

class LiveDataStopLiveStreamRequest(_message.Message):
    __slots__ = ("base", "request")
    BASE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    request: LiveStreamStopRequest
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., request: _Optional[_Union[LiveStreamStopRequest, _Mapping]] = ...) -> None: ...

class LiveDataChangeLensRequest(_message.Message):
    __slots__ = ("base", "request")
    BASE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    request: _common_pb2.ChangeCameraLensRequest
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., request: _Optional[_Union[_common_pb2.ChangeCameraLensRequest, _Mapping]] = ...) -> None: ...

class LiveDataChangeZoomRequest(_message.Message):
    __slots__ = ("base", "request")
    BASE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    request: _common_pb2.ChangeCameraZoomRequest
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., request: _Optional[_Union[_common_pb2.ChangeCameraZoomRequest, _Mapping]] = ...) -> None: ...

class LiveDataStartRecordingRequest(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ...) -> None: ...

class LiveDataStopRecordingRequest(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ...) -> None: ...

class LiveDataCapturePhotoRequest(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ...) -> None: ...

class LiveDataStreamDetectionsRequest(_message.Message):
    __slots__ = ("base", "stream_url")
    BASE_FIELD_NUMBER: _ClassVar[int]
    STREAM_URL_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    stream_url: str
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., stream_url: _Optional[str] = ...) -> None: ...

class LiveDataDetectionResponse(_message.Message):
    __slots__ = ("tid", "timestamp", "has_errors", "sn", "asset_id", "detections", "error")
    TID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    SN_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    DETECTIONS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    tid: str
    timestamp: _timestamp_pb2.Timestamp
    has_errors: bool
    sn: str
    asset_id: str
    detections: _common_pb2.DetectionBatch
    error: _common_pb2.GlobalErrorMessage
    def __init__(self, tid: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., has_errors: bool = ..., sn: _Optional[str] = ..., asset_id: _Optional[str] = ..., detections: _Optional[_Union[_common_pb2.DetectionBatch, _Mapping]] = ..., error: _Optional[_Union[_common_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...

class AssetTelemetry(_message.Message):
    __slots__ = ("id", "timestamp", "latitude", "longitude", "absolute_altitude", "relative_altitude", "environment_temp", "inside_temp", "humidity", "mode", "rainfall", "sub_asset_information", "sub_asset_at_home", "sub_asset_charging", "sub_asset_percentage", "heading", "debug_mode_open", "has_active_manual_control_session", "cover_state", "working_voltage", "working_current", "supply_voltage", "wind_speed", "position_valid", "network_information", "air_conditioner", "manual_control_state", "position_state")
    class PositionState(_message.Message):
        __slots__ = ("gps_number", "rtk_number", "quality")
        GPS_NUMBER_FIELD_NUMBER: _ClassVar[int]
        RTK_NUMBER_FIELD_NUMBER: _ClassVar[int]
        QUALITY_FIELD_NUMBER: _ClassVar[int]
        gps_number: int
        rtk_number: int
        quality: int
        def __init__(self, gps_number: _Optional[int] = ..., rtk_number: _Optional[int] = ..., quality: _Optional[int] = ...) -> None: ...
    class AssetAirConditioner(_message.Message):
        __slots__ = ("state", "switch_time")
        STATE_FIELD_NUMBER: _ClassVar[int]
        SWITCH_TIME_FIELD_NUMBER: _ClassVar[int]
        state: _common_pb2.AssetAirConditionerStateEnum
        switch_time: int
        def __init__(self, state: _Optional[_Union[_common_pb2.AssetAirConditionerStateEnum, str]] = ..., switch_time: _Optional[int] = ...) -> None: ...
    class AssetNetworkInformation(_message.Message):
        __slots__ = ("type", "rate", "quality")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        RATE_FIELD_NUMBER: _ClassVar[int]
        QUALITY_FIELD_NUMBER: _ClassVar[int]
        type: _common_pb2.NetworkTypeEnum
        rate: float
        quality: _common_pb2.NetworkStateQualityEnum
        def __init__(self, type: _Optional[_Union[_common_pb2.NetworkTypeEnum, str]] = ..., rate: _Optional[float] = ..., quality: _Optional[_Union[_common_pb2.NetworkStateQualityEnum, str]] = ...) -> None: ...
    class AssetSubAssetInformation(_message.Message):
        __slots__ = ("sn", "model", "paired", "online")
        SN_FIELD_NUMBER: _ClassVar[int]
        MODEL_FIELD_NUMBER: _ClassVar[int]
        PAIRED_FIELD_NUMBER: _ClassVar[int]
        ONLINE_FIELD_NUMBER: _ClassVar[int]
        sn: str
        model: str
        paired: bool
        online: bool
        def __init__(self, sn: _Optional[str] = ..., model: _Optional[str] = ..., paired: bool = ..., online: bool = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    ABSOLUTE_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_TEMP_FIELD_NUMBER: _ClassVar[int]
    INSIDE_TEMP_FIELD_NUMBER: _ClassVar[int]
    HUMIDITY_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    RAINFALL_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSET_INFORMATION_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSET_AT_HOME_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSET_CHARGING_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSET_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    HEADING_FIELD_NUMBER: _ClassVar[int]
    DEBUG_MODE_OPEN_FIELD_NUMBER: _ClassVar[int]
    HAS_ACTIVE_MANUAL_CONTROL_SESSION_FIELD_NUMBER: _ClassVar[int]
    COVER_STATE_FIELD_NUMBER: _ClassVar[int]
    WORKING_VOLTAGE_FIELD_NUMBER: _ClassVar[int]
    WORKING_CURRENT_FIELD_NUMBER: _ClassVar[int]
    SUPPLY_VOLTAGE_FIELD_NUMBER: _ClassVar[int]
    WIND_SPEED_FIELD_NUMBER: _ClassVar[int]
    POSITION_VALID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_INFORMATION_FIELD_NUMBER: _ClassVar[int]
    AIR_CONDITIONER_FIELD_NUMBER: _ClassVar[int]
    MANUAL_CONTROL_STATE_FIELD_NUMBER: _ClassVar[int]
    POSITION_STATE_FIELD_NUMBER: _ClassVar[int]
    id: str
    timestamp: _timestamp_pb2.Timestamp
    latitude: float
    longitude: float
    absolute_altitude: float
    relative_altitude: float
    environment_temp: float
    inside_temp: float
    humidity: float
    mode: _common_pb2.AssetMode
    rainfall: _common_pb2.RainfallEnum
    sub_asset_information: AssetTelemetry.AssetSubAssetInformation
    sub_asset_at_home: bool
    sub_asset_charging: bool
    sub_asset_percentage: float
    heading: float
    debug_mode_open: bool
    has_active_manual_control_session: bool
    cover_state: _common_pb2.AssetCoverStateEnum
    working_voltage: int
    working_current: int
    supply_voltage: int
    wind_speed: float
    position_valid: bool
    network_information: AssetTelemetry.AssetNetworkInformation
    air_conditioner: AssetTelemetry.AssetAirConditioner
    manual_control_state: _common_pb2.ManualControlStateEnum
    position_state: AssetTelemetry.PositionState
    def __init__(self, id: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., absolute_altitude: _Optional[float] = ..., relative_altitude: _Optional[float] = ..., environment_temp: _Optional[float] = ..., inside_temp: _Optional[float] = ..., humidity: _Optional[float] = ..., mode: _Optional[_Union[_common_pb2.AssetMode, str]] = ..., rainfall: _Optional[_Union[_common_pb2.RainfallEnum, str]] = ..., sub_asset_information: _Optional[_Union[AssetTelemetry.AssetSubAssetInformation, _Mapping]] = ..., sub_asset_at_home: bool = ..., sub_asset_charging: bool = ..., sub_asset_percentage: _Optional[float] = ..., heading: _Optional[float] = ..., debug_mode_open: bool = ..., has_active_manual_control_session: bool = ..., cover_state: _Optional[_Union[_common_pb2.AssetCoverStateEnum, str]] = ..., working_voltage: _Optional[int] = ..., working_current: _Optional[int] = ..., supply_voltage: _Optional[int] = ..., wind_speed: _Optional[float] = ..., position_valid: bool = ..., network_information: _Optional[_Union[AssetTelemetry.AssetNetworkInformation, _Mapping]] = ..., air_conditioner: _Optional[_Union[AssetTelemetry.AssetAirConditioner, _Mapping]] = ..., manual_control_state: _Optional[_Union[_common_pb2.ManualControlStateEnum, str]] = ..., position_state: _Optional[_Union[AssetTelemetry.PositionState, _Mapping]] = ...) -> None: ...

class SubAssetTelemetry(_message.Message):
    __slots__ = ("id", "timestamp", "latitude", "longitude", "absolute_altitude", "relative_altitude", "horizontal_speed", "vertical_speed", "wind_speed", "wind_direction", "heading", "gear", "payload_telemetry", "battery_information", "height_limit", "home_distance", "total_movement_distance", "total_movement_time", "mode", "country")
    class SubAssetBatteryInformation(_message.Message):
        __slots__ = ("percentage", "remaining_time", "return_to_home_power")
        PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        REMAINING_TIME_FIELD_NUMBER: _ClassVar[int]
        RETURN_TO_HOME_POWER_FIELD_NUMBER: _ClassVar[int]
        percentage: str
        remaining_time: int
        return_to_home_power: str
        def __init__(self, percentage: _Optional[str] = ..., remaining_time: _Optional[int] = ..., return_to_home_power: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    ABSOLUTE_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    HORIZONTAL_SPEED_FIELD_NUMBER: _ClassVar[int]
    VERTICAL_SPEED_FIELD_NUMBER: _ClassVar[int]
    WIND_SPEED_FIELD_NUMBER: _ClassVar[int]
    WIND_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    HEADING_FIELD_NUMBER: _ClassVar[int]
    GEAR_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_TELEMETRY_FIELD_NUMBER: _ClassVar[int]
    BATTERY_INFORMATION_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    HOME_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MOVEMENT_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MOVEMENT_TIME_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    id: str
    timestamp: _timestamp_pb2.Timestamp
    latitude: float
    longitude: float
    absolute_altitude: float
    relative_altitude: float
    horizontal_speed: float
    vertical_speed: float
    wind_speed: float
    wind_direction: str
    heading: float
    gear: int
    payload_telemetry: PayloadTelemetry
    battery_information: SubAssetTelemetry.SubAssetBatteryInformation
    height_limit: int
    home_distance: float
    total_movement_distance: float
    total_movement_time: float
    mode: _common_pb2.SubAssetMode
    country: str
    def __init__(self, id: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., absolute_altitude: _Optional[float] = ..., relative_altitude: _Optional[float] = ..., horizontal_speed: _Optional[float] = ..., vertical_speed: _Optional[float] = ..., wind_speed: _Optional[float] = ..., wind_direction: _Optional[str] = ..., heading: _Optional[float] = ..., gear: _Optional[int] = ..., payload_telemetry: _Optional[_Union[PayloadTelemetry, _Mapping]] = ..., battery_information: _Optional[_Union[SubAssetTelemetry.SubAssetBatteryInformation, _Mapping]] = ..., height_limit: _Optional[int] = ..., home_distance: _Optional[float] = ..., total_movement_distance: _Optional[float] = ..., total_movement_time: _Optional[float] = ..., mode: _Optional[_Union[_common_pb2.SubAssetMode, str]] = ..., country: _Optional[str] = ...) -> None: ...

class PayloadTelemetry(_message.Message):
    __slots__ = ("id", "timestamp", "camera_data", "range_finder_data", "sensor_data", "name")
    class CameraData(_message.Message):
        __slots__ = ("current_lens", "gimbal_pitch", "gimbal_yaw", "zoom_factor", "gimbal_roll")
        CURRENT_LENS_FIELD_NUMBER: _ClassVar[int]
        GIMBAL_PITCH_FIELD_NUMBER: _ClassVar[int]
        GIMBAL_YAW_FIELD_NUMBER: _ClassVar[int]
        ZOOM_FACTOR_FIELD_NUMBER: _ClassVar[int]
        GIMBAL_ROLL_FIELD_NUMBER: _ClassVar[int]
        current_lens: str
        gimbal_pitch: float
        gimbal_yaw: float
        zoom_factor: float
        gimbal_roll: float
        def __init__(self, current_lens: _Optional[str] = ..., gimbal_pitch: _Optional[float] = ..., gimbal_yaw: _Optional[float] = ..., zoom_factor: _Optional[float] = ..., gimbal_roll: _Optional[float] = ...) -> None: ...
    class RangeFinderData(_message.Message):
        __slots__ = ("target_latitude", "target_longitude", "target_distance", "target_altitude")
        TARGET_LATITUDE_FIELD_NUMBER: _ClassVar[int]
        TARGET_LONGITUDE_FIELD_NUMBER: _ClassVar[int]
        TARGET_DISTANCE_FIELD_NUMBER: _ClassVar[int]
        TARGET_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
        target_latitude: float
        target_longitude: float
        target_distance: float
        target_altitude: float
        def __init__(self, target_latitude: _Optional[float] = ..., target_longitude: _Optional[float] = ..., target_distance: _Optional[float] = ..., target_altitude: _Optional[float] = ...) -> None: ...
    class SensorData(_message.Message):
        __slots__ = ("target_temperature",)
        TARGET_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
        target_temperature: float
        def __init__(self, target_temperature: _Optional[float] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CAMERA_DATA_FIELD_NUMBER: _ClassVar[int]
    RANGE_FINDER_DATA_FIELD_NUMBER: _ClassVar[int]
    SENSOR_DATA_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    timestamp: _timestamp_pb2.Timestamp
    camera_data: PayloadTelemetry.CameraData
    range_finder_data: PayloadTelemetry.RangeFinderData
    sensor_data: PayloadTelemetry.SensorData
    name: str
    def __init__(self, id: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., camera_data: _Optional[_Union[PayloadTelemetry.CameraData, _Mapping]] = ..., range_finder_data: _Optional[_Union[PayloadTelemetry.RangeFinderData, _Mapping]] = ..., sensor_data: _Optional[_Union[PayloadTelemetry.SensorData, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...

class LiveDataStreamNotificationsRequest(_message.Message):
    __slots__ = ("base", "event_types")
    BASE_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPES_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    event_types: _containers.RepeatedScalarFieldContainer[NotificationEventType]
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., event_types: _Optional[_Iterable[_Union[NotificationEventType, str]]] = ...) -> None: ...

class AssetStatusEvent(_message.Message):
    __slots__ = ("sn", "asset_id", "online")
    SN_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    ONLINE_FIELD_NUMBER: _ClassVar[int]
    sn: str
    asset_id: str
    online: bool
    def __init__(self, sn: _Optional[str] = ..., asset_id: _Optional[str] = ..., online: bool = ...) -> None: ...

class TaskEvent(_message.Message):
    __slots__ = ("task_id", "task_type", "status", "progress", "message", "external_task_type")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_TASK_TYPE_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    task_type: _common_pb2.TaskTypeProto
    status: _common_pb2.TaskStatus
    progress: float
    message: str
    external_task_type: str
    def __init__(self, task_id: _Optional[str] = ..., task_type: _Optional[_Union[_common_pb2.TaskTypeProto, str]] = ..., status: _Optional[_Union[_common_pb2.TaskStatus, str]] = ..., progress: _Optional[float] = ..., message: _Optional[str] = ..., external_task_type: _Optional[str] = ...) -> None: ...

class OperationEvent(_message.Message):
    __slots__ = ("operation_id", "mission_type", "status", "message")
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    MISSION_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    mission_type: _common_pb2.MissionType
    status: _common_pb2.MissionStatus
    message: str
    def __init__(self, operation_id: _Optional[str] = ..., mission_type: _Optional[_Union[_common_pb2.MissionType, str]] = ..., status: _Optional[_Union[_common_pb2.MissionStatus, str]] = ..., message: _Optional[str] = ...) -> None: ...

class LiveDataNotificationResponse(_message.Message):
    __slots__ = ("tid", "timestamp", "has_errors", "sn", "asset_id", "asset_status", "task_event", "operation_event", "error")
    TID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    SN_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    ASSET_STATUS_FIELD_NUMBER: _ClassVar[int]
    TASK_EVENT_FIELD_NUMBER: _ClassVar[int]
    OPERATION_EVENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    tid: str
    timestamp: _timestamp_pb2.Timestamp
    has_errors: bool
    sn: str
    asset_id: str
    asset_status: AssetStatusEvent
    task_event: TaskEvent
    operation_event: OperationEvent
    error: _common_pb2.GlobalErrorMessage
    def __init__(self, tid: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., has_errors: bool = ..., sn: _Optional[str] = ..., asset_id: _Optional[str] = ..., asset_status: _Optional[_Union[AssetStatusEvent, _Mapping]] = ..., task_event: _Optional[_Union[TaskEvent, _Mapping]] = ..., operation_event: _Optional[_Union[OperationEvent, _Mapping]] = ..., error: _Optional[_Union[_common_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...

class ProduceNotificationRequest(_message.Message):
    __slots__ = ("base", "asset_status", "task_event", "operation_event", "error")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ASSET_STATUS_FIELD_NUMBER: _ClassVar[int]
    TASK_EVENT_FIELD_NUMBER: _ClassVar[int]
    OPERATION_EVENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    asset_status: AssetStatusEvent
    task_event: TaskEvent
    operation_event: OperationEvent
    error: _common_pb2.GlobalErrorMessage
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., asset_status: _Optional[_Union[AssetStatusEvent, _Mapping]] = ..., task_event: _Optional[_Union[TaskEvent, _Mapping]] = ..., operation_event: _Optional[_Union[OperationEvent, _Mapping]] = ..., error: _Optional[_Union[_common_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...
