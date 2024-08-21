from typing import Optional
from dataclasses import dataclass, field

from .record_guild_user_config_data import GuildUserConfigDataRecord
from .record_guild_user_data import GuildUserDataRecord
from ..record_base import BaseRecord
from ..user.record_user_data import UserDataRecord


@dataclass
class GuildMemberInfo(BaseRecord):
    userData: Optional[UserDataRecord] = field(default=None)
    guildUserData: Optional[GuildUserDataRecord] = field(default=None)
    guildUserConfigData: Optional[GuildUserConfigDataRecord] = field(default=None)
    totalPower: Optional[int] = field(default=None)
    maxHp: Optional[int] = field(default=None)
    bestLevel: Optional[int] = field(default=None)
    bestTotalPower: Optional[int] = field(default=None)
