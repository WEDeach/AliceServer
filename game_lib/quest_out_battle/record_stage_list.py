from dataclasses import dataclass, field
from typing import List

from ..record_base import BaseRecord
from ...utils.shared import AliceShared


@dataclass
class StageListRecord(BaseRecord):
    questAreaMstId: int = field(default=0)
    questStageMstId: int = field(default=0)
    stageStatus: int = field(default=0)
    stageBossEnemyId: int = field(default=0)
    stageBossResourceName: str = field(default="")
    stageBossIconResourceName: str = field(default="")
    stageBossAssetBundleName: str = field(default="")
    stageBossAttribute: int = field(default=0)
    clearRewardObjectType: int = field(default=0)
    clearRewardObjectId: int = field(default=0)
    clearRewardNum: int = field(default=0)
    questLevel: int = field(default=0)
    questUseStamina: int = field(default=0)
    questBaseStamina: int = field(default=0)
    isAp1Campaign: bool = field(default=False)
    hasGotFirstReward: bool = field(default=False)
    clearCount: int = field(default=0)
    stampRewardNum: int = field(default=0)
    nextQuestStageRewardMstId: int = field(default=0)
    isCanSkipQuest: bool = field(default=False)
    skippedCount: int = field(default=0)
    maxEnableSkipCount: int = field(default=0)

    @staticmethod
    def fetch_datas(questAreaMstId: int):
        db = AliceShared.get_database()
        ts = db.get_mst_table("quest_stage")
        res: List[StageListRecord] = []
        for t in ts:
            if t["questAreaMstId"] == questAreaMstId:
                res.append(
                    StageListRecord(
                        questAreaMstId=t["questAreaMstId"],
                        questStageMstId=t["questStageMstId"],
                        stageStatus=1 if t["level"] == 1 else 9,
                        stageBossEnemyId=203,
                        stageBossAssetBundleName="enemy/3",
                        stageBossAttribute=2,
                        clearRewardObjectType=t["objectType"],
                        clearRewardObjectId=t["objectId"],
                        clearRewardNum=t["num"],
                        questUseStamina=t["useStamina"],
                        questBaseStamina=t["useStamina"],
                        questLevel=t["level"],
                    )
                )
        return res
