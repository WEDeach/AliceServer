from dataclasses import dataclass

from ..req_base import BaseReq


@dataclass
class GetBonusDeckReq(BaseReq):
    questAreaMstId: int
    questStageMstId: int
