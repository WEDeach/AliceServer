from dataclasses import dataclass
from ..req_base import BaseReq

@dataclass
class LoginReq(BaseReq):
    appVersion: str
    urlParam: str
    deviceModel: str
    osType: int
    osVersion: str
    storeType: int
    graphicsDeviceId: int
    graphicsDeviceVendorId: int
    processorCount: int
    processorType: str
    supportedRenderTargetCount: int
    supports3DTextures: bool
    supportsAccelerometer: bool
    supportsComputeShaders: bool
    supportsGyroscope: bool
    supportsImageEffects: bool
    supportsInstancing: bool
    supportsLocationService: bool
    supportsRenderTextures: bool
    supportsRenderToCubemap: bool
    supportsShadows: bool
    supportsSparseTextures: bool
    supportsStencil: int
    supportsVibration: bool
    uuid: str
    xuid: int