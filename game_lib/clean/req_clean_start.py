from dataclasses import dataclass

from ..req_base import BaseReq


@dataclass
class CleanStartReq(BaseReq):
    cleaningType: int
