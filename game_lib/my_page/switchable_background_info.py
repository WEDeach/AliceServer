from typing import List, Optional
from dataclasses import dataclass, field

from .background_info import BackgroundInfo
from ..record_base import BaseRecord


@dataclass
class SwitchableBackgroundInfo(BaseRecord):
    backgroundInfoList: Optional[List[BackgroundInfo]] = field(default=None)
    isForceBackground: Optional[bool] = field(default=False)
    forceBackgroundId: Optional[int] = field(default=None)
    forceBackgroundPopupMessage: Optional[str] = field(default=None)
