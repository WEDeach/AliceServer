from typing import Optional
from dataclasses import dataclass, field

from ..record_base import BaseRecord


@dataclass
class DeckDetailDataRecord(BaseRecord):
    deckDetailDataId: Optional[int] = field(default=0)
    deckDataId: Optional[int] = field(default=0)
    cardDataId: Optional[int] = field(default=0)
    cardType: Optional[int] = field(default=0)
    frontSkillMstId: Optional[int] = field(default=0)
    backSkillMstId: Optional[int] = field(default=0)
    autoSkillMstId: Optional[int] = field(default=0)
    questSkillMstId: Optional[int] = field(default=0)
    protectorSkillMstId: Optional[int] = field(default=0)
    limitBreakSkillMstId: Optional[int] = field(default=0)
    isSubDeck: Optional[bool] = field(default=False)
    position: Optional[int] = field(default=0)
    isActivatedLimitBreakSkill: Optional[bool] = field(default=False)
