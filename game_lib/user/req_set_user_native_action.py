from dataclasses import dataclass, field
from ..req_base import BaseReq


@dataclass
class SetUserNativeActionReq(BaseReq):
    _type: int = field(metadata={"json_key": "type"})
    value: int
