from dataclasses import dataclass, field

from ..record_base import BaseRecord


@dataclass
class StandByJobLimitationData(BaseRecord):
    questStageJobLimitationMstId: int = field(default=0)
    instrument: int = field(default=0)
    grimoire: int = field(default=0)
    stick: int = field(default=0)
    sword: int = field(default=0)
    hammer: int = field(default=0)
    gun: int = field(default=0)
    spear: int = field(default=0)
