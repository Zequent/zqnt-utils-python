import datetime

from . import common_pb2 as _common_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EdgePrepareTaskRequest(_message.Message):
    __slots__ = ("base", "task_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    task_id: str
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., task_id: _Optional[str] = ...) -> None: ...

class EdgeStartTaskRequest(_message.Message):
    __slots__ = ("base", "task_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    task_id: str
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., task_id: _Optional[str] = ...) -> None: ...

class EdgeStopTaskRequest(_message.Message):
    __slots__ = ("base", "task_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    task_id: str
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., task_id: _Optional[str] = ...) -> None: ...

class EdgeResponse(_message.Message):
    __slots__ = ("has_errors", "tid", "sn", "asset_id", "response_message", "timestamp", "empty", "error", "progress", "live_stream_start_response", "external_id")
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TID_FIELD_NUMBER: _ClassVar[int]
    SN_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    EMPTY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    LIVE_STREAM_START_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    has_errors: bool
    tid: str
    sn: str
    asset_id: str
    response_message: str
    timestamp: _timestamp_pb2.Timestamp
    empty: _empty_pb2.Empty
    error: _common_pb2.GlobalErrorMessage
    progress: _common_pb2.CommandProgress
    live_stream_start_response: _common_pb2.LiveStreamStartResponse
    external_id: str
    def __init__(self, has_errors: bool = ..., tid: _Optional[str] = ..., sn: _Optional[str] = ..., asset_id: _Optional[str] = ..., response_message: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., empty: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., error: _Optional[_Union[_common_pb2.GlobalErrorMessage, _Mapping]] = ..., progress: _Optional[_Union[_common_pb2.CommandProgress, _Mapping]] = ..., live_stream_start_response: _Optional[_Union[_common_pb2.LiveStreamStartResponse, _Mapping]] = ..., external_id: _Optional[str] = ...) -> None: ...

class EdgeTakeOffRequest(_message.Message):
    __slots__ = ("base", "request", "external_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    request: _common_pb2.Coordinates
    external_id: str
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., request: _Optional[_Union[_common_pb2.Coordinates, _Mapping]] = ..., external_id: _Optional[str] = ...) -> None: ...

class EdgeGoToRequest(_message.Message):
    __slots__ = ("base", "request", "external_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    request: _common_pb2.Coordinates
    external_id: str
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., request: _Optional[_Union[_common_pb2.Coordinates, _Mapping]] = ..., external_id: _Optional[str] = ...) -> None: ...

class EdgeReturnToHomeRequest(_message.Message):
    __slots__ = ("base", "request")
    BASE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    request: _common_pb2.ReturnToHomeRequest
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., request: _Optional[_Union[_common_pb2.ReturnToHomeRequest, _Mapping]] = ...) -> None: ...

class EdgeManualControlRequest(_message.Message):
    __slots__ = ("base", "request")
    BASE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    request: _common_pb2.ManualControlRequest
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., request: _Optional[_Union[_common_pb2.ManualControlRequest, _Mapping]] = ...) -> None: ...

class EdgeManualControlInputRequest(_message.Message):
    __slots__ = ("base", "request")
    BASE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    request: _common_pb2.ManualControlInput
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., request: _Optional[_Union[_common_pb2.ManualControlInput, _Mapping]] = ...) -> None: ...

class EdgeLookAtRequest(_message.Message):
    __slots__ = ("base", "request", "payload_index", "locked")
    BASE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_INDEX_FIELD_NUMBER: _ClassVar[int]
    LOCKED_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    request: _common_pb2.Coordinates
    payload_index: str
    locked: bool
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., request: _Optional[_Union[_common_pb2.Coordinates, _Mapping]] = ..., payload_index: _Optional[str] = ..., locked: bool = ...) -> None: ...

class EdgeTakePhotoRequest(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ...) -> None: ...

class EdgeEnableGimbalTrackingRequest(_message.Message):
    __slots__ = ("base", "enabled")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    enabled: bool
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., enabled: bool = ...) -> None: ...

class EdgeGetDetectionsRequest(_message.Message):
    __slots__ = ("base", "stream_url")
    BASE_FIELD_NUMBER: _ClassVar[int]
    STREAM_URL_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    stream_url: str
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., stream_url: _Optional[str] = ...) -> None: ...

class EdgeDetectionResponse(_message.Message):
    __slots__ = ("base", "detections")
    class DetectionResult(_message.Message):
        __slots__ = ("object_id", "object_type", "confidence", "bounding_box")
        class BoundingBox(_message.Message):
            __slots__ = ("x", "y", "width", "height")
            X_FIELD_NUMBER: _ClassVar[int]
            Y_FIELD_NUMBER: _ClassVar[int]
            WIDTH_FIELD_NUMBER: _ClassVar[int]
            HEIGHT_FIELD_NUMBER: _ClassVar[int]
            x: float
            y: float
            width: float
            height: float
            def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., width: _Optional[float] = ..., height: _Optional[float] = ...) -> None: ...
        OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
        OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
        CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
        BOUNDING_BOX_FIELD_NUMBER: _ClassVar[int]
        object_id: str
        object_type: str
        confidence: float
        bounding_box: EdgeDetectionResponse.DetectionResult.BoundingBox
        def __init__(self, object_id: _Optional[str] = ..., object_type: _Optional[str] = ..., confidence: _Optional[float] = ..., bounding_box: _Optional[_Union[EdgeDetectionResponse.DetectionResult.BoundingBox, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    DETECTIONS_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    detections: _containers.RepeatedCompositeFieldContainer[EdgeDetectionResponse.DetectionResult]
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., detections: _Optional[_Iterable[_Union[EdgeDetectionResponse.DetectionResult, _Mapping]]] = ...) -> None: ...

class EdgeGetCapabilitiesRequest(_message.Message):
    __slots__ = ("sn", "asset_id")
    SN_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    sn: str
    asset_id: str
    def __init__(self, sn: _Optional[str] = ..., asset_id: _Optional[str] = ...) -> None: ...

class EdgeGetCapabilitiesResponse(_message.Message):
    __slots__ = ("capabilities", "error")
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    capabilities: _common_pb2.CurrentCapabilities
    error: _common_pb2.GlobalErrorMessage
    def __init__(self, capabilities: _Optional[_Union[_common_pb2.CurrentCapabilities, _Mapping]] = ..., error: _Optional[_Union[_common_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...

class EdgeOpenCoverRequest(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ...) -> None: ...

class EdgeCloseCoverRequest(_message.Message):
    __slots__ = ("base", "force")
    BASE_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    force: bool
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., force: bool = ...) -> None: ...

class EdgeStartChargingRequest(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ...) -> None: ...

class EdgeStopChargingRequest(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ...) -> None: ...

class EdgeRebootAssetRequest(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ...) -> None: ...

class EdgeBootSubAssetRequest(_message.Message):
    __slots__ = ("base", "boot_up")
    BASE_FIELD_NUMBER: _ClassVar[int]
    BOOT_UP_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    boot_up: bool
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., boot_up: bool = ...) -> None: ...

class EdgeRemoteDebugModeRequest(_message.Message):
    __slots__ = ("base", "enabled")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    enabled: bool
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., enabled: bool = ...) -> None: ...

class EdgeChangeAcModeRequest(_message.Message):
    __slots__ = ("base", "mode")
    BASE_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    mode: _common_pb2.AssetAirConditionerStateEnum
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., mode: _Optional[_Union[_common_pb2.AssetAirConditionerStateEnum, str]] = ...) -> None: ...

class EdgeChangeCameraLensRequest(_message.Message):
    __slots__ = ("base", "request")
    BASE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    request: _common_pb2.ChangeCameraLensRequest
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., request: _Optional[_Union[_common_pb2.ChangeCameraLensRequest, _Mapping]] = ...) -> None: ...

class EdgeChangeCameraZoomRequest(_message.Message):
    __slots__ = ("base", "request")
    BASE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    request: _common_pb2.ChangeCameraZoomRequest
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., request: _Optional[_Union[_common_pb2.ChangeCameraZoomRequest, _Mapping]] = ...) -> None: ...

class EdgeCapturePhotoRequest(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ...) -> None: ...

class EdgeStartRecordingRequest(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ...) -> None: ...

class EdgeStopRecordingRequest(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ...) -> None: ...

class EdgeStartLiveStreamRequest(_message.Message):
    __slots__ = ("base", "request")
    BASE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    request: EdgeLiveStreamStartRequest
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., request: _Optional[_Union[EdgeLiveStreamStartRequest, _Mapping]] = ...) -> None: ...

class EdgeLiveStreamStartRequest(_message.Message):
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

class EdgeStopLiveStreamRequest(_message.Message):
    __slots__ = ("base", "request")
    BASE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    request: EdgeLiveStreamStopRequest
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., request: _Optional[_Union[EdgeLiveStreamStopRequest, _Mapping]] = ...) -> None: ...

class EdgeLiveStreamStopRequest(_message.Message):
    __slots__ = ("video_id",)
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    video_id: str
    def __init__(self, video_id: _Optional[str] = ...) -> None: ...

class EdgeRegisterAssetRequest(_message.Message):
    __slots__ = ("base", "asset_dto")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ASSET_DTO_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    asset_dto: _common_pb2.AssetProtoDTO
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., asset_dto: _Optional[_Union[_common_pb2.AssetProtoDTO, _Mapping]] = ...) -> None: ...

class EdgeDeRegisterAssetRequest(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ...) -> None: ...

class EdgeCustomCommandRequest(_message.Message):
    __slots__ = ("base", "command_type", "params")
    BASE_FIELD_NUMBER: _ClassVar[int]
    COMMAND_TYPE_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    command_type: str
    params: _struct_pb2.Struct
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., command_type: _Optional[str] = ..., params: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class EdgeCustomCommandResponse(_message.Message):
    __slots__ = ("has_errors", "tid", "sn", "asset_id", "response_message", "timestamp", "command_type", "result", "empty", "error", "progress")
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TID_FIELD_NUMBER: _ClassVar[int]
    SN_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    COMMAND_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    EMPTY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    has_errors: bool
    tid: str
    sn: str
    asset_id: str
    response_message: str
    timestamp: _timestamp_pb2.Timestamp
    command_type: str
    result: _struct_pb2.Struct
    empty: _empty_pb2.Empty
    error: _common_pb2.GlobalErrorMessage
    progress: _common_pb2.CommandProgress
    def __init__(self, has_errors: bool = ..., tid: _Optional[str] = ..., sn: _Optional[str] = ..., asset_id: _Optional[str] = ..., response_message: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., command_type: _Optional[str] = ..., result: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., empty: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., error: _Optional[_Union[_common_pb2.GlobalErrorMessage, _Mapping]] = ..., progress: _Optional[_Union[_common_pb2.CommandProgress, _Mapping]] = ...) -> None: ...
