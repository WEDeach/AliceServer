from dataclasses import dataclass, field

from ..record_base import BaseRecord


@dataclass
class StageJoinRewardRecord(BaseRecord):
    objectType: int = field(default=0)
    objectId: int = field(default=0)
    num: int = field(default=0)
    isNew: bool = field(default=False)
