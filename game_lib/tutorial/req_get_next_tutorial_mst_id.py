from dataclasses import dataclass
from ..req_base import BaseReq

@dataclass
class GetNextTutorialMstIdReq(BaseReq):
    currentTutorialMstId: int