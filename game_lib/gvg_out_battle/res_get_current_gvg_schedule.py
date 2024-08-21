from dataclasses import asdict, dataclass, field
from typing import Optional

from .current_gvg_schedule_value import CurrentGvgScheduleValue
from ..res_base import BaseRes


@dataclass
class GetCurrentGvgScheduleRes(BaseRes):
    currentGvgSchedule: Optional[CurrentGvgScheduleValue] = field(default=None)
