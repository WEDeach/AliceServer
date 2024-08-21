from dataclasses import dataclass, field

from ..record_base import BaseRecord


@dataclass
class QuestRankupResultDataRecord(BaseRecord):
    beforeLevel: int = field(default=0)
    afterLevel: int = field(default=0)
    beforeDeckCardNum: int = field(default=0)
    afterDeckCardNum: int = field(default=0)
    beforeDeckCost: int = field(default=0)
    afterDeckCost: int = field(default=0)
    beforeWeaponSubDeckCardNum: int = field(default=0)
    afterWeaponSubDeckCardNum: int = field(default=0)
    beforeProtectorSubDeckCardNum: int = field(default=0)
    afterProtectorSubDeckCardNum: int = field(default=0)
    beforeNightmareSubDeckCardNum: int = field(default=0)
    afterNightmareSubDeckCardNum: int = field(default=0)
