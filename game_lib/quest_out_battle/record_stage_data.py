from dataclasses import dataclass, field

from ..record_base import BaseRecord


@dataclass
class StageDataRecord(BaseRecord):
    questStageId: int = field(default=0)
    stageStatus: int = field(default=0)
    clearRewardObjectType: int = field(default=0)
    clearRewardObjectId: int = field(default=0)
    clearRewardNum: int = field(default=0)
    isStageRewardComplete: bool = field(default=False)
    hasGotFirstReward: bool = field(default=False)
    totalPowerThreshold: int = field(default=0)
    isLimitCountQuest: bool = field(default=False)
    limitCountRestNum: int = field(default=0)
    limitCountEndTime: int = field(default=0)
    questUseStamina: int = field(default=0)
    questBaseStamina: int = field(default=0)
    isAp1Campaign: bool = field(default=False)
