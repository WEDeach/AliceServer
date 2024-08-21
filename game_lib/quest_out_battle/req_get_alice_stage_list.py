from dataclasses import dataclass
from ..req_base import BaseReq


@dataclass
class GetAliceStageListReq(BaseReq):
    questAreaMstId: int
    battleNum: int
    tabType: int
    rangeId: int
