from dataclasses import dataclass

from ..req_base import BaseReq


@dataclass
class CleanEndReq(BaseReq):
    remainTime: int
    currentWave: int
    getAp: int
    getExp: int
    getEnemyDown: int
