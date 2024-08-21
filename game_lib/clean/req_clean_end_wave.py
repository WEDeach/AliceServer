from dataclasses import dataclass

from ..req_base import BaseReq


@dataclass
class CleanEndWaveReq(BaseReq):
    remainTime: int
    currentWave: int
    getAp: int
    getExp: int
    getEnemyDown: int
