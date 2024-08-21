from dataclasses import dataclass, field

from ..record_base import BaseRecord


@dataclass
class FixedDeckInfo(BaseRecord):
    enable: bool = field(default=False)
    deckName: str = field(default="")
    characterMstId: int = field(default=0)
    totalPower: int = field(default=0)
    fireCardNum: int = field(default=0)
    waterCardNum: int = field(default=0)
    windCardNum: int = field(default=0)
