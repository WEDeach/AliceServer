from dataclasses import dataclass, field
from typing import List, Optional

from ..mst.record_alice_quest_story_mst import AliceQuestStoryMstRecord
from ..mst.record_mst_version_summary import MstVersionSummaryRecord
from ..res_base import BaseRes


@dataclass
class GetScenarioStoryMstRes(BaseRes):
    aliceQuestStoryMstList: List[AliceQuestStoryMstRecord] = field(default_factory=list)
    mstVersionSummary: Optional[MstVersionSummaryRecord] = field(default=None)

    @staticmethod
    def get(storyIndex: int, storyNo: int):
        r = GetScenarioStoryMstRes()

        r.aliceQuestStoryMstList = AliceQuestStoryMstRecord.fetch(storyIndex, storyNo)
        r.mstVersionSummary = MstVersionSummaryRecord.get(40)

        return r
