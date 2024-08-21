from typing import Optional
from dataclasses import dataclass, field
from ..record_base import BaseRecord


@dataclass
class GuildUserConfigDataRecord(BaseRecord):
    guildUserConfigDataId: Optional[int] = field(default=None)
    userId: Optional[str] = field(default=None)
    rearguardGvgTimeType: Optional[str] = field(default=None)
    invitationGvgJoinType: Optional[int] = field(default=None)
    invitationGuildRankType: Optional[int] = field(default=None)
    invitationActionType: Optional[int] = field(default=None)
    invitationGvgTimeType: Optional[int] = field(default=None)
    isInvitationSearch: Optional[bool] = field(default=False)
