from dataclasses import dataclass, field
from typing import Optional

from ..record_base import BaseRecord


@dataclass
class GachaDetailLogRecord(BaseRecord):
    gachaDetailLogId: Optional[int] = field(default=0)
    userId: Optional[int] = field(default=0)
    gachaLogId: Optional[int] = field(default=0)
    presentDataId: Optional[int] = field(default=0)
    objectId: Optional[int] = field(default=0)
    objectRarity: Optional[int] = field(default=0)
    objectDataId: Optional[int] = field(default=0)
    medalNum: Optional[int] = field(default=0)
    isNew: Optional[int] = field(default=0)
    isChanceUp: Optional[int] = field(default=0)
    createdTime: Optional[int] = field(default=0)
    releaseCharacterMstId: Optional[int] = field(default=0)
    isNewCharacter: Optional[bool] = field(default=False)
    isLevelMax: Optional[bool] = field(default=False)
