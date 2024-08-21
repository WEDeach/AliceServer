from dataclasses import dataclass, field

from ..record_base import BaseRecord


@dataclass
class QuestAreaCharacterPercentRecord(BaseRecord):
    characterUniqueId: int = field(default=0)
    stageTotal: int = field(default=0)
    stageClear: int = field(default=0)
    stagePercent: int = field(default=0)
    missionTotal: int = field(default=0)
    missionClear: int = field(default=0)
    missionPercent: int = field(default=0)
