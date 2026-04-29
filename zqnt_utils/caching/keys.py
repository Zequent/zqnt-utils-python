"""
CacheKeys – mirrors com.zqnt.utils.caching.CacheKeys.

Key patterns use ``{placeholder}`` syntax; call ``.build(**kwargs)`` to
substitute placeholders::

    key = CacheKeys.EDGE_ENDPOINTS.build(vendor="DJI")
    # → "edge-endpoints:DJI"

    key = CacheKeys.ASSET_ACTIVE_TASKS.build(sn="DOCK001", taskId="task-1")
    # → "asset-active-tasks:DOCK001:task-1"
"""

from enum import Enum


class CacheKeys(Enum):
    ASSET_ONLINE                    = "asset-online:"
    ASSET_MODE                      = "asset-mode:"
    ASSET_TELEMETRY                 = "asset-telemetry:"
    SUBASSET_TELEMETRY              = "subasset-telemetry:"
    ASSET_MANUAL_CONTROL_STATE      = "drc-state:"
    ASSET_LIVE_STREAM_STATE         = "live-stream-state:"
    ASSET_SERVICES_REPLY_WAIT       = "asset-task-reply-wait:{tid}:{method}"
    ASSET_ACTIVE_TASKS              = "asset-active-tasks:{sn}:{taskId}"
    ASSET_COMPLETED_TASKS           = "asset-completed-tasks:{sn}:{taskId}"
    ASSET_TASK_EXTERNAL_ID_REFERENCE = "asset-task-external-id-reference:{externalId}:{sn}"
    ASSET_MANUAL_CONTROL_REQUEST    = "asset-manual-control-request:"
    SUBASSET_AT_HOME                = "subaset-at-home:"   # intentional typo – matches Java
    ASSET_SUBASSET_REFERENCE        = "asset-subasset-reference:"
    ASSET_PROPERTIES                = "asset-properties:"
    ASSET_DTO                       = "asset-dto:{sn}"
    SUBASSET_DTO                    = "subasset-dto:{subAssetSn}"
    EDGE_ENDPOINTS                  = "edge-endpoints:{vendor}"
    EDGE_VENDOR                     = "edge-vendor:{sn}"

    def build(self, **kwargs: str) -> str:
        """
        Return the final Redis key with all placeholders replaced.

        Simple keys (no placeholders) can be called without arguments;
        the trailing ``:`` is kept intentionally — append the id yourself::

            CacheKeys.ASSET_TELEMETRY.build() + device_sn
            # → "asset-telemetry:DOCK001"
        """
        return self.value.format(**kwargs)
