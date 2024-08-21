from dataclasses import dataclass
from ..req_base import BaseReq


@dataclass
class SetUserNameReq(BaseReq):
    userName: str
