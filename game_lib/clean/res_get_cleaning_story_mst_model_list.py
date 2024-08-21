from dataclasses import dataclass, field
from typing import List

from ..mst.record_cleaning_story_mst import CleaningStoryMstRecord
from ..res_base import BaseRes


@dataclass
class GetCleaningStoryMstModelListRes(BaseRes):
    mstList: List[CleaningStoryMstRecord] = field(default_factory=list)

    @staticmethod
    def get(characterUniqueId: int):
        r = GetCleaningStoryMstModelListRes()

        # TODO: FETCH CLEAN STORYS.
        return r