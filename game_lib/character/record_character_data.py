from dataclasses import dataclass
from ..record_base import BaseRecord


@dataclass
class CharacterDataRecord(BaseRecord):
    characterDataId: int
    characterMstId: int
    userId: int
    level: int
    maxLevel: int
    exp: int
    limitBreakCount: int
    openedStoryStep: int
    isDeleted: bool
    createdTime: int
    isJobAwakening: bool
