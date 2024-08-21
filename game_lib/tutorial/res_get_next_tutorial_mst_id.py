from dataclasses import dataclass
from ..res_base import BaseRes

@dataclass
class GetNextTutorialMstIdRes(BaseRes):
    nextTutorialMstId: int