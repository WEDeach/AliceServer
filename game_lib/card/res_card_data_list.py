from dataclasses import dataclass, field
from typing import List

from .record_card_data import CardDataRecord
from ..res_base import BaseRes


@dataclass
class CardDataListRes(BaseRes):
    cardDataList: List[CardDataRecord] = field(default_factory=list)

    @staticmethod
    def get(uid: int):
        r = CardDataListRes()

        # TODO: fetch user cards
        r.cardDataList.append(
            CardDataRecord(
                cardDataId=1,
                cardMstId=587,
                level=1,
                levelupExp=10,
                frontSkillMstId=991,
                isDeck=True,
            )
        )
        return r
