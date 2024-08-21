from dataclasses import dataclass, field

from ..record_base import BaseRecord


@dataclass
class StageNextRewardRecord(BaseRecord):
    questStageMstId: int = field(default=0)
    objectType: int = field(default=0)
    objectId: int = field(default=0)
    num: int = field(default=0)
    isLast: bool = field(default=False)
