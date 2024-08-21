from dataclasses import dataclass, field

from ..guild.guild_item_info import GuildItemInfo
from ..record_base import BaseRecord


@dataclass
class GveInfo(BaseRecord):
    guildItemInfo: GuildItemInfo = field(default=GuildItemInfo())
    isRaidBossExist: bool = field(default=False)
