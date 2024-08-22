from dataclasses import dataclass, field
from typing import List

from .record_default_reward import DefaultRewardRecord
from .record_enemy_reward import EnemyRewardRecord
from .record_quest_card_bonus_reward import QuestCardBonusRewardRecord
from .record_quest_friend import QuestFriendRecord
from .record_quest_mission import QuestMissionRecord
from .record_quest_mission_complete_reward import QuestMissionCompleteRewardRecord
from .record_quest_mission_reward import QuestMissionRewardRecord
from .record_quest_out_battle_effect import QuestOutBattleEffectRecord
from .record_quest_rankup_result_data import QuestRankupResultDataRecord
from .record_quest_result_data import QuestResultDataRecord
from .record_stage_join_reward import StageJoinRewardRecord
from .record_stage_reward import StageRewardRecord
from .record_stage_round_reward import StageRoundRewardRecord
from .relationship_config import RelationshipConfig
from .res_fixed_deck_info import FixedDeckInfoRes
from ..res_base import BaseRes
from ..user.record_user_data import UserDataRecord


@dataclass
class GetResultRes(BaseRes):
    resultData: QuestResultDataRecord = field(default=QuestResultDataRecord())
    relationshipInfo: RelationshipConfig = field(default=RelationshipConfig())
    defaultReward: DefaultRewardRecord = field(default=DefaultRewardRecord())
    enemyReward: List[EnemyRewardRecord] = field(default_factory=list)
    stageRoundReward: List[StageRoundRewardRecord] = field(default_factory=list)
    stageReward: List[StageRewardRecord] = field(default_factory=list)
    stageJoinReward: List[StageJoinRewardRecord] = field(default_factory=list)
    questMissionReward: List[QuestMissionRewardRecord] = field(default_factory=list)
    questMissionList: List[QuestMissionRecord] = field(default_factory=list)
    questMissionCompleteReward: List[QuestMissionCompleteRewardRecord] = field(
        default_factory=list
    )
    cardBonusReward: List[QuestCardBonusRewardRecord] = field(default_factory=list)
    friendRelationshipDataRecordList: List[QuestFriendRecord] = field(
        default_factory=list
    )
    userData: UserDataRecord = field(init=False)
    effectList: QuestOutBattleEffectRecord = field(default=QuestOutBattleEffectRecord())
    rankupResultData: QuestRankupResultDataRecord = field(
        default=QuestRankupResultDataRecord()
    )
    fixedDeckInfo: FixedDeckInfoRes = field(default=FixedDeckInfoRes())
    appearedRaidBossMovieResourceMstId: int = field(default=0)
    isRareRaid: bool = field(default=False)
    enableSkipCount: int = field(default=0)
    cannotSkipText: str = field(default="")
    skipValidTime: int = field(default=0)
    isRarisRentalPlayBattleeRaid: bool = field(default=False)
    enableWebView: bool = field(default=False)

    @staticmethod
    def get_by_tutorial(questStageMstId: int, characterMstId: int):
        r = GetResultRes()

        # TODO: fetch data for tutorial.
        r.resultData.questStageMstId = questStageMstId
        r.resultData.characterMstId = characterMstId
        r.defaultReward.exp = 6
        r.defaultReward.expBefore = 0
        r.defaultReward.expAfter = 6
        r.defaultReward.levelBefore = 1
        r.defaultReward.levelAfter = 1
        r.rankupResultData.beforeLevel = 1
        r.rankupResultData.afterLevel = 1
        r.userData = UserDataRecord.get(700001)

        return r
