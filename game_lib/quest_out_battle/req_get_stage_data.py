from dataclasses import dataclass
from ..req_base import BaseReq


@dataclass
class GetStageDataReq(BaseReq):
    questStageMstId: int
    questDataId: int
    tabType: int
