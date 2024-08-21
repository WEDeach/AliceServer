from dataclasses import dataclass, field

from ..res_base import BaseRes


@dataclass
class CleaningDeckData(BaseRes):
    characterMstId: int = field(default=1)
    cardMstId: int = field(default=587)
