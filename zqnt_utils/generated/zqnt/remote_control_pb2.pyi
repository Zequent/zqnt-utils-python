import datetime

from . import common_pb2 as _common_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RemoteControlResponse(_message.Message):
    __slots__ = ("has_errors", "tid", "sn", "asset_id", "timestamp", "response_message", "empty", "error", "progress")
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TID_FIELD_NUMBER: _ClassVar[int]
    SN_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    EMPTY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    has_errors: bool
    tid: str
    sn: str
    asset_id: str
    timestamp: _timestamp_pb2.Timestamp
    response_message: str
    empty: _empty_pb2.Empty
    error: _common_pb2.GlobalErrorMessage
    progress: _common_pb2.CommandProgress
    def __init__(self, has_errors: bool = ..., tid: _Optional[str] = ..., sn: _Optional[str] = ..., asset_id: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., response_message: _Optional[str] = ..., empty: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., error: _Optional[_Union[_common_pb2.GlobalErrorMessage, _Mapping]] = ..., progress: _Optional[_Union[_common_pb2.CommandProgress, _Mapping]] = ...) -> None: ...

class RemoteControlTakeOffRequest(_message.Message):
    __slots__ = ("base", "request")
    BASE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    request: _common_pb2.Coordinates
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., request: _Optional[_Union[_common_pb2.Coordinates, _Mapping]] = ...) -> None: ...

class RemoteControlGoToRequest(_message.Message):
    __slots__ = ("base", "request")
    BASE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    request: _common_pb2.Coordinates
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., request: _Optional[_Union[_common_pb2.Coordinates, _Mapping]] = ...) -> None: ...

class RemoteControlReturnToHomeRequest(_message.Message):
    __slots__ = ("base", "request")
    BASE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    request: _common_pb2.ReturnToHomeRequest
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., request: _Optional[_Union[_common_pb2.ReturnToHomeRequest, _Mapping]] = ...) -> None: ...

class RemoteControlManualControlRequest(_message.Message):
    __slots__ = ("base", "request")
    BASE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    request: _common_pb2.ManualControlRequest
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., request: _Optional[_Union[_common_pb2.ManualControlRequest, _Mapping]] = ...) -> None: ...

class RemoteControlManualControlInputRequest(_message.Message):
    __slots__ = ("base", "request")
    BASE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    request: _common_pb2.ManualControlInput
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., request: _Optional[_Union[_common_pb2.ManualControlInput, _Mapping]] = ...) -> None: ...

class RemoteControlLookAtRequest(_message.Message):
    __slots__ = ("base", "request")
    BASE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    request: _common_pb2.Coordinates
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., request: _Optional[_Union[_common_pb2.Coordinates, _Mapping]] = ...) -> None: ...

class RemoteControlDetectionRequest(_message.Message):
    __slots__ = ("base", "request")
    BASE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    request: _common_pb2.DetectionControlRequest
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., request: _Optional[_Union[_common_pb2.DetectionControlRequest, _Mapping]] = ...) -> None: ...

class RemoteControlChangeCameraLensRequest(_message.Message):
    __slots__ = ("base", "request")
    BASE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    request: _common_pb2.ChangeCameraLensRequest
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., request: _Optional[_Union[_common_pb2.ChangeCameraLensRequest, _Mapping]] = ...) -> None: ...

class RemoteControlChangeCameraZoomRequest(_message.Message):
    __slots__ = ("base", "request")
    BASE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    request: _common_pb2.ChangeCameraZoomRequest
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., request: _Optional[_Union[_common_pb2.ChangeCameraZoomRequest, _Mapping]] = ...) -> None: ...

class RemoteControlOpenCoverRequest(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ...) -> None: ...

class RemoteControlCloseCoverRequest(_message.Message):
    __slots__ = ("base", "force")
    BASE_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    force: bool
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., force: bool = ...) -> None: ...

class RemoteControlStartChargingRequest(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ...) -> None: ...

class RemoteControlStopChargingRequest(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ...) -> None: ...

class RemoteControlRebootAssetRequest(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ...) -> None: ...

class RemoteControlBootSubAssetRequest(_message.Message):
    __slots__ = ("base", "boot_up")
    BASE_FIELD_NUMBER: _ClassVar[int]
    BOOT_UP_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    boot_up: bool
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., boot_up: bool = ...) -> None: ...

class RemoteControlDebugModeRequest(_message.Message):
    __slots__ = ("base", "enabled")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    enabled: bool
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., enabled: bool = ...) -> None: ...

class RemoteControlChangeAcModeRequest(_message.Message):
    __slots__ = ("base", "mode")
    BASE_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    mode: _common_pb2.AssetAirConditionerStateEnum
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., mode: _Optional[_Union[_common_pb2.AssetAirConditionerStateEnum, str]] = ...) -> None: ...

class RemoteControlCustomCommandRequest(_message.Message):
    __slots__ = ("base", "command_type", "params")
    BASE_FIELD_NUMBER: _ClassVar[int]
    COMMAND_TYPE_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    command_type: str
    params: _struct_pb2.Struct
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ..., command_type: _Optional[str] = ..., params: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class RemoteControlCustomCommandResponse(_message.Message):
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

class RemoteControlTakePhotoRequest(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.RequestBase
    def __init__(self, base: _Optional[_Union[_common_pb2.RequestBase, _Mapping]] = ...) -> None: ...
