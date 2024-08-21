from dataclasses import dataclass
from ..req_base import BaseReq


@dataclass
class GetStageRewardReq(BaseReq):
    questStageMstId: int
