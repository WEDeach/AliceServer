from typing import Optional
from dataclasses import dataclass, field

from ..record_base import BaseRecord


@dataclass
class DeckListRecord(BaseRecord):
    deckDataId: Optional[int] = field(default=0)
    deckName: Optional[str] = field(default="")
    isGvg: Optional[bool] = field(default=False)
    deckCardNum: Optional[int] = field(default=0)
    fireCardNum: Optional[int] = field(default=0)
    waterCardNum: Optional[int] = field(default=0)
    windCardNum: Optional[int] = field(default=0)
    totalDeckCost: Optional[int] = field(default=0)
    totalAttack: Optional[int] = field(default=0)
    totalDefence: Optional[int] = field(default=0)
