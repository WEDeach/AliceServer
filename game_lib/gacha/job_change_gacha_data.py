from dataclasses import dataclass, field
from typing import List, Optional

from .job_change_gacha_series_data import JobChangeGachaSeriesData
from ..record_base import BaseRecord


@dataclass
class JobChangeGachaData(BaseRecord):
    bannerMstId: Optional[int] = field(default=0)
    startTime: Optional[int] = field(default=0)
    endTime: Optional[int] = field(default=0)
    jobChangeGachaSeriesMstList: Optional[List[JobChangeGachaSeriesData]] = field(
        default=None
    )
    CanDraw: Optional[bool] = field(default=False)
    CanDrawTomorrow: Optional[bool] = field(default=False)
