from dataclasses import dataclass, field

from ..record_base import BaseRecord


@dataclass
class QuestMissionRecord(BaseRecord):
    questStageMstId: int = field(default=0)
    questMissionMstId: int = field(default=0)
    isClear: bool = field(default=False)
