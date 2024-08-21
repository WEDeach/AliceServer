from dataclasses import dataclass
from ..req_base import BaseReq

@dataclass
class UserDataReq(BaseReq):
    userId: int