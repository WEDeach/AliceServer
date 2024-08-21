from dataclasses import dataclass, field
from typing import List

from .record_get_quest_calendar import GetQuestCalendarRecord
from ..res_base import BaseRes


@dataclass
class GetQuestCalendarMstDataRes(BaseRes):
    questCalendarMstDataList: List[GetQuestCalendarRecord] = field(default_factory=list)
    beforeQuestCalendarMstDataList: List[GetQuestCalendarRecord] = field(
        default_factory=list
    )
