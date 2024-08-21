from dataclasses import dataclass

from ..record_base import BaseRecord


@dataclass
class MountainEvent(BaseRecord):
    startTime: int
    endTime: int
    mypageBackgroundEffectId: int
    mypageMiniTutorialId: int
    clearNormalStageNo: int
