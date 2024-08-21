from dataclasses import dataclass, field
from typing import List, Optional

from .gve_info import GveInfo
from .navigator_talk_res import NavigatorTalkRes
from .record_campaign_list import CampaignListRecord
from .record_in_possible_unit_quest_stage import InPossibleUnitQuestStageRecord
from .record_quest_mission import QuestMissionRecord
from .record_stage_list import StageListRecord
from ..res_base import BaseRes


@dataclass
class GetAliceStageListRes(BaseRes):
    questAreaMstId: int = field(default=0)
    specialCharacterAbilityMstId: int = field(default=0)
    stageList: List[StageListRecord] = field(default_factory=list)
    questMissionList: List[QuestMissionRecord] = field(default_factory=list)
    campaignList: List[CampaignListRecord] = field(default_factory=list)
    inPossibleQuestStageList: List[InPossibleUnitQuestStageRecord] = field(
        default_factory=list
    )
    isHardView: bool = field(default=False)
    boostCharacterName: str = field(default="")
    navigatorTalkRes: NavigatorTalkRes = field(default=NavigatorTalkRes())
    itemCount: int = field(default=0)
    gveInfo: Optional[GveInfo] = field(default=None)

    @staticmethod
    def get(questAreaMstId: int, battleNum: Optional[int], prisonRangeId: int):
        r = GetAliceStageListRes(
            questAreaMstId=questAreaMstId,
        )

        # TODO: fetch quest stage datas.
        r.stageList = StageListRecord.fetch_datas(questAreaMstId)

        return r
