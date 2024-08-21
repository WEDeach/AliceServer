from dataclasses import dataclass

from ..req_base import BaseReq


@dataclass
class GetTutorialResultReq(BaseReq):
    questStageMstId: int
    characterMstId: int
