from dataclasses import dataclass, field

from ..res_base import BaseRes


@dataclass
class CleaningResultData(BaseRes):
    getTotalAp: int = field(default=0)
    beforeAp: int = field(default=30)
    beforeMaxAp: int = field(default=30)
    afterAp: int = field(default=30)
    afterMaxAp: int = field(default=30)
    beforeLevel: int = field(default=1)
    afterLevel: int = field(default=1)
    beforeDeckCardNum: int = field(default=5)
    afterDeckCardNum: int = field(default=5)
    beforeDeckCost: int = field(default=100)
    afterDeckCost: int = field(default=100)
    beforeSubDeckCardNum: int = field(default=10)
    afterSubDeckCardNum: int = field(default=10)
    getTotalExp: int = field(default=0)
    getTotalEnemyDown: int = field(default=69)
