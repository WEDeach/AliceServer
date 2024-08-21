from typing import Optional
from dataclasses import dataclass, field

from ..record_base import BaseRecord


@dataclass
class SwitchableBgmInfo(BaseRecord):
    id: Optional[int] = field(default=None)
    cueSheetName: Optional[str] = field(default=None)
    cueName: Optional[str] = field(default=None)
