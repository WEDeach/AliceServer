from dataclasses import dataclass, field
from typing import List, Optional

from .record_stamp_next_reward import StampNextRewardRecord
from .record_stamp_reward import StampRewardRecord
from ..res_base import BaseRes


@dataclass
class GetStageRewardRes(BaseRes):
    questStageMstId: int = field(default=0)
    clearCount: int = field(default=0)
    completeStatus: bool = field(default=False)
    stampRewardList: List[StampRewardRecord] = field(default_factory=list)
    stampNextReward: Optional[StampNextRewardRecord] = field(default=None)

    @staticmethod
    def get(questStageMstId: int):
        r = GetStageRewardRes(
            questStageMstId = questStageMstId,
        )

        # TODO: fetch stage rewards.

        return r
