from dataclasses import dataclass, field
from typing import Optional

from .gvg_watching_info import GvgWatchingInfo
from ..record_base import BaseRecord


@dataclass
class CurrentGvgScheduleValue(BaseRecord):
    _type: int = field(metadata={"json_key": "type"})
    classNo: int
    eveTime: int
    startTime: int
    endTime: int
    gvgWatchingInfo: Optional[GvgWatchingInfo]
    forceNormalUI: bool
    isAllowedGvgTournamentPush: bool
