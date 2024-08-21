from dataclasses import dataclass, field
from typing import Optional

from ..record_base import BaseRecord


@dataclass
class JobChangeGachaSeriesData(BaseRecord):
    gachaSeriesMstId: Optional[int] = field(default=0)
    weaponType: Optional[int] = field(default=0)
    endTime: Optional[int] = field(default=0)
    canDrawToday: Optional[bool] = field(default=False)
    canDrawTomorrow: Optional[bool] = field(default=False)
