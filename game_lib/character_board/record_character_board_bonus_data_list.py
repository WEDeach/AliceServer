from typing import Optional
from dataclasses import dataclass, field

from ..record_base import BaseRecord


@dataclass
class CharacterBoardBonusDataListRecord(BaseRecord):
    characterUniqueId: Optional[int] = field(default=0)
    hpCharacterBonus: Optional[int] = field(default=0)
    attackCharacterBonus: Optional[int] = field(default=0)
    magicAttackCharacterBonus: Optional[int] = field(default=0)
    defenceCharacterBonus: Optional[int] = field(default=0)
    magicDefenceCharacterBonus: Optional[int] = field(default=0)
    gvgSpReductionLevel: Optional[int] = field(default=0)
    questSpReductionLevel: Optional[int] = field(default=0)
