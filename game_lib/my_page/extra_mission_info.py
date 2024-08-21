from typing import List, Optional
from dataclasses import dataclass, field

from ..record_base import BaseRecord


@dataclass
class ExtraMissionInfo(BaseRecord):
    extraMissionEventId: Optional[int] = field(default=None)
    achievedExtraMissionMstIdList: Optional[List[int]] = field(default=None)
    progressingExtraMissionMstId: Optional[int] = field(default=None)
