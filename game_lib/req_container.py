from dataclasses import dataclass
from .req_base import BaseReq
from typing import Any, Dict, Generic, Optional, Type, TypeVar, Union
import msgpack

T = TypeVar("T", bound=BaseReq)


@dataclass
class ReqContainer(BaseReq, Generic[T]):
    uuid: str
    userId: int
    sessionId: str
    actionToken: str
    ctag: str
    actionTime: int
    payload: Union[T, None] = None

    @classmethod
    def unwrap(cls, data: bytes, payload_type: Optional[Type[T]] = None):
        """Unwarp request data."""
        m = msgpack.unpackb(data, use_list=True, raw=False)
        r = cls(**m)
        p: Optional[Dict[str, Any]] = m.get("payload")
        if p is not None and payload_type is not None:
            r.payload = payload_type.from_dict(p)
        return r
