from dataclasses import dataclass, field
from typing import List, Optional


from .record_impossible_quest_area_list import ImpossibleQuestAreaListRecord
from .record_quest_area_character_percent import QuestAreaCharacterPercentRecord
from .record_quest_area_movie_data import QuestAreaMovieDataRecord
from .record_quest_area_percent import QuestAreaPercentRecord
from ..res_base import BaseRes
from ...utils.shared import AliceShared


@dataclass
class GetAreaMapListRes(BaseRes):
    questMapMstId: int = field(default=0)
    isHardView: bool = field(default=False)
    enableForceAreaRelease: int = field(default=False)
    questAreaPercent: List[QuestAreaPercentRecord] = field(default_factory=list)
    questAreaCharacterPercent: List[QuestAreaCharacterPercentRecord] = field(
        default_factory=list
    )
    questMovieData: Optional[QuestAreaMovieDataRecord] = field(default=None)
    impossibleQuestAreaList: List[ImpossibleQuestAreaListRecord] = field(
        default_factory=list
    )

    @staticmethod
    def get(questMapMstId: int):
        r = GetAreaMapListRes(questMapMstId=questMapMstId)

        # TODO: fetch user quest status.
        # TEST INIT DATA.
        db = AliceShared.get_database()
        mst_aqag = db.get_mst_table("alice_quest_area_group")
        mst_qs = db.get_mst_table("quest_stage")
        character_uids = []
        for aqag in mst_aqag:
            if aqag['questMapMstId'] == questMapMstId:
                if aqag['characterUniqueId'] not in character_uids:
                    character_uids.append(aqag['characterUniqueId'])
                r.questAreaPercent.append(QuestAreaPercentRecord(
                    characterUniqueId=aqag['characterUniqueId'],
                    characterOrderNo=aqag['characterOrderNo'],
                    questAreaType=aqag['questAreaType'],
                    questAreaNo=aqag['questAreaNo'],
                    questAreaMstId=aqag['questAreaMstId'],
                    areaStatus=1 if aqag['questAreaNo'] == 1 else 9
                ))
        for character_uid in character_uids:
            r.questAreaCharacterPercent.append(QuestAreaCharacterPercentRecord(
                characterUniqueId=character_uid,
                stageTotal=100,
            ))
        return r
