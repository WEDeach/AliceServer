from dataclasses import dataclass, field

from ..res_base import BaseRes


@dataclass
class FixedDeckInfoRes(BaseRes):
    enable: bool = field(default=False)
    characterMstId: int = field(default=0)
