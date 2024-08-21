from dataclasses import dataclass

from ..gacha.res_gacha_exec import GachaExecRes
from ..res_base import BaseRes


@dataclass
class TutorialGachaExecRes(BaseRes):
    gachaExecRes: GachaExecRes
    nextTutorialMstId: int
