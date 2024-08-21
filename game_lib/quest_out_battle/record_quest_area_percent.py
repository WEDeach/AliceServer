from dataclasses import dataclass, field

from ..record_base import BaseRecord


@dataclass
class QuestAreaPercentRecord(BaseRecord):
    characterUniqueId: int = field(default=0)
    characterOrderNo: int = field(default=0)
    questAreaType: int = field(default=0)
    questAreaNo: int = field(default=0)
    questAreaMstId: int = field(default=0)
    stageTotal: int = field(default=0)
    stageClear: int = field(default=0)
    stagePercent: int = field(default=0)
    missionTotal: int = field(default=0)
    missionClear: int = field(default=0)
    missionPercent: int = field(default=0)
    isCampaign: bool = field(default=False)
    areaStatus: int = field(default=0)
