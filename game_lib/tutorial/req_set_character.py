from dataclasses import dataclass
from ..req_base import BaseReq


@dataclass
class SetCharacterReq(BaseReq):
    characterMstId: int
