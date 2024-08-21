from dataclasses import dataclass, field
from typing import List


from .record_deck_data import DeckDataRecord
from ..character_board.record_character_board_bonus_data_list import (
    CharacterBoardBonusDataListRecord,
)
from ..user.user_character_bonus_data import UserCharacterBonusData
from ..res_base import BaseRes


@dataclass
class DeckDataListRes(BaseRes):
    deckDataList: List[DeckDataRecord] = field(default_factory=list)
    userCharacterBonusData: UserCharacterBonusData = field(
        default=UserCharacterBonusData()
    )
    characterBoardBonusDataList: List[CharacterBoardBonusDataListRecord] = field(
        default_factory=list
    )
    
    @staticmethod
    def get(uid: int):
        r = DeckDataListRes()

        # TODO: fetch user decks
        r.deckDataList.append(DeckDataRecord(
            deckDataId=1,
            userId=uid,
            deckName="TEST DECK",
            characterDataId=1,
            deckType=1,
            isGvg=True,
            isQuest=True,
            deckCardNum=1,
            maxDeckCardNum=5,
            waterCardNum=1,
            totalDeckCost=16,
            totalAttack=686,
            vsFireTotalAttack=1710,
            vsWaterTotalAttack=1368,
            vsWindTotalAttack=1096,
            totalDefence=448,
            vsFireTotalDefence=1120,
            vsWaterTotalDefence=896,
            vsWindTotalDefence=718,
            totalPower=1134,
            attackTotalPower=454,
            magicAttackTotalPower=232,
            defenceTotalPower=268,
            magicDefenceTotalPower=180,
            maxHp=1000
        ))
        return r
