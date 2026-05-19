import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RemoteControlCommand(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REMOTE_CONTROL_COMMAND_ARM: _ClassVar[RemoteControlCommand]
    REMOTE_CONTROL_COMMAND_DISARM: _ClassVar[RemoteControlCommand]
    REMOTE_CONTROL_COMMAND_TAKEOFF: _ClassVar[RemoteControlCommand]
    REMOTE_CONTROL_COMMAND_LAND: _ClassVar[RemoteControlCommand]
    REMOTE_CONTROL_COMMAND_RETURN_TO_HOME: _ClassVar[RemoteControlCommand]
    REMOTE_CONTROL_COMMAND_GOTO: _ClassVar[RemoteControlCommand]
    REMOTE_CONTROL_COMMAND_OPEN_DOCK: _ClassVar[RemoteControlCommand]
    REMOTE_CONTROL_COMMAND_CLOSE_DOCK: _ClassVar[RemoteControlCommand]
    REMOTE_CONTROL_COMMAND_START_CHARGING: _ClassVar[RemoteControlCommand]
    REMOTE_CONTROL_COMMAND_STOP_CHARGING: _ClassVar[RemoteControlCommand]
    REMOTE_CONTROL_COMMAND_OPEN_REMOTE_DEBUGGING: _ClassVar[RemoteControlCommand]
    REMOTE_CONTROL_COMMAND_CLOSE_REMOTE_DEBUGGING: _ClassVar[RemoteControlCommand]
    REMOTE_CONTROL_COMMAND_GRAB_FLIGHT_AUTH: _ClassVar[RemoteControlCommand]
    REMOTE_CONTROL_COMMAND_GRAB_PAYLOAD_AUTH: _ClassVar[RemoteControlCommand]
    REMOTE_CONTROL_COMMAND_BOOT_UP_DRONE: _ClassVar[RemoteControlCommand]
    REMOTE_CONTROL_COMMAND_BOOT_DOWN_DRONE: _ClassVar[RemoteControlCommand]
    REMOTE_CONTROL_COMMAND_DOCK_AC_COOLING_MODE: _ClassVar[RemoteControlCommand]
    REMOTE_CONTROL_COMMAND_DOCK_AC_HEATING_MODE: _ClassVar[RemoteControlCommand]
    REMOTE_CONTROL_COMMAND_DOCK_AC_DEHUMIDIFICATION_MODE: _ClassVar[RemoteControlCommand]
    REMOTE_CONTROL_COMMAND_DOCK_AC_IDLE_MODE: _ClassVar[RemoteControlCommand]
    REMOTE_CONTROL_COMMAND_ENTER_REMOTE_CONTROL_MODE: _ClassVar[RemoteControlCommand]
    REMOTE_CONTROL_COMMAND_EXIT_REMOTE_CONTROL_MODE: _ClassVar[RemoteControlCommand]
    REMOTE_CONTROL_COMMAND_LIVE_STREAM_CHANGE_LENS: _ClassVar[RemoteControlCommand]
    REMOTE_CONTROL_COMMAND_HEARTBEAT: _ClassVar[RemoteControlCommand]
    REMOTE_CONTROL_COMMAND_LIVE_STREAM_CHANGE_ZOOM: _ClassVar[RemoteControlCommand]
    REMOTE_CONTROL_COMMAND_LIVE_STREAM_IR_ENABLE_TEMP_MEASUREMENT: _ClassVar[RemoteControlCommand]
    REMOTE_CONTROL_COMMAND_LIVE_STREAM_IR_DISABLE_TEMP_MEASUREMENT: _ClassVar[RemoteControlCommand]
    REMOTE_CONTROL_COMMAND_LIVE_STREAM_STATUS: _ClassVar[RemoteControlCommand]
    REMOTE_CONTROL_COMMAND_CLOSE_DOCK_FORCE: _ClassVar[RemoteControlCommand]
    REMOTE_CONTROL_COMMAND_LOOK_AT: _ClassVar[RemoteControlCommand]
    REMOTE_CONTROL_COMMAND_DETECTION_START: _ClassVar[RemoteControlCommand]
    REMOTE_CONTROL_COMMAND_ENABLE_DETECTION_TRACKING: _ClassVar[RemoteControlCommand]
    REMOTE_CONTROL_COMMAND_DETECTION_STOP: _ClassVar[RemoteControlCommand]
    REMOTE_CONTROL_COMMAND_DISABLE_DETECTION_TRACKING: _ClassVar[RemoteControlCommand]

class ManualControlStateEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MANUAL_CONTROL_STATE_DISCONNECTED: _ClassVar[ManualControlStateEnum]
    MANUAL_CONTROL_STATE_CONNECTING: _ClassVar[ManualControlStateEnum]
    MANUAL_CONTROL_STATE_CONNECTED: _ClassVar[ManualControlStateEnum]

class LiveDataServiceCommand(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LIVE_DATA_COMMAND_START_TELEMETRY_STREAM: _ClassVar[LiveDataServiceCommand]
    LIVE_DATA_COMMAND_GET_TELEMETRY_DATA: _ClassVar[LiveDataServiceCommand]
    LIVE_DATA_COMMAND_STOP_TELEMETRY_STREAM: _ClassVar[LiveDataServiceCommand]
    LIVE_DATA_COMMAND_START_LIVE_STREAM: _ClassVar[LiveDataServiceCommand]
    LIVE_DATA_COMMAND_STOP_LIVE_STREAM: _ClassVar[LiveDataServiceCommand]

class LiveDataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LIVE_DATA_TYPE_ASSET_TELEMETRY: _ClassVar[LiveDataType]
    LIVE_DATA_TYPE_SUBASSET_TELEMETRY: _ClassVar[LiveDataType]

class RainfallEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RAINFALL_NO: _ClassVar[RainfallEnum]
    RAINFALL_LIGHT: _ClassVar[RainfallEnum]
    RAINFALL_MODERATE: _ClassVar[RainfallEnum]
    RAINFALL_HEAVY: _ClassVar[RainfallEnum]

class NetworkTypeEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NETWORK_TYPE_4_G: _ClassVar[NetworkTypeEnum]
    NETWORK_TYPE_ETHERNET: _ClassVar[NetworkTypeEnum]

class AssetCoverStateEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COVER_STATE_CLOSED: _ClassVar[AssetCoverStateEnum]
    COVER_STATE_OPENED: _ClassVar[AssetCoverStateEnum]
    COVER_STATE_HALF_OPEN: _ClassVar[AssetCoverStateEnum]
    COVER_STATE_ABNORMAL: _ClassVar[AssetCoverStateEnum]

class NetworkStateQualityEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NETWORK_STATE_QUALITY_NO_SIGNAL: _ClassVar[NetworkStateQualityEnum]
    NETWORK_STATE_QUALITY_BAD: _ClassVar[NetworkStateQualityEnum]
    NETWORK_STATE_QUALITY_POOR: _ClassVar[NetworkStateQualityEnum]
    NETWORK_STATE_QUALITY_FAIR: _ClassVar[NetworkStateQualityEnum]
    NETWORK_STATE_QUALITY_GOOD: _ClassVar[NetworkStateQualityEnum]
    NETWORK_STATE_QUALITY_EXCELLENT: _ClassVar[NetworkStateQualityEnum]

class AssetAirConditionerStateEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AIR_CONDITIONER_IDLE: _ClassVar[AssetAirConditionerStateEnum]
    AIR_CONDITIONER_COOL: _ClassVar[AssetAirConditionerStateEnum]
    AIR_CONDITIONER_HEAT: _ClassVar[AssetAirConditionerStateEnum]
    AIR_CONDITIONER_DEHUMIDIFICATION: _ClassVar[AssetAirConditionerStateEnum]
    AIR_CONDITIONER_COOLING_EXIT: _ClassVar[AssetAirConditionerStateEnum]
    AIR_CONDITIONER_HEATING_EXIT: _ClassVar[AssetAirConditionerStateEnum]
    AIR_CONDITIONER_DEHUMIDIFICATION_EXIT: _ClassVar[AssetAirConditionerStateEnum]
    AIR_CONDITIONER_COOLING_PREPARATION: _ClassVar[AssetAirConditionerStateEnum]
    AIR_CONDITIONER_HEATING_PREPARATION: _ClassVar[AssetAirConditionerStateEnum]
    AIR_CONDITIONER_DEHUMIDIFICATION_PREPARATION: _ClassVar[AssetAirConditionerStateEnum]
    AIR_CONDITIONER_DISCONNECTED: _ClassVar[AssetAirConditionerStateEnum]

class AssetMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ASSET_MODE_IDLE: _ClassVar[AssetMode]
    ASSET_MODE_DEBUGGING: _ClassVar[AssetMode]
    ASSET_MODE_REMOTE_DEBUGGING: _ClassVar[AssetMode]
    ASSET_MODE_UPGRADING: _ClassVar[AssetMode]
    ASSET_MODE_WORKING: _ClassVar[AssetMode]
    ASSET_MODE_TO_BE_CALIBRATED: _ClassVar[AssetMode]

class SubAssetMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SUBASSET_MODE_IDLE: _ClassVar[SubAssetMode]
    SUBASSET_MODE_TAKEOFF_PREPARE: _ClassVar[SubAssetMode]
    SUBASSET_MODE_TAKEOFF_FINISHED: _ClassVar[SubAssetMode]
    SUBASSET_MODE_MANUAL: _ClassVar[SubAssetMode]
    SUBASSET_MODE_TAKEOFF_AUTO: _ClassVar[SubAssetMode]
    SUBASSET_MODE_WAYLINE: _ClassVar[SubAssetMode]
    SUBASSET_MODE_PANORAMIC_SHOT: _ClassVar[SubAssetMode]
    SUBASSET_MODE_ACTIVE_TRACK: _ClassVar[SubAssetMode]
    SUBASSET_MODE_ADS_B_AVOIDANCE: _ClassVar[SubAssetMode]
    SUBASSET_MODE_RETURN_AUTO: _ClassVar[SubAssetMode]
    SUBASSET_MODE_LANDING_AUTO: _ClassVar[SubAssetMode]
    SUBASSET_MODE_LANDING_FORCE: _ClassVar[SubAssetMode]
    SUBASSET_MODE_LANDING_THREE_PROPELLER: _ClassVar[SubAssetMode]
    SUBASSET_MODE_UPGRADING: _ClassVar[SubAssetMode]
    SUBASSET_MODE_DISCONNECTED: _ClassVar[SubAssetMode]
    SUBASSET_MODE_APAS: _ClassVar[SubAssetMode]
    SUBASSET_MODE_VIRTUAL_JOYSTICK: _ClassVar[SubAssetMode]
    SUBASSET_MODE_LIVE_FLIGHT_CONTROLS: _ClassVar[SubAssetMode]
    SUBASSET_MODE_AERIAL_RTK_FIXED: _ClassVar[SubAssetMode]
    SUBASSET_MODE_DOCK_SITE_EVALUATION: _ClassVar[SubAssetMode]
    SUBASSET_MODE_POI: _ClassVar[SubAssetMode]

class ErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ERROR_CODE_SYSTEM: _ClassVar[ErrorCode]
    ERROR_CODE_CLIENT: _ClassVar[ErrorCode]
    ERROR_CODE_SDK: _ClassVar[ErrorCode]
    ERROR_CODE_SERVICE: _ClassVar[ErrorCode]
    ERROR_CODE_ASSET: _ClassVar[ErrorCode]

class AssetTypeEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ASSET_TYPE_UNKNOWN: _ClassVar[AssetTypeEnum]
    ASSET_TYPE_AIRCRAFT: _ClassVar[AssetTypeEnum]
    ASSET_TYPE_DOCK: _ClassVar[AssetTypeEnum]
    ASSET_TYPE_SENSOR: _ClassVar[AssetTypeEnum]
    ASSET_TYPE_CAMERA: _ClassVar[AssetTypeEnum]
    ASSET_TYPE_OTHER: _ClassVar[AssetTypeEnum]
    ASSET_TYPE_JAMMER: _ClassVar[AssetTypeEnum]
    ASSET_TYPE_CYBER_ATTACK: _ClassVar[AssetTypeEnum]

class AssetVendor(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ASSET_VENDOR_DJI: _ClassVar[AssetVendor]
    ASSET_VENDOR_AUTEL: _ClassVar[AssetVendor]
    ASSET_VENDOR_ROS: _ClassVar[AssetVendor]
    ASSET_VENDOR_MAVLINK: _ClassVar[AssetVendor]
    ASSET_VENDOR_RTMP_RTSP: _ClassVar[AssetVendor]
    ASSET_VENDOR_SAPIENT: _ClassVar[AssetVendor]

class AssetConnection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MQTT: _ClassVar[AssetConnection]
    TCP: _ClassVar[AssetConnection]
    SERIAL: _ClassVar[AssetConnection]

class LiveStreamTypeEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LIVE_STREAM_TYPE_UNKNOWN: _ClassVar[LiveStreamTypeEnum]
    LIVE_STREAM_TYPE_RTMP: _ClassVar[LiveStreamTypeEnum]
    LIVE_STREAM_TYPE_RTSP: _ClassVar[LiveStreamTypeEnum]
    LIVE_STREAM_TYPE_WEBRTC: _ClassVar[LiveStreamTypeEnum]

class SchedulerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SCHEDULER_TYPE_OPERATION: _ClassVar[SchedulerType]
    SCHEDULER_TYPE_TASK: _ClassVar[SchedulerType]
    SCHEDULER_TYPE_SYSTEM_JOBS: _ClassVar[SchedulerType]
    SCHEDULER_TYPE_ORGANIZATION: _ClassVar[SchedulerType]
    SCHEDULER_TYPE_DATABASE: _ClassVar[SchedulerType]
    SCHEDULER_TYPE_CONNECTORS: _ClassVar[SchedulerType]

class MissionAutonomyCommand(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMMAND_UNSPECIFIED: _ClassVar[MissionAutonomyCommand]
    CREATE_OPERATION: _ClassVar[MissionAutonomyCommand]
    UPDATE_OPERATION: _ClassVar[MissionAutonomyCommand]
    DELETE_OPERATION: _ClassVar[MissionAutonomyCommand]
    CREATE_TASK: _ClassVar[MissionAutonomyCommand]
    UPDATE_TASK: _ClassVar[MissionAutonomyCommand]
    DELETE_TASK: _ClassVar[MissionAutonomyCommand]
    GET_OPERATION_BY_ID: _ClassVar[MissionAutonomyCommand]
    GET_ALL_OPERATIONS: _ClassVar[MissionAutonomyCommand]
    GET_TASK_BY_FLIGHT_ID: _ClassVar[MissionAutonomyCommand]
    GET_ALL_TASKS_FOR_OPERATION: _ClassVar[MissionAutonomyCommand]
    GET_ALL_TASKS_FOR_ASSET: _ClassVar[MissionAutonomyCommand]
    PREPARE_TASK: _ClassVar[MissionAutonomyCommand]
    START_TASK: _ClassVar[MissionAutonomyCommand]
    CANCEL_TASK: _ClassVar[MissionAutonomyCommand]
    UPLOAD_TASK_TO_STORAGE: _ClassVar[MissionAutonomyCommand]
    OPERATION_EVENTS: _ClassVar[MissionAutonomyCommand]
    REGISTER_TASK_ON_ASSET: _ClassVar[MissionAutonomyCommand]
    PAUSE_TASK: _ClassVar[MissionAutonomyCommand]
    RESUME_TASK: _ClassVar[MissionAutonomyCommand]

class VehicleAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VEHICLE_ACTION_NONE: _ClassVar[VehicleAction]
    VEHICLE_ACTION_TAKEOFF: _ClassVar[VehicleAction]
    VEHICLE_ACTION_LAND: _ClassVar[VehicleAction]

class FlyToWaylineModeProto(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FTW_MODE_SAFELY: _ClassVar[FlyToWaylineModeProto]
    FTW_MODE_POINT_TO_POINT: _ClassVar[FlyToWaylineModeProto]

class WaylineFinishActionProto(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WF_ACTION_GO_HOME: _ClassVar[WaylineFinishActionProto]
    WF_ACTION_NO_ACTION: _ClassVar[WaylineFinishActionProto]
    WF_ACTION_AUTO_LANDING: _ClassVar[WaylineFinishActionProto]
    WF_ACTION_GOTO_FIRST_WAYPOINT: _ClassVar[WaylineFinishActionProto]
    WF_ACTION_STOP: _ClassVar[WaylineFinishActionProto]

class ExitWaylineWhenRcLostEnumProto(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EWWRL_CONTINUE: _ClassVar[ExitWaylineWhenRcLostEnumProto]
    EWWRL_EXECUTE_RC_LOST_ACTION: _ClassVar[ExitWaylineWhenRcLostEnumProto]

class RcLostActionEnumProto(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RC_LOST_ACTION_HOVER: _ClassVar[RcLostActionEnumProto]
    RC_LOST_ACTION_LAND: _ClassVar[RcLostActionEnumProto]
    RC_LOST_ACTION_RETURN_HOME: _ClassVar[RcLostActionEnumProto]

class WaylineTypeEnumProto(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WT_WAYPOINT: _ClassVar[WaylineTypeEnumProto]
    WT_MAPPING_2D: _ClassVar[WaylineTypeEnumProto]
    WT_MAPPING_3D: _ClassVar[WaylineTypeEnumProto]
    WT_MAPPING_STRIP: _ClassVar[WaylineTypeEnumProto]

class WaylineTurnModeProto(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WT_MODE_COORDINATE_TURN: _ClassVar[WaylineTurnModeProto]
    WT_MODE_TO_POINT_AND_STOP_WITH_DISCONTINUITY_CURVATURE: _ClassVar[WaylineTurnModeProto]
    WT_MODE_TO_POINT_AND_STOP_WITH_CONTINUITY_CURVATURE: _ClassVar[WaylineTurnModeProto]
    WT_MODE_TO_POINT_AND_PASS_WITH_CONTINUITY_CURVATURE: _ClassVar[WaylineTurnModeProto]

class WaylineGimbalPitchModeProto(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WGP_MODE_MANUAL: _ClassVar[WaylineGimbalPitchModeProto]
    WGP_MODE_POINT_SETTINGS: _ClassVar[WaylineGimbalPitchModeProto]
    WGP_MODE_LOOK_DOWN: _ClassVar[WaylineGimbalPitchModeProto]

class RthModeEnumProto(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RTH_MODE_OPTIMAL: _ClassVar[RthModeEnumProto]
    RTH_MODE_PRESET: _ClassVar[RthModeEnumProto]

class OutOfControlActionEnumProto(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OOC_RETURN_TO_HOME: _ClassVar[OutOfControlActionEnumProto]
    OOC_HOVERING: _ClassVar[OutOfControlActionEnumProto]
    OOC_LANDING: _ClassVar[OutOfControlActionEnumProto]

class WaylinePrecisionTypeEnumProto(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRECISION_GPS: _ClassVar[WaylinePrecisionTypeEnumProto]
    PRECISION_RTK: _ClassVar[WaylinePrecisionTypeEnumProto]

class FlighttaskBreakReasonEnumProto(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BREAK_REASON_NORMAL: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_NOT_ID: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_UNCOMMON_ERROR: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_ERROR_LOADING_FILE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_ERROR_BREAKPOINT_FILE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_INCORRECT_PARAMETER: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_PARSING_FILE_TIMEOUT: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_ALREADY_STARTED: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_UNABLE_TO_INTERRUPT_WAYLINE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_NOT_STARTED: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_FLIGHT_MISSION_CONFLICT: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_UNABLE_TO_RESUME_WAYLINE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_MAXIMUM_ALTITUDE_LIMIT: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_MAXIMUM_DISTANCE_LIMIT: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_TOO_LOW_HEIGHT: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_OBSTACLE_AVOIDANCE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_POOR_RTK: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_BOUNDARY_OF_RESTRICTED_ZONE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_GEO_ALTITUDE_LIMIT: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_TAKEOFF_REQUEST_FAILED: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_TAKEOFF_EXECUTION_FAILED: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_WAYLINE_MISSION_REQUEST_FAILED: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_RTK_FIXING_REQUEST_FAILED: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_RTK_FIXING_EXECUTION_FAILED: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_WEAK_GPS: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_ERROR_RC_MODE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_HOME_POINT_NOT_REFRESHED: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_LOW_BATTERY: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_LOW_BATTERY_RTH: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_RC_DISCONNECTION: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_ON_THE_GROUND: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_ABNORMAL_VISUAL_STATUS: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_INVALID_ALTITUDE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_CALCULATION_ERROR: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_STRONG_WINDS_RTH: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_USER_EXIT: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_USER_INTERRUPTION: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_USER_TRIGGERED_RTH: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_INCORRECT_START_INFORMATION: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_UNSUPPORTED_COORDINATE_SYSTEM: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_UNSUPPORTED_ALTITUDE_MODE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_UNSUPPORTED_TRANSITIONAL_WAYLINE_MODE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_UNSUPPORTED_YAW_MODE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_UNSUPPORTED_YAW_DIRECTION_REVERSAL_MODE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_UNSUPPORTED_WAYPOINT_TYPE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_INVALID_COORDINATED_TURNING_TYPE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_INVALID_GLOBAL_SPEED: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_WAYPOINT_NUMBER_ABNORMAL: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_INVALID_LATITUDE_AND_LONGITUDE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_ABNORMAL_TURNING_INTERCEPT: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_INVALID_SEGMENT_MAXIMUM_SPEED: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_INVALID_TARGET_SPEED: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_INVALID_YAW_ANGLE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_BREAKPOINT_INVALID_MISSION_ID: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_BREAKPOINT_INVALID_PROGRESS_INFORMATION: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_BREAKPOINT_ERROR_MISSION_STATE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_BREAKPOINT_INVALID_INDEX_INFORMATION: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_BREAKPOINT_INCORRECT_LATITUDE_AND_LONGITUDE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_BREAKPOINT_INVALID_YAW: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_BREAKPOINT_INCORRECT_FLAG_SETTING: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_WAYLINE_GENERATION_FAILED: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_WAYLINE_EXECUTION_FAILED: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_WAYLINE_OBSTACLE_SENSING: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_UNRECOGNIZED_ACTION_TYPE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_DUPLICATE_ACTION_ID: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_ACTION_ID_NOT_65535: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_INVALID_NUMBER_OF_ACTION_GROUPS: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_ERROR_EFFECTIVE_RANGE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_BREAKPOINT_INVALID_ACTION_INDEX: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_BREAKPOINT_TRIGGER_RUNNING_ABNORMAL: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_BREAKPOINT_DUPLICATE_ACTION_GROUP_ID: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_BREAKPOINT_DUPLICATE_ACTION_GROUP_POSITION: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_BREAKPOINT_INVALID_ACTION_GROUP_POSITION: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_BREAKPOINT_INVALID_ACTION_ID: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_BREAKPOINT_UNABLE_TO_INTERRUPT: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_INCORRECT_BREAKPOINT_INFORMATION: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_BREAKPOINT_UNRECOGNIZED_ACTION_TYPE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_BREAKPOINT_UNRECOGNIZED_TRIGGER_TYPE: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_UNKNOWN_ERROR_1: _ClassVar[FlighttaskBreakReasonEnumProto]
    BREAK_REASON_UNKNOWN_ERROR_2: _ClassVar[FlighttaskBreakReasonEnumProto]

class TaskGoal(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TASK_UNDEFINED: _ClassVar[TaskGoal]
    TRACK: _ClassVar[TaskGoal]
    FOLLOW: _ClassVar[TaskGoal]
    SIMPLE: _ClassVar[TaskGoal]
    DETECT: _ClassVar[TaskGoal]

class TaskTypeProto(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TASK_TYPE_UNSPECIFIED: _ClassVar[TaskTypeProto]
    TASK_TYPE_DETECT: _ClassVar[TaskTypeProto]
    TASK_TYPE_AREA_MAPPING: _ClassVar[TaskTypeProto]
    TASK_TYPE_WAYPOINT: _ClassVar[TaskTypeProto]
    TASK_TYPE_POI: _ClassVar[TaskTypeProto]
    TASK_TYPE_FOLLOW: _ClassVar[TaskTypeProto]
    TASK_TYPE_TRACK: _ClassVar[TaskTypeProto]
    TASK_TYPE_COUNTER_DRONE: _ClassVar[TaskTypeProto]

class TaskStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TASK_UNKNOWN: _ClassVar[TaskStatus]
    TASK_DRAFT: _ClassVar[TaskStatus]
    TASK_SCHEDULED: _ClassVar[TaskStatus]
    TASK_RUNNING: _ClassVar[TaskStatus]
    TASK_ERROR: _ClassVar[TaskStatus]
    TASK_COMPLETED: _ClassVar[TaskStatus]
    TASK_PREPARED: _ClassVar[TaskStatus]
    TASK_PAUSED: _ClassVar[TaskStatus]

class MissionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STANDARD: _ClassVar[MissionType]
    REMOTE_OPS: _ClassVar[MissionType]
    DRF: _ClassVar[MissionType]
    MISSION: _ClassVar[MissionType]

class MissionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OPERATION_UNKNOWN: _ClassVar[MissionStatus]
    OPERATION_DRAFT: _ClassVar[MissionStatus]
    OPERATION_ACTIVE: _ClassVar[MissionStatus]
    OPERATION_INACTIVE: _ClassVar[MissionStatus]
    OPERATION_ERROR: _ClassVar[MissionStatus]
REMOTE_CONTROL_COMMAND_ARM: RemoteControlCommand
REMOTE_CONTROL_COMMAND_DISARM: RemoteControlCommand
REMOTE_CONTROL_COMMAND_TAKEOFF: RemoteControlCommand
REMOTE_CONTROL_COMMAND_LAND: RemoteControlCommand
REMOTE_CONTROL_COMMAND_RETURN_TO_HOME: RemoteControlCommand
REMOTE_CONTROL_COMMAND_GOTO: RemoteControlCommand
REMOTE_CONTROL_COMMAND_OPEN_DOCK: RemoteControlCommand
REMOTE_CONTROL_COMMAND_CLOSE_DOCK: RemoteControlCommand
REMOTE_CONTROL_COMMAND_START_CHARGING: RemoteControlCommand
REMOTE_CONTROL_COMMAND_STOP_CHARGING: RemoteControlCommand
REMOTE_CONTROL_COMMAND_OPEN_REMOTE_DEBUGGING: RemoteControlCommand
REMOTE_CONTROL_COMMAND_CLOSE_REMOTE_DEBUGGING: RemoteControlCommand
REMOTE_CONTROL_COMMAND_GRAB_FLIGHT_AUTH: RemoteControlCommand
REMOTE_CONTROL_COMMAND_GRAB_PAYLOAD_AUTH: RemoteControlCommand
REMOTE_CONTROL_COMMAND_BOOT_UP_DRONE: RemoteControlCommand
REMOTE_CONTROL_COMMAND_BOOT_DOWN_DRONE: RemoteControlCommand
REMOTE_CONTROL_COMMAND_DOCK_AC_COOLING_MODE: RemoteControlCommand
REMOTE_CONTROL_COMMAND_DOCK_AC_HEATING_MODE: RemoteControlCommand
REMOTE_CONTROL_COMMAND_DOCK_AC_DEHUMIDIFICATION_MODE: RemoteControlCommand
REMOTE_CONTROL_COMMAND_DOCK_AC_IDLE_MODE: RemoteControlCommand
REMOTE_CONTROL_COMMAND_ENTER_REMOTE_CONTROL_MODE: RemoteControlCommand
REMOTE_CONTROL_COMMAND_EXIT_REMOTE_CONTROL_MODE: RemoteControlCommand
REMOTE_CONTROL_COMMAND_LIVE_STREAM_CHANGE_LENS: RemoteControlCommand
REMOTE_CONTROL_COMMAND_HEARTBEAT: RemoteControlCommand
REMOTE_CONTROL_COMMAND_LIVE_STREAM_CHANGE_ZOOM: RemoteControlCommand
REMOTE_CONTROL_COMMAND_LIVE_STREAM_IR_ENABLE_TEMP_MEASUREMENT: RemoteControlCommand
REMOTE_CONTROL_COMMAND_LIVE_STREAM_IR_DISABLE_TEMP_MEASUREMENT: RemoteControlCommand
REMOTE_CONTROL_COMMAND_LIVE_STREAM_STATUS: RemoteControlCommand
REMOTE_CONTROL_COMMAND_CLOSE_DOCK_FORCE: RemoteControlCommand
REMOTE_CONTROL_COMMAND_LOOK_AT: RemoteControlCommand
REMOTE_CONTROL_COMMAND_DETECTION_START: RemoteControlCommand
REMOTE_CONTROL_COMMAND_ENABLE_DETECTION_TRACKING: RemoteControlCommand
REMOTE_CONTROL_COMMAND_DETECTION_STOP: RemoteControlCommand
REMOTE_CONTROL_COMMAND_DISABLE_DETECTION_TRACKING: RemoteControlCommand
MANUAL_CONTROL_STATE_DISCONNECTED: ManualControlStateEnum
MANUAL_CONTROL_STATE_CONNECTING: ManualControlStateEnum
MANUAL_CONTROL_STATE_CONNECTED: ManualControlStateEnum
LIVE_DATA_COMMAND_START_TELEMETRY_STREAM: LiveDataServiceCommand
LIVE_DATA_COMMAND_GET_TELEMETRY_DATA: LiveDataServiceCommand
LIVE_DATA_COMMAND_STOP_TELEMETRY_STREAM: LiveDataServiceCommand
LIVE_DATA_COMMAND_START_LIVE_STREAM: LiveDataServiceCommand
LIVE_DATA_COMMAND_STOP_LIVE_STREAM: LiveDataServiceCommand
LIVE_DATA_TYPE_ASSET_TELEMETRY: LiveDataType
LIVE_DATA_TYPE_SUBASSET_TELEMETRY: LiveDataType
RAINFALL_NO: RainfallEnum
RAINFALL_LIGHT: RainfallEnum
RAINFALL_MODERATE: RainfallEnum
RAINFALL_HEAVY: RainfallEnum
NETWORK_TYPE_4_G: NetworkTypeEnum
NETWORK_TYPE_ETHERNET: NetworkTypeEnum
COVER_STATE_CLOSED: AssetCoverStateEnum
COVER_STATE_OPENED: AssetCoverStateEnum
COVER_STATE_HALF_OPEN: AssetCoverStateEnum
COVER_STATE_ABNORMAL: AssetCoverStateEnum
NETWORK_STATE_QUALITY_NO_SIGNAL: NetworkStateQualityEnum
NETWORK_STATE_QUALITY_BAD: NetworkStateQualityEnum
NETWORK_STATE_QUALITY_POOR: NetworkStateQualityEnum
NETWORK_STATE_QUALITY_FAIR: NetworkStateQualityEnum
NETWORK_STATE_QUALITY_GOOD: NetworkStateQualityEnum
NETWORK_STATE_QUALITY_EXCELLENT: NetworkStateQualityEnum
AIR_CONDITIONER_IDLE: AssetAirConditionerStateEnum
AIR_CONDITIONER_COOL: AssetAirConditionerStateEnum
AIR_CONDITIONER_HEAT: AssetAirConditionerStateEnum
AIR_CONDITIONER_DEHUMIDIFICATION: AssetAirConditionerStateEnum
AIR_CONDITIONER_COOLING_EXIT: AssetAirConditionerStateEnum
AIR_CONDITIONER_HEATING_EXIT: AssetAirConditionerStateEnum
AIR_CONDITIONER_DEHUMIDIFICATION_EXIT: AssetAirConditionerStateEnum
AIR_CONDITIONER_COOLING_PREPARATION: AssetAirConditionerStateEnum
AIR_CONDITIONER_HEATING_PREPARATION: AssetAirConditionerStateEnum
AIR_CONDITIONER_DEHUMIDIFICATION_PREPARATION: AssetAirConditionerStateEnum
AIR_CONDITIONER_DISCONNECTED: AssetAirConditionerStateEnum
ASSET_MODE_IDLE: AssetMode
ASSET_MODE_DEBUGGING: AssetMode
ASSET_MODE_REMOTE_DEBUGGING: AssetMode
ASSET_MODE_UPGRADING: AssetMode
ASSET_MODE_WORKING: AssetMode
ASSET_MODE_TO_BE_CALIBRATED: AssetMode
SUBASSET_MODE_IDLE: SubAssetMode
SUBASSET_MODE_TAKEOFF_PREPARE: SubAssetMode
SUBASSET_MODE_TAKEOFF_FINISHED: SubAssetMode
SUBASSET_MODE_MANUAL: SubAssetMode
SUBASSET_MODE_TAKEOFF_AUTO: SubAssetMode
SUBASSET_MODE_WAYLINE: SubAssetMode
SUBASSET_MODE_PANORAMIC_SHOT: SubAssetMode
SUBASSET_MODE_ACTIVE_TRACK: SubAssetMode
SUBASSET_MODE_ADS_B_AVOIDANCE: SubAssetMode
SUBASSET_MODE_RETURN_AUTO: SubAssetMode
SUBASSET_MODE_LANDING_AUTO: SubAssetMode
SUBASSET_MODE_LANDING_FORCE: SubAssetMode
SUBASSET_MODE_LANDING_THREE_PROPELLER: SubAssetMode
SUBASSET_MODE_UPGRADING: SubAssetMode
SUBASSET_MODE_DISCONNECTED: SubAssetMode
SUBASSET_MODE_APAS: SubAssetMode
SUBASSET_MODE_VIRTUAL_JOYSTICK: SubAssetMode
SUBASSET_MODE_LIVE_FLIGHT_CONTROLS: SubAssetMode
SUBASSET_MODE_AERIAL_RTK_FIXED: SubAssetMode
SUBASSET_MODE_DOCK_SITE_EVALUATION: SubAssetMode
SUBASSET_MODE_POI: SubAssetMode
ERROR_CODE_SYSTEM: ErrorCode
ERROR_CODE_CLIENT: ErrorCode
ERROR_CODE_SDK: ErrorCode
ERROR_CODE_SERVICE: ErrorCode
ERROR_CODE_ASSET: ErrorCode
ASSET_TYPE_UNKNOWN: AssetTypeEnum
ASSET_TYPE_AIRCRAFT: AssetTypeEnum
ASSET_TYPE_DOCK: AssetTypeEnum
ASSET_TYPE_SENSOR: AssetTypeEnum
ASSET_TYPE_CAMERA: AssetTypeEnum
ASSET_TYPE_OTHER: AssetTypeEnum
ASSET_TYPE_JAMMER: AssetTypeEnum
ASSET_TYPE_CYBER_ATTACK: AssetTypeEnum
ASSET_VENDOR_DJI: AssetVendor
ASSET_VENDOR_AUTEL: AssetVendor
ASSET_VENDOR_ROS: AssetVendor
ASSET_VENDOR_MAVLINK: AssetVendor
ASSET_VENDOR_RTMP_RTSP: AssetVendor
ASSET_VENDOR_SAPIENT: AssetVendor
MQTT: AssetConnection
TCP: AssetConnection
SERIAL: AssetConnection
LIVE_STREAM_TYPE_UNKNOWN: LiveStreamTypeEnum
LIVE_STREAM_TYPE_RTMP: LiveStreamTypeEnum
LIVE_STREAM_TYPE_RTSP: LiveStreamTypeEnum
LIVE_STREAM_TYPE_WEBRTC: LiveStreamTypeEnum
SCHEDULER_TYPE_OPERATION: SchedulerType
SCHEDULER_TYPE_TASK: SchedulerType
SCHEDULER_TYPE_SYSTEM_JOBS: SchedulerType
SCHEDULER_TYPE_ORGANIZATION: SchedulerType
SCHEDULER_TYPE_DATABASE: SchedulerType
SCHEDULER_TYPE_CONNECTORS: SchedulerType
COMMAND_UNSPECIFIED: MissionAutonomyCommand
CREATE_OPERATION: MissionAutonomyCommand
UPDATE_OPERATION: MissionAutonomyCommand
DELETE_OPERATION: MissionAutonomyCommand
CREATE_TASK: MissionAutonomyCommand
UPDATE_TASK: MissionAutonomyCommand
DELETE_TASK: MissionAutonomyCommand
GET_OPERATION_BY_ID: MissionAutonomyCommand
GET_ALL_OPERATIONS: MissionAutonomyCommand
GET_TASK_BY_FLIGHT_ID: MissionAutonomyCommand
GET_ALL_TASKS_FOR_OPERATION: MissionAutonomyCommand
GET_ALL_TASKS_FOR_ASSET: MissionAutonomyCommand
PREPARE_TASK: MissionAutonomyCommand
START_TASK: MissionAutonomyCommand
CANCEL_TASK: MissionAutonomyCommand
UPLOAD_TASK_TO_STORAGE: MissionAutonomyCommand
OPERATION_EVENTS: MissionAutonomyCommand
REGISTER_TASK_ON_ASSET: MissionAutonomyCommand
PAUSE_TASK: MissionAutonomyCommand
RESUME_TASK: MissionAutonomyCommand
VEHICLE_ACTION_NONE: VehicleAction
VEHICLE_ACTION_TAKEOFF: VehicleAction
VEHICLE_ACTION_LAND: VehicleAction
FTW_MODE_SAFELY: FlyToWaylineModeProto
FTW_MODE_POINT_TO_POINT: FlyToWaylineModeProto
WF_ACTION_GO_HOME: WaylineFinishActionProto
WF_ACTION_NO_ACTION: WaylineFinishActionProto
WF_ACTION_AUTO_LANDING: WaylineFinishActionProto
WF_ACTION_GOTO_FIRST_WAYPOINT: WaylineFinishActionProto
WF_ACTION_STOP: WaylineFinishActionProto
EWWRL_CONTINUE: ExitWaylineWhenRcLostEnumProto
EWWRL_EXECUTE_RC_LOST_ACTION: ExitWaylineWhenRcLostEnumProto
RC_LOST_ACTION_HOVER: RcLostActionEnumProto
RC_LOST_ACTION_LAND: RcLostActionEnumProto
RC_LOST_ACTION_RETURN_HOME: RcLostActionEnumProto
WT_WAYPOINT: WaylineTypeEnumProto
WT_MAPPING_2D: WaylineTypeEnumProto
WT_MAPPING_3D: WaylineTypeEnumProto
WT_MAPPING_STRIP: WaylineTypeEnumProto
WT_MODE_COORDINATE_TURN: WaylineTurnModeProto
WT_MODE_TO_POINT_AND_STOP_WITH_DISCONTINUITY_CURVATURE: WaylineTurnModeProto
WT_MODE_TO_POINT_AND_STOP_WITH_CONTINUITY_CURVATURE: WaylineTurnModeProto
WT_MODE_TO_POINT_AND_PASS_WITH_CONTINUITY_CURVATURE: WaylineTurnModeProto
WGP_MODE_MANUAL: WaylineGimbalPitchModeProto
WGP_MODE_POINT_SETTINGS: WaylineGimbalPitchModeProto
WGP_MODE_LOOK_DOWN: WaylineGimbalPitchModeProto
RTH_MODE_OPTIMAL: RthModeEnumProto
RTH_MODE_PRESET: RthModeEnumProto
OOC_RETURN_TO_HOME: OutOfControlActionEnumProto
OOC_HOVERING: OutOfControlActionEnumProto
OOC_LANDING: OutOfControlActionEnumProto
PRECISION_GPS: WaylinePrecisionTypeEnumProto
PRECISION_RTK: WaylinePrecisionTypeEnumProto
BREAK_REASON_NORMAL: FlighttaskBreakReasonEnumProto
BREAK_REASON_NOT_ID: FlighttaskBreakReasonEnumProto
BREAK_REASON_UNCOMMON_ERROR: FlighttaskBreakReasonEnumProto
BREAK_REASON_ERROR_LOADING_FILE: FlighttaskBreakReasonEnumProto
BREAK_REASON_ERROR_BREAKPOINT_FILE: FlighttaskBreakReasonEnumProto
BREAK_REASON_INCORRECT_PARAMETER: FlighttaskBreakReasonEnumProto
BREAK_REASON_PARSING_FILE_TIMEOUT: FlighttaskBreakReasonEnumProto
BREAK_REASON_ALREADY_STARTED: FlighttaskBreakReasonEnumProto
BREAK_REASON_UNABLE_TO_INTERRUPT_WAYLINE: FlighttaskBreakReasonEnumProto
BREAK_REASON_NOT_STARTED: FlighttaskBreakReasonEnumProto
BREAK_REASON_FLIGHT_MISSION_CONFLICT: FlighttaskBreakReasonEnumProto
BREAK_REASON_UNABLE_TO_RESUME_WAYLINE: FlighttaskBreakReasonEnumProto
BREAK_REASON_MAXIMUM_ALTITUDE_LIMIT: FlighttaskBreakReasonEnumProto
BREAK_REASON_MAXIMUM_DISTANCE_LIMIT: FlighttaskBreakReasonEnumProto
BREAK_REASON_TOO_LOW_HEIGHT: FlighttaskBreakReasonEnumProto
BREAK_REASON_OBSTACLE_AVOIDANCE: FlighttaskBreakReasonEnumProto
BREAK_REASON_POOR_RTK: FlighttaskBreakReasonEnumProto
BREAK_REASON_BOUNDARY_OF_RESTRICTED_ZONE: FlighttaskBreakReasonEnumProto
BREAK_REASON_GEO_ALTITUDE_LIMIT: FlighttaskBreakReasonEnumProto
BREAK_REASON_TAKEOFF_REQUEST_FAILED: FlighttaskBreakReasonEnumProto
BREAK_REASON_TAKEOFF_EXECUTION_FAILED: FlighttaskBreakReasonEnumProto
BREAK_REASON_WAYLINE_MISSION_REQUEST_FAILED: FlighttaskBreakReasonEnumProto
BREAK_REASON_RTK_FIXING_REQUEST_FAILED: FlighttaskBreakReasonEnumProto
BREAK_REASON_RTK_FIXING_EXECUTION_FAILED: FlighttaskBreakReasonEnumProto
BREAK_REASON_WEAK_GPS: FlighttaskBreakReasonEnumProto
BREAK_REASON_ERROR_RC_MODE: FlighttaskBreakReasonEnumProto
BREAK_REASON_HOME_POINT_NOT_REFRESHED: FlighttaskBreakReasonEnumProto
BREAK_REASON_LOW_BATTERY: FlighttaskBreakReasonEnumProto
BREAK_REASON_LOW_BATTERY_RTH: FlighttaskBreakReasonEnumProto
BREAK_REASON_RC_DISCONNECTION: FlighttaskBreakReasonEnumProto
BREAK_REASON_ON_THE_GROUND: FlighttaskBreakReasonEnumProto
BREAK_REASON_ABNORMAL_VISUAL_STATUS: FlighttaskBreakReasonEnumProto
BREAK_REASON_INVALID_ALTITUDE: FlighttaskBreakReasonEnumProto
BREAK_REASON_CALCULATION_ERROR: FlighttaskBreakReasonEnumProto
BREAK_REASON_STRONG_WINDS_RTH: FlighttaskBreakReasonEnumProto
BREAK_REASON_USER_EXIT: FlighttaskBreakReasonEnumProto
BREAK_REASON_USER_INTERRUPTION: FlighttaskBreakReasonEnumProto
BREAK_REASON_USER_TRIGGERED_RTH: FlighttaskBreakReasonEnumProto
BREAK_REASON_INCORRECT_START_INFORMATION: FlighttaskBreakReasonEnumProto
BREAK_REASON_UNSUPPORTED_COORDINATE_SYSTEM: FlighttaskBreakReasonEnumProto
BREAK_REASON_UNSUPPORTED_ALTITUDE_MODE: FlighttaskBreakReasonEnumProto
BREAK_REASON_UNSUPPORTED_TRANSITIONAL_WAYLINE_MODE: FlighttaskBreakReasonEnumProto
BREAK_REASON_UNSUPPORTED_YAW_MODE: FlighttaskBreakReasonEnumProto
BREAK_REASON_UNSUPPORTED_YAW_DIRECTION_REVERSAL_MODE: FlighttaskBreakReasonEnumProto
BREAK_REASON_UNSUPPORTED_WAYPOINT_TYPE: FlighttaskBreakReasonEnumProto
BREAK_REASON_INVALID_COORDINATED_TURNING_TYPE: FlighttaskBreakReasonEnumProto
BREAK_REASON_INVALID_GLOBAL_SPEED: FlighttaskBreakReasonEnumProto
BREAK_REASON_WAYPOINT_NUMBER_ABNORMAL: FlighttaskBreakReasonEnumProto
BREAK_REASON_INVALID_LATITUDE_AND_LONGITUDE: FlighttaskBreakReasonEnumProto
BREAK_REASON_ABNORMAL_TURNING_INTERCEPT: FlighttaskBreakReasonEnumProto
BREAK_REASON_INVALID_SEGMENT_MAXIMUM_SPEED: FlighttaskBreakReasonEnumProto
BREAK_REASON_INVALID_TARGET_SPEED: FlighttaskBreakReasonEnumProto
BREAK_REASON_INVALID_YAW_ANGLE: FlighttaskBreakReasonEnumProto
BREAK_REASON_BREAKPOINT_INVALID_MISSION_ID: FlighttaskBreakReasonEnumProto
BREAK_REASON_BREAKPOINT_INVALID_PROGRESS_INFORMATION: FlighttaskBreakReasonEnumProto
BREAK_REASON_BREAKPOINT_ERROR_MISSION_STATE: FlighttaskBreakReasonEnumProto
BREAK_REASON_BREAKPOINT_INVALID_INDEX_INFORMATION: FlighttaskBreakReasonEnumProto
BREAK_REASON_BREAKPOINT_INCORRECT_LATITUDE_AND_LONGITUDE: FlighttaskBreakReasonEnumProto
BREAK_REASON_BREAKPOINT_INVALID_YAW: FlighttaskBreakReasonEnumProto
BREAK_REASON_BREAKPOINT_INCORRECT_FLAG_SETTING: FlighttaskBreakReasonEnumProto
BREAK_REASON_WAYLINE_GENERATION_FAILED: FlighttaskBreakReasonEnumProto
BREAK_REASON_WAYLINE_EXECUTION_FAILED: FlighttaskBreakReasonEnumProto
BREAK_REASON_WAYLINE_OBSTACLE_SENSING: FlighttaskBreakReasonEnumProto
BREAK_REASON_UNRECOGNIZED_ACTION_TYPE: FlighttaskBreakReasonEnumProto
BREAK_REASON_DUPLICATE_ACTION_ID: FlighttaskBreakReasonEnumProto
BREAK_REASON_ACTION_ID_NOT_65535: FlighttaskBreakReasonEnumProto
BREAK_REASON_INVALID_NUMBER_OF_ACTION_GROUPS: FlighttaskBreakReasonEnumProto
BREAK_REASON_ERROR_EFFECTIVE_RANGE: FlighttaskBreakReasonEnumProto
BREAK_REASON_BREAKPOINT_INVALID_ACTION_INDEX: FlighttaskBreakReasonEnumProto
BREAK_REASON_BREAKPOINT_TRIGGER_RUNNING_ABNORMAL: FlighttaskBreakReasonEnumProto
BREAK_REASON_BREAKPOINT_DUPLICATE_ACTION_GROUP_ID: FlighttaskBreakReasonEnumProto
BREAK_REASON_BREAKPOINT_DUPLICATE_ACTION_GROUP_POSITION: FlighttaskBreakReasonEnumProto
BREAK_REASON_BREAKPOINT_INVALID_ACTION_GROUP_POSITION: FlighttaskBreakReasonEnumProto
BREAK_REASON_BREAKPOINT_INVALID_ACTION_ID: FlighttaskBreakReasonEnumProto
BREAK_REASON_BREAKPOINT_UNABLE_TO_INTERRUPT: FlighttaskBreakReasonEnumProto
BREAK_REASON_INCORRECT_BREAKPOINT_INFORMATION: FlighttaskBreakReasonEnumProto
BREAK_REASON_BREAKPOINT_UNRECOGNIZED_ACTION_TYPE: FlighttaskBreakReasonEnumProto
BREAK_REASON_BREAKPOINT_UNRECOGNIZED_TRIGGER_TYPE: FlighttaskBreakReasonEnumProto
BREAK_REASON_UNKNOWN_ERROR_1: FlighttaskBreakReasonEnumProto
BREAK_REASON_UNKNOWN_ERROR_2: FlighttaskBreakReasonEnumProto
TASK_UNDEFINED: TaskGoal
TRACK: TaskGoal
FOLLOW: TaskGoal
SIMPLE: TaskGoal
DETECT: TaskGoal
TASK_TYPE_UNSPECIFIED: TaskTypeProto
TASK_TYPE_DETECT: TaskTypeProto
TASK_TYPE_AREA_MAPPING: TaskTypeProto
TASK_TYPE_WAYPOINT: TaskTypeProto
TASK_TYPE_POI: TaskTypeProto
TASK_TYPE_FOLLOW: TaskTypeProto
TASK_TYPE_TRACK: TaskTypeProto
TASK_TYPE_COUNTER_DRONE: TaskTypeProto
TASK_UNKNOWN: TaskStatus
TASK_DRAFT: TaskStatus
TASK_SCHEDULED: TaskStatus
TASK_RUNNING: TaskStatus
TASK_ERROR: TaskStatus
TASK_COMPLETED: TaskStatus
TASK_PREPARED: TaskStatus
TASK_PAUSED: TaskStatus
STANDARD: MissionType
REMOTE_OPS: MissionType
DRF: MissionType
MISSION: MissionType
OPERATION_UNKNOWN: MissionStatus
OPERATION_DRAFT: MissionStatus
OPERATION_ACTIVE: MissionStatus
OPERATION_INACTIVE: MissionStatus
OPERATION_ERROR: MissionStatus

class GlobalErrorMessage(_message.Message):
    __slots__ = ("timestamp", "error_message", "error_code")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    error_message: str
    error_code: ErrorCode
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., error_message: _Optional[str] = ..., error_code: _Optional[_Union[ErrorCode, str]] = ...) -> None: ...

class Capability(_message.Message):
    __slots__ = ("command", "description", "available", "unavailable_reason", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    UNAVAILABLE_REASON_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    command: str
    description: str
    available: bool
    unavailable_reason: str
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, command: _Optional[str] = ..., description: _Optional[str] = ..., available: bool = ..., unavailable_reason: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...

class CurrentCapabilities(_message.Message):
    __slots__ = ("asset_sn", "asset_type", "capabilities", "timestamp")
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    asset_sn: str
    asset_type: str
    capabilities: _containers.RepeatedCompositeFieldContainer[Capability]
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, asset_sn: _Optional[str] = ..., asset_type: _Optional[str] = ..., capabilities: _Optional[_Iterable[_Union[Capability, _Mapping]]] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Coordinates(_message.Message):
    __slots__ = ("latitude", "longitude", "altitude")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    altitude: float
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., altitude: _Optional[float] = ...) -> None: ...

class ReturnToHomeRequest(_message.Message):
    __slots__ = ("altitude",)
    ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    altitude: float
    def __init__(self, altitude: _Optional[float] = ...) -> None: ...

class ManualControlRequest(_message.Message):
    __slots__ = ("client_id", "user_id", "reason", "session_id")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    user_id: str
    reason: str
    session_id: str
    def __init__(self, client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., reason: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class ManualControlInput(_message.Message):
    __slots__ = ("roll", "pitch", "yaw", "throttle", "gimbal_pitch")
    ROLL_FIELD_NUMBER: _ClassVar[int]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    YAW_FIELD_NUMBER: _ClassVar[int]
    THROTTLE_FIELD_NUMBER: _ClassVar[int]
    GIMBAL_PITCH_FIELD_NUMBER: _ClassVar[int]
    roll: float
    pitch: float
    yaw: float
    throttle: float
    gimbal_pitch: float
    def __init__(self, roll: _Optional[float] = ..., pitch: _Optional[float] = ..., yaw: _Optional[float] = ..., throttle: _Optional[float] = ..., gimbal_pitch: _Optional[float] = ...) -> None: ...

class LiveStreamState(_message.Message):
    __slots__ = ("video_id", "stream_url", "is_live", "started_at", "asset_type")
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    STREAM_URL_FIELD_NUMBER: _ClassVar[int]
    IS_LIVE_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    video_id: str
    stream_url: str
    is_live: bool
    started_at: _timestamp_pb2.Timestamp
    asset_type: str
    def __init__(self, video_id: _Optional[str] = ..., stream_url: _Optional[str] = ..., is_live: bool = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., asset_type: _Optional[str] = ...) -> None: ...

class LiveStreamStartResponse(_message.Message):
    __slots__ = ("stream_url", "video_id")
    STREAM_URL_FIELD_NUMBER: _ClassVar[int]
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    stream_url: str
    video_id: str
    def __init__(self, stream_url: _Optional[str] = ..., video_id: _Optional[str] = ...) -> None: ...

class ChangeCameraLensRequest(_message.Message):
    __slots__ = ("lens",)
    LENS_FIELD_NUMBER: _ClassVar[int]
    lens: str
    def __init__(self, lens: _Optional[str] = ...) -> None: ...

class ChangeCameraZoomRequest(_message.Message):
    __slots__ = ("lens", "zoom")
    LENS_FIELD_NUMBER: _ClassVar[int]
    ZOOM_FIELD_NUMBER: _ClassVar[int]
    lens: str
    zoom: int
    def __init__(self, lens: _Optional[str] = ..., zoom: _Optional[int] = ...) -> None: ...

class DetectionControlRequest(_message.Message):
    __slots__ = ("command", "asset_sn", "sub_asset_sn", "task_id", "stream_url", "gimbal_tracking_enabled")
    class DetectionControlCommand(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REMOTE_CONTROL_COMMAND_DETECTION_START: _ClassVar[DetectionControlRequest.DetectionControlCommand]
        REMOTE_CONTROL_COMMAND_DETECTION_STOP: _ClassVar[DetectionControlRequest.DetectionControlCommand]
    REMOTE_CONTROL_COMMAND_DETECTION_START: DetectionControlRequest.DetectionControlCommand
    REMOTE_CONTROL_COMMAND_DETECTION_STOP: DetectionControlRequest.DetectionControlCommand
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    STREAM_URL_FIELD_NUMBER: _ClassVar[int]
    GIMBAL_TRACKING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    command: DetectionControlRequest.DetectionControlCommand
    asset_sn: str
    sub_asset_sn: str
    task_id: str
    stream_url: str
    gimbal_tracking_enabled: bool
    def __init__(self, command: _Optional[_Union[DetectionControlRequest.DetectionControlCommand, str]] = ..., asset_sn: _Optional[str] = ..., sub_asset_sn: _Optional[str] = ..., task_id: _Optional[str] = ..., stream_url: _Optional[str] = ..., gimbal_tracking_enabled: bool = ...) -> None: ...

class CommandProgress(_message.Message):
    __slots__ = ("progress", "state", "left_time_in_seconds")
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    LEFT_TIME_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    progress: float
    state: str
    left_time_in_seconds: float
    def __init__(self, progress: _Optional[float] = ..., state: _Optional[str] = ..., left_time_in_seconds: _Optional[float] = ...) -> None: ...

class ManualControlState(_message.Message):
    __slots__ = ("state", "sn", "asset_id", "active", "client_id", "user_id", "session_id")
    STATE_FIELD_NUMBER: _ClassVar[int]
    SN_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    state: ManualControlStateEnum
    sn: str
    asset_id: str
    active: bool
    client_id: str
    user_id: str
    session_id: str
    def __init__(self, state: _Optional[_Union[ManualControlStateEnum, str]] = ..., sn: _Optional[str] = ..., asset_id: _Optional[str] = ..., active: bool = ..., client_id: _Optional[str] = ..., user_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class RequestBase(_message.Message):
    __slots__ = ("tid", "sn", "timestamp")
    TID_FIELD_NUMBER: _ClassVar[int]
    SN_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    tid: str
    sn: str
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, tid: _Optional[str] = ..., sn: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AssetProtoDTO(_message.Message):
    __slots__ = ("id", "sn", "name", "type", "vendor", "connection", "connection_string", "model", "port", "live_stream_server", "external_device_type", "external_device_sub_type", "organization", "online", "sub_asset_dto", "external_id", "stream_type")
    ID_FIELD_NUMBER: _ClassVar[int]
    SN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VENDOR_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_STRING_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    LIVE_STREAM_SERVER_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_DEVICE_SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    ONLINE_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSET_DTO_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    STREAM_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    sn: str
    name: str
    type: str
    vendor: str
    connection: str
    connection_string: str
    model: str
    port: int
    live_stream_server: str
    external_device_type: str
    external_device_sub_type: str
    organization: str
    online: bool
    sub_asset_dto: SubAssetProtoDTO
    external_id: str
    stream_type: LiveStreamTypeEnum
    def __init__(self, id: _Optional[str] = ..., sn: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[str] = ..., vendor: _Optional[str] = ..., connection: _Optional[str] = ..., connection_string: _Optional[str] = ..., model: _Optional[str] = ..., port: _Optional[int] = ..., live_stream_server: _Optional[str] = ..., external_device_type: _Optional[str] = ..., external_device_sub_type: _Optional[str] = ..., organization: _Optional[str] = ..., online: bool = ..., sub_asset_dto: _Optional[_Union[SubAssetProtoDTO, _Mapping]] = ..., external_id: _Optional[str] = ..., stream_type: _Optional[_Union[LiveStreamTypeEnum, str]] = ...) -> None: ...

class SubAssetProtoDTO(_message.Message):
    __slots__ = ("id", "sn", "name", "type", "vendor", "connection", "connection_string", "model", "port", "live_stream_server", "external_device_type", "external_device_sub_type", "organization", "online", "external_id", "stream_type", "stream_url_predefined")
    ID_FIELD_NUMBER: _ClassVar[int]
    SN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VENDOR_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_STRING_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    LIVE_STREAM_SERVER_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_DEVICE_SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    ONLINE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    STREAM_TYPE_FIELD_NUMBER: _ClassVar[int]
    STREAM_URL_PREDEFINED_FIELD_NUMBER: _ClassVar[int]
    id: str
    sn: str
    name: str
    type: str
    vendor: str
    connection: str
    connection_string: str
    model: str
    port: int
    live_stream_server: str
    external_device_type: str
    external_device_sub_type: str
    organization: str
    online: bool
    external_id: str
    stream_type: LiveStreamTypeEnum
    stream_url_predefined: bool
    def __init__(self, id: _Optional[str] = ..., sn: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[str] = ..., vendor: _Optional[str] = ..., connection: _Optional[str] = ..., connection_string: _Optional[str] = ..., model: _Optional[str] = ..., port: _Optional[int] = ..., live_stream_server: _Optional[str] = ..., external_device_type: _Optional[str] = ..., external_device_sub_type: _Optional[str] = ..., organization: _Optional[str] = ..., online: bool = ..., external_id: _Optional[str] = ..., stream_type: _Optional[_Union[LiveStreamTypeEnum, str]] = ..., stream_url_predefined: bool = ...) -> None: ...

class OrganizationProtoDTO(_message.Message):
    __slots__ = ("id", "name", "description", "assets")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    assets: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., assets: _Optional[_Iterable[str]] = ...) -> None: ...

class MissionProtoDTO(_message.Message):
    __slots__ = ("id", "name", "description", "tasks", "status", "type", "geo_json", "start_date", "end_date", "assigned_assets", "created_at", "modified_at", "updated_user")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TASKS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    GEO_JSON_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_ASSETS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_USER_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    tasks: _containers.RepeatedCompositeFieldContainer[TaskProtoDTO]
    status: MissionStatus
    type: MissionType
    geo_json: str
    start_date: _timestamp_pb2.Timestamp
    end_date: _timestamp_pb2.Timestamp
    assigned_assets: _containers.RepeatedScalarFieldContainer[str]
    created_at: _timestamp_pb2.Timestamp
    modified_at: _timestamp_pb2.Timestamp
    updated_user: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., tasks: _Optional[_Iterable[_Union[TaskProtoDTO, _Mapping]]] = ..., status: _Optional[_Union[MissionStatus, str]] = ..., type: _Optional[_Union[MissionType, str]] = ..., geo_json: _Optional[str] = ..., start_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., assigned_assets: _Optional[_Iterable[str]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_user: _Optional[str] = ...) -> None: ...

class TaskProtoDTO(_message.Message):
    __slots__ = ("id", "mission_id", "created_at", "modified_at", "modified_from", "name", "description", "task_type", "config", "status", "asset_id", "sn_number", "current_progress", "current_step", "break_reason", "external_command_type", "waypoint_config", "detect_config", "area_mapping_config", "poi_config", "follow_config", "track_config")
    ID_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_FROM_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TASK_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    SN_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CURRENT_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_STEP_FIELD_NUMBER: _ClassVar[int]
    BREAK_REASON_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_COMMAND_TYPE_FIELD_NUMBER: _ClassVar[int]
    WAYPOINT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DETECT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AREA_MAPPING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    POI_CONFIG_FIELD_NUMBER: _ClassVar[int]
    FOLLOW_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TRACK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    id: str
    mission_id: str
    created_at: _timestamp_pb2.Timestamp
    modified_at: _timestamp_pb2.Timestamp
    modified_from: str
    name: str
    description: str
    task_type: str
    config: str
    status: TaskStatus
    asset_id: str
    sn_number: str
    current_progress: int
    current_step: str
    break_reason: FlighttaskBreakReasonEnumProto
    external_command_type: str
    waypoint_config: WaypointTaskConfigProto
    detect_config: DetectTaskConfigProto
    area_mapping_config: AreaMappingTaskConfigProto
    poi_config: PoiTaskConfigProto
    follow_config: FollowTaskConfigProto
    track_config: TrackTaskConfigProto
    def __init__(self, id: _Optional[str] = ..., mission_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_from: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., task_type: _Optional[str] = ..., config: _Optional[str] = ..., status: _Optional[_Union[TaskStatus, str]] = ..., asset_id: _Optional[str] = ..., sn_number: _Optional[str] = ..., current_progress: _Optional[int] = ..., current_step: _Optional[str] = ..., break_reason: _Optional[_Union[FlighttaskBreakReasonEnumProto, str]] = ..., external_command_type: _Optional[str] = ..., waypoint_config: _Optional[_Union[WaypointTaskConfigProto, _Mapping]] = ..., detect_config: _Optional[_Union[DetectTaskConfigProto, _Mapping]] = ..., area_mapping_config: _Optional[_Union[AreaMappingTaskConfigProto, _Mapping]] = ..., poi_config: _Optional[_Union[PoiTaskConfigProto, _Mapping]] = ..., follow_config: _Optional[_Union[FollowTaskConfigProto, _Mapping]] = ..., track_config: _Optional[_Union[TrackTaskConfigProto, _Mapping]] = ...) -> None: ...

class WaypointProtoDTO(_message.Message):
    __slots__ = ("latitude", "longitude", "altitude", "speed", "fly_trough", "vehicle_action", "wp_order", "gimbal_pitch")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    FLY_TROUGH_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_ACTION_FIELD_NUMBER: _ClassVar[int]
    WP_ORDER_FIELD_NUMBER: _ClassVar[int]
    GIMBAL_PITCH_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    altitude: float
    speed: float
    fly_trough: bool
    vehicle_action: VehicleAction
    wp_order: int
    gimbal_pitch: int
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., altitude: _Optional[float] = ..., speed: _Optional[float] = ..., fly_trough: bool = ..., vehicle_action: _Optional[_Union[VehicleAction, str]] = ..., wp_order: _Optional[int] = ..., gimbal_pitch: _Optional[int] = ...) -> None: ...

class SchedulerProtoDTO(_message.Message):
    __slots__ = ("id", "name", "mission_id", "task_id", "cron_expression", "active", "type", "client_time_zone", "created_at", "modified_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    CRON_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    mission_id: str
    task_id: str
    cron_expression: str
    active: bool
    type: SchedulerType
    client_time_zone: str
    created_at: _timestamp_pb2.Timestamp
    modified_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., mission_id: _Optional[str] = ..., task_id: _Optional[str] = ..., cron_expression: _Optional[str] = ..., active: bool = ..., type: _Optional[_Union[SchedulerType, str]] = ..., client_time_zone: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SchedulerProtoDTOList(_message.Message):
    __slots__ = ("scheduler_dto_list",)
    SCHEDULER_DTO_LIST_FIELD_NUMBER: _ClassVar[int]
    scheduler_dto_list: _containers.RepeatedCompositeFieldContainer[SchedulerProtoDTO]
    def __init__(self, scheduler_dto_list: _Optional[_Iterable[_Union[SchedulerProtoDTO, _Mapping]]] = ...) -> None: ...

class WaypointTaskConfigProto(_message.Message):
    __slots__ = ("flight_id", "waypoints", "fly_to_wayline_mode", "wayline_finish_action", "wayline_type", "wayline_turn_mode", "use_straight_line", "wayline_precision_type", "exit_wayline_when_rc_lost_enum", "rc_lost_action_enum", "out_of_control_action", "take_off_security_height", "rth_altitude", "rth_mode", "rth_speed", "global_speed", "global_transition_speed", "global_height", "gimbal_pitch_mode", "global_gimbal_pitch", "payload_imaging_type", "file_url", "file_md5", "flight_area_file_url", "flight_area_checksum")
    FLIGHT_ID_FIELD_NUMBER: _ClassVar[int]
    WAYPOINTS_FIELD_NUMBER: _ClassVar[int]
    FLY_TO_WAYLINE_MODE_FIELD_NUMBER: _ClassVar[int]
    WAYLINE_FINISH_ACTION_FIELD_NUMBER: _ClassVar[int]
    WAYLINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    WAYLINE_TURN_MODE_FIELD_NUMBER: _ClassVar[int]
    USE_STRAIGHT_LINE_FIELD_NUMBER: _ClassVar[int]
    WAYLINE_PRECISION_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXIT_WAYLINE_WHEN_RC_LOST_ENUM_FIELD_NUMBER: _ClassVar[int]
    RC_LOST_ACTION_ENUM_FIELD_NUMBER: _ClassVar[int]
    OUT_OF_CONTROL_ACTION_FIELD_NUMBER: _ClassVar[int]
    TAKE_OFF_SECURITY_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    RTH_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    RTH_MODE_FIELD_NUMBER: _ClassVar[int]
    RTH_SPEED_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_SPEED_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_TRANSITION_SPEED_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    GIMBAL_PITCH_MODE_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_GIMBAL_PITCH_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_IMAGING_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILE_URL_FIELD_NUMBER: _ClassVar[int]
    FILE_MD5_FIELD_NUMBER: _ClassVar[int]
    FLIGHT_AREA_FILE_URL_FIELD_NUMBER: _ClassVar[int]
    FLIGHT_AREA_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    flight_id: str
    waypoints: _containers.RepeatedCompositeFieldContainer[WaypointProtoDTO]
    fly_to_wayline_mode: FlyToWaylineModeProto
    wayline_finish_action: WaylineFinishActionProto
    wayline_type: WaylineTypeEnumProto
    wayline_turn_mode: WaylineTurnModeProto
    use_straight_line: bool
    wayline_precision_type: WaylinePrecisionTypeEnumProto
    exit_wayline_when_rc_lost_enum: ExitWaylineWhenRcLostEnumProto
    rc_lost_action_enum: RcLostActionEnumProto
    out_of_control_action: OutOfControlActionEnumProto
    take_off_security_height: float
    rth_altitude: int
    rth_mode: RthModeEnumProto
    rth_speed: float
    global_speed: float
    global_transition_speed: float
    global_height: float
    gimbal_pitch_mode: WaylineGimbalPitchModeProto
    global_gimbal_pitch: int
    payload_imaging_type: str
    file_url: str
    file_md5: str
    flight_area_file_url: str
    flight_area_checksum: str
    def __init__(self, flight_id: _Optional[str] = ..., waypoints: _Optional[_Iterable[_Union[WaypointProtoDTO, _Mapping]]] = ..., fly_to_wayline_mode: _Optional[_Union[FlyToWaylineModeProto, str]] = ..., wayline_finish_action: _Optional[_Union[WaylineFinishActionProto, str]] = ..., wayline_type: _Optional[_Union[WaylineTypeEnumProto, str]] = ..., wayline_turn_mode: _Optional[_Union[WaylineTurnModeProto, str]] = ..., use_straight_line: bool = ..., wayline_precision_type: _Optional[_Union[WaylinePrecisionTypeEnumProto, str]] = ..., exit_wayline_when_rc_lost_enum: _Optional[_Union[ExitWaylineWhenRcLostEnumProto, str]] = ..., rc_lost_action_enum: _Optional[_Union[RcLostActionEnumProto, str]] = ..., out_of_control_action: _Optional[_Union[OutOfControlActionEnumProto, str]] = ..., take_off_security_height: _Optional[float] = ..., rth_altitude: _Optional[int] = ..., rth_mode: _Optional[_Union[RthModeEnumProto, str]] = ..., rth_speed: _Optional[float] = ..., global_speed: _Optional[float] = ..., global_transition_speed: _Optional[float] = ..., global_height: _Optional[float] = ..., gimbal_pitch_mode: _Optional[_Union[WaylineGimbalPitchModeProto, str]] = ..., global_gimbal_pitch: _Optional[int] = ..., payload_imaging_type: _Optional[str] = ..., file_url: _Optional[str] = ..., file_md5: _Optional[str] = ..., flight_area_file_url: _Optional[str] = ..., flight_area_checksum: _Optional[str] = ...) -> None: ...

class DetectTaskConfigProto(_message.Message):
    __slots__ = ("detection_targets", "detection_mode", "area_latitude", "area_longitude", "area_radius", "detection_altitude", "scan_pattern", "scan_speed", "thermal_detection", "visual_detection", "min_confidence", "max_detections", "auto_capture_on_detection", "investigate_detections", "investigation_distance", "investigation_duration", "gimbal_pitch", "enable_zoom", "zoom_level", "max_duration", "on_max_detections_action", "realtime_alerts", "ai_model_id", "detection_parameters")
    class DetectionParameterProto(_message.Message):
        __slots__ = ("name", "value", "description")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: str
        description: str
        def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...
    DETECTION_TARGETS_FIELD_NUMBER: _ClassVar[int]
    DETECTION_MODE_FIELD_NUMBER: _ClassVar[int]
    AREA_LATITUDE_FIELD_NUMBER: _ClassVar[int]
    AREA_LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    AREA_RADIUS_FIELD_NUMBER: _ClassVar[int]
    DETECTION_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    SCAN_PATTERN_FIELD_NUMBER: _ClassVar[int]
    SCAN_SPEED_FIELD_NUMBER: _ClassVar[int]
    THERMAL_DETECTION_FIELD_NUMBER: _ClassVar[int]
    VISUAL_DETECTION_FIELD_NUMBER: _ClassVar[int]
    MIN_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    MAX_DETECTIONS_FIELD_NUMBER: _ClassVar[int]
    AUTO_CAPTURE_ON_DETECTION_FIELD_NUMBER: _ClassVar[int]
    INVESTIGATE_DETECTIONS_FIELD_NUMBER: _ClassVar[int]
    INVESTIGATION_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    INVESTIGATION_DURATION_FIELD_NUMBER: _ClassVar[int]
    GIMBAL_PITCH_FIELD_NUMBER: _ClassVar[int]
    ENABLE_ZOOM_FIELD_NUMBER: _ClassVar[int]
    ZOOM_LEVEL_FIELD_NUMBER: _ClassVar[int]
    MAX_DURATION_FIELD_NUMBER: _ClassVar[int]
    ON_MAX_DETECTIONS_ACTION_FIELD_NUMBER: _ClassVar[int]
    REALTIME_ALERTS_FIELD_NUMBER: _ClassVar[int]
    AI_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    DETECTION_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    detection_targets: _containers.RepeatedScalarFieldContainer[str]
    detection_mode: str
    area_latitude: float
    area_longitude: float
    area_radius: float
    detection_altitude: float
    scan_pattern: str
    scan_speed: float
    thermal_detection: bool
    visual_detection: bool
    min_confidence: float
    max_detections: int
    auto_capture_on_detection: bool
    investigate_detections: bool
    investigation_distance: float
    investigation_duration: int
    gimbal_pitch: int
    enable_zoom: bool
    zoom_level: float
    max_duration: int
    on_max_detections_action: str
    realtime_alerts: bool
    ai_model_id: str
    detection_parameters: _containers.RepeatedCompositeFieldContainer[DetectTaskConfigProto.DetectionParameterProto]
    def __init__(self, detection_targets: _Optional[_Iterable[str]] = ..., detection_mode: _Optional[str] = ..., area_latitude: _Optional[float] = ..., area_longitude: _Optional[float] = ..., area_radius: _Optional[float] = ..., detection_altitude: _Optional[float] = ..., scan_pattern: _Optional[str] = ..., scan_speed: _Optional[float] = ..., thermal_detection: bool = ..., visual_detection: bool = ..., min_confidence: _Optional[float] = ..., max_detections: _Optional[int] = ..., auto_capture_on_detection: bool = ..., investigate_detections: bool = ..., investigation_distance: _Optional[float] = ..., investigation_duration: _Optional[int] = ..., gimbal_pitch: _Optional[int] = ..., enable_zoom: bool = ..., zoom_level: _Optional[float] = ..., max_duration: _Optional[int] = ..., on_max_detections_action: _Optional[str] = ..., realtime_alerts: bool = ..., ai_model_id: _Optional[str] = ..., detection_parameters: _Optional[_Iterable[_Union[DetectTaskConfigProto.DetectionParameterProto, _Mapping]]] = ...) -> None: ...

class AreaMappingTaskConfigProto(_message.Message):
    __slots__ = ("area_vertices", "survey_altitude", "flight_pattern", "front_overlap", "side_overlap", "speed", "gimbal_pitch", "camera_angle", "terrain_following", "ground_sampling_distance", "enable3_d_reconstruction")
    class AreaVertexProto(_message.Message):
        __slots__ = ("latitude", "longitude", "order")
        LATITUDE_FIELD_NUMBER: _ClassVar[int]
        LONGITUDE_FIELD_NUMBER: _ClassVar[int]
        ORDER_FIELD_NUMBER: _ClassVar[int]
        latitude: float
        longitude: float
        order: int
        def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., order: _Optional[int] = ...) -> None: ...
    AREA_VERTICES_FIELD_NUMBER: _ClassVar[int]
    SURVEY_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    FLIGHT_PATTERN_FIELD_NUMBER: _ClassVar[int]
    FRONT_OVERLAP_FIELD_NUMBER: _ClassVar[int]
    SIDE_OVERLAP_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    GIMBAL_PITCH_FIELD_NUMBER: _ClassVar[int]
    CAMERA_ANGLE_FIELD_NUMBER: _ClassVar[int]
    TERRAIN_FOLLOWING_FIELD_NUMBER: _ClassVar[int]
    GROUND_SAMPLING_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    ENABLE3_D_RECONSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    area_vertices: _containers.RepeatedCompositeFieldContainer[AreaMappingTaskConfigProto.AreaVertexProto]
    survey_altitude: float
    flight_pattern: str
    front_overlap: int
    side_overlap: int
    speed: float
    gimbal_pitch: int
    camera_angle: int
    terrain_following: bool
    ground_sampling_distance: float
    enable3_d_reconstruction: bool
    def __init__(self, area_vertices: _Optional[_Iterable[_Union[AreaMappingTaskConfigProto.AreaVertexProto, _Mapping]]] = ..., survey_altitude: _Optional[float] = ..., flight_pattern: _Optional[str] = ..., front_overlap: _Optional[int] = ..., side_overlap: _Optional[int] = ..., speed: _Optional[float] = ..., gimbal_pitch: _Optional[int] = ..., camera_angle: _Optional[int] = ..., terrain_following: bool = ..., ground_sampling_distance: _Optional[float] = ..., enable3_d_reconstruction: bool = ...) -> None: ...

class PoiTaskConfigProto(_message.Message):
    __slots__ = ("poi_latitude", "poi_longitude", "poi_altitude", "orbit_radius", "orbit_speed", "flight_altitude", "number_of_orbits", "orbit_direction", "start_angle", "end_angle", "capture_enabled", "capture_interval", "lock_camera_on_poi")
    POI_LATITUDE_FIELD_NUMBER: _ClassVar[int]
    POI_LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    POI_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    ORBIT_RADIUS_FIELD_NUMBER: _ClassVar[int]
    ORBIT_SPEED_FIELD_NUMBER: _ClassVar[int]
    FLIGHT_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_ORBITS_FIELD_NUMBER: _ClassVar[int]
    ORBIT_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    START_ANGLE_FIELD_NUMBER: _ClassVar[int]
    END_ANGLE_FIELD_NUMBER: _ClassVar[int]
    CAPTURE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CAPTURE_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    LOCK_CAMERA_ON_POI_FIELD_NUMBER: _ClassVar[int]
    poi_latitude: float
    poi_longitude: float
    poi_altitude: float
    orbit_radius: float
    orbit_speed: float
    flight_altitude: float
    number_of_orbits: int
    orbit_direction: str
    start_angle: int
    end_angle: int
    capture_enabled: bool
    capture_interval: int
    lock_camera_on_poi: bool
    def __init__(self, poi_latitude: _Optional[float] = ..., poi_longitude: _Optional[float] = ..., poi_altitude: _Optional[float] = ..., orbit_radius: _Optional[float] = ..., orbit_speed: _Optional[float] = ..., flight_altitude: _Optional[float] = ..., number_of_orbits: _Optional[int] = ..., orbit_direction: _Optional[str] = ..., start_angle: _Optional[int] = ..., end_angle: _Optional[int] = ..., capture_enabled: bool = ..., capture_interval: _Optional[int] = ..., lock_camera_on_poi: bool = ...) -> None: ...

class FollowTaskConfigProto(_message.Message):
    __slots__ = ("target_type", "initial_latitude", "initial_longitude", "follow_distance", "relative_altitude", "max_speed", "follow_mode", "angle_offset", "obstacle_avoidance", "max_duration", "max_distance_from_start", "lost_target_action", "lost_target_timeout", "lock_camera_on_target", "gimbal_pitch_offset", "auto_capture", "capture_interval")
    TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    INITIAL_LATITUDE_FIELD_NUMBER: _ClassVar[int]
    INITIAL_LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    FOLLOW_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    MAX_SPEED_FIELD_NUMBER: _ClassVar[int]
    FOLLOW_MODE_FIELD_NUMBER: _ClassVar[int]
    ANGLE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    OBSTACLE_AVOIDANCE_FIELD_NUMBER: _ClassVar[int]
    MAX_DURATION_FIELD_NUMBER: _ClassVar[int]
    MAX_DISTANCE_FROM_START_FIELD_NUMBER: _ClassVar[int]
    LOST_TARGET_ACTION_FIELD_NUMBER: _ClassVar[int]
    LOST_TARGET_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    LOCK_CAMERA_ON_TARGET_FIELD_NUMBER: _ClassVar[int]
    GIMBAL_PITCH_OFFSET_FIELD_NUMBER: _ClassVar[int]
    AUTO_CAPTURE_FIELD_NUMBER: _ClassVar[int]
    CAPTURE_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    target_type: str
    initial_latitude: float
    initial_longitude: float
    follow_distance: float
    relative_altitude: float
    max_speed: float
    follow_mode: str
    angle_offset: int
    obstacle_avoidance: bool
    max_duration: int
    max_distance_from_start: float
    lost_target_action: str
    lost_target_timeout: int
    lock_camera_on_target: bool
    gimbal_pitch_offset: int
    auto_capture: bool
    capture_interval: int
    def __init__(self, target_type: _Optional[str] = ..., initial_latitude: _Optional[float] = ..., initial_longitude: _Optional[float] = ..., follow_distance: _Optional[float] = ..., relative_altitude: _Optional[float] = ..., max_speed: _Optional[float] = ..., follow_mode: _Optional[str] = ..., angle_offset: _Optional[int] = ..., obstacle_avoidance: bool = ..., max_duration: _Optional[int] = ..., max_distance_from_start: _Optional[float] = ..., lost_target_action: _Optional[str] = ..., lost_target_timeout: _Optional[int] = ..., lock_camera_on_target: bool = ..., gimbal_pitch_offset: _Optional[int] = ..., auto_capture: bool = ..., capture_interval: _Optional[int] = ...) -> None: ...

class TrackTaskConfigProto(_message.Message):
    __slots__ = ("target_type", "initial_latitude", "initial_longitude", "target_altitude", "tracking_mode", "max_movement_radius", "tracking_altitude", "gimbal_tracking", "auto_zoom", "zoom_level", "tracking_sensitivity", "max_duration", "lost_target_action", "lost_target_timeout", "search_pattern", "search_duration", "continuous_recording", "photo_capture", "capture_interval", "confidence_threshold")
    TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    INITIAL_LATITUDE_FIELD_NUMBER: _ClassVar[int]
    INITIAL_LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    TARGET_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    TRACKING_MODE_FIELD_NUMBER: _ClassVar[int]
    MAX_MOVEMENT_RADIUS_FIELD_NUMBER: _ClassVar[int]
    TRACKING_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    GIMBAL_TRACKING_FIELD_NUMBER: _ClassVar[int]
    AUTO_ZOOM_FIELD_NUMBER: _ClassVar[int]
    ZOOM_LEVEL_FIELD_NUMBER: _ClassVar[int]
    TRACKING_SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
    MAX_DURATION_FIELD_NUMBER: _ClassVar[int]
    LOST_TARGET_ACTION_FIELD_NUMBER: _ClassVar[int]
    LOST_TARGET_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    SEARCH_PATTERN_FIELD_NUMBER: _ClassVar[int]
    SEARCH_DURATION_FIELD_NUMBER: _ClassVar[int]
    CONTINUOUS_RECORDING_FIELD_NUMBER: _ClassVar[int]
    PHOTO_CAPTURE_FIELD_NUMBER: _ClassVar[int]
    CAPTURE_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    target_type: str
    initial_latitude: float
    initial_longitude: float
    target_altitude: float
    tracking_mode: str
    max_movement_radius: float
    tracking_altitude: float
    gimbal_tracking: bool
    auto_zoom: bool
    zoom_level: float
    tracking_sensitivity: str
    max_duration: int
    lost_target_action: str
    lost_target_timeout: int
    search_pattern: str
    search_duration: int
    continuous_recording: bool
    photo_capture: bool
    capture_interval: int
    confidence_threshold: float
    def __init__(self, target_type: _Optional[str] = ..., initial_latitude: _Optional[float] = ..., initial_longitude: _Optional[float] = ..., target_altitude: _Optional[float] = ..., tracking_mode: _Optional[str] = ..., max_movement_radius: _Optional[float] = ..., tracking_altitude: _Optional[float] = ..., gimbal_tracking: bool = ..., auto_zoom: bool = ..., zoom_level: _Optional[float] = ..., tracking_sensitivity: _Optional[str] = ..., max_duration: _Optional[int] = ..., lost_target_action: _Optional[str] = ..., lost_target_timeout: _Optional[int] = ..., search_pattern: _Optional[str] = ..., search_duration: _Optional[int] = ..., continuous_recording: bool = ..., photo_capture: bool = ..., capture_interval: _Optional[int] = ..., confidence_threshold: _Optional[float] = ...) -> None: ...
