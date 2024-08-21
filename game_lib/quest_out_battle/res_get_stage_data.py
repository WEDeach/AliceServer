from dataclasses import dataclass, field
from typing import List, Optional

from .stand_by_job_limitation_data import StandByJobLimitationData

from .fixed_deck_info import FixedDeckInfo

from .record_quest_unit_card_bonus_reward import QuestUnitCardBonusRewardRecord

from ..deck.record_deck_list import DeckListRecord

from .record_campaign_list import CampaignListRecord

from .record_drop_reward_list import DropRewardListRecord

from .record_stage_next_reward import StageNextRewardRecord

from .record_stage_data import StageDataRecord

from ..res_base import BaseRes


@dataclass
class GetStageDataRes(BaseRes):
    stageData: StageDataRecord
    stageNextReward: Optional[StageNextRewardRecord] = field(default=None)
    dropRewardList: List[DropRewardListRecord] = field(default_factory=list)
    campaignList: List[CampaignListRecord] = field(default_factory=list)
    deckList: List[DeckListRecord] = field(default_factory=list)
    cardBonusRewardList: List[QuestUnitCardBonusRewardRecord] = field(
        default_factory=list
    )
    fixedDeckInfo: Optional[FixedDeckInfo] = field(default=None)
    enableSkipCount: int = field(default=0)
    cannotSkipText: str = field(default="")
    skipValidTime: int = field(default=0)
    jobLimitationList: List[StandByJobLimitationData] = field(default_factory=list)

    @staticmethod
    def get(questStageMstId: int, questDataId: int = 0):
        r = GetStageDataRes(
            stageData=StageDataRecord(
                questStageId=questStageMstId,
                stageStatus=1
            )
        )

        return r