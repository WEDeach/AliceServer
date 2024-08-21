from dataclasses import dataclass, field
from typing import List

from .record_deck_detail_data import DeckDetailDataRecord
from .record_support_job_data import SupportJobDataRecord
from ..res_base import BaseRes


@dataclass
class DeckDetailDataListRes(BaseRes):
    deckDetailDataList: List[DeckDetailDataRecord] = field(default_factory=list)
    supportJobList: List[SupportJobDataRecord] = field(default_factory=list)

    @staticmethod
    def get(deckDataId: int):
        r = DeckDetailDataListRes()

        # TODO: fetch user deck details
        r.deckDetailDataList.append(
            DeckDetailDataRecord(
                deckDetailDataId=1,
                deckDataId=deckDataId,
                cardDataId=1,
                cardType=1,
            )
        )
        return r
