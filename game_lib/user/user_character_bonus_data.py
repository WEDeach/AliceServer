from typing import Optional
from dataclasses import dataclass, field
from ..record_base import BaseRecord


@dataclass
class UserCharacterBonusData(BaseRecord):
    hpCharacterBonus: Optional[int] = field(default=0)
    hpArtBonus: Optional[int] = field(default=0)
    attackCharacterBonus: Optional[int] = field(default=0)
    magicAttackCharacterBonus: Optional[int] = field(default=0)
    attackArtBonus: Optional[int] = field(default=0)
    defenceCharacterBonus: Optional[int] = field(default=0)
    magicDefenceCharacterBonus: Optional[int] = field(default=0)
    defenceArtBonus: Optional[int] = field(default=0)
    deckCostBonus: Optional[int] = field(default=0)
