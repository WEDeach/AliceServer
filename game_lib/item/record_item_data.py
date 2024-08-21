from typing import Optional
from dataclasses import dataclass, field

from ..record_base import BaseRecord


@dataclass
class ItemDataRecord(BaseRecord):
    itemDataId: Optional[int] = field(default=0)
    userId: Optional[int] = field(default=0)
    itemMstId: Optional[int] = field(default=0)
    num: Optional[int] = field(default=0)
    createdTime: Optional[int] = field(default=0)
    updatedTime: Optional[int] = field(default=0)
    description: Optional[str] = field(default=None)
