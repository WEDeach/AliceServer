from dataclasses import dataclass, field
from typing import List

from ..res_base import BaseRes


@dataclass
class GetBonusDeckRes(BaseRes):
    deckDataIdList: List[int] = field(default_factory=list)

    @staticmethod
    def get(questAreaMstId: int, questStageMstId: int):
        r = GetBonusDeckRes()

        # TODO: fetch user bouns deck ids

        return r
