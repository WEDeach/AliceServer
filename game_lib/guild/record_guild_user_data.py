from typing import Optional
from dataclasses import dataclass, field
from ..record_base import BaseRecord


@dataclass
class GuildUserDataRecord(BaseRecord):
    userId: Optional[int] = field(default=None)
    guildDataId: Optional[str] = field(default=None)
    guildPoint: Optional[str] = field(default=None)
    guildRoleMstId: Optional[int] = field(default=None)
    joinTime: Optional[int] = field(default=None)
    updatedTime: Optional[int] = field(default=None)
    createdTime: Optional[int] = field(default=None)
    language: Optional[str] = field(default=None)
