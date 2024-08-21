from dataclasses import dataclass, field

from ..record_base import BaseRecord


@dataclass
class GuildItemInfo(BaseRecord):
    useItemMstId: int = field(default=0)
    guildItemNum: int = field(default=0)
