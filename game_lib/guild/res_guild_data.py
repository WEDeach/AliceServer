from dataclasses import dataclass, field
from typing import List, Optional

from .record_guild_data import GuildDataRecord
from ..res_base import BaseRes


@dataclass
class GuildDataRes(BaseRes):
    guildData: Optional[GuildDataRecord] = field(default=None)
    # guildOwnData: GuildOwnDataRecord
    # myGuildUserConfigData: GuildUserConfigDataRecord
    # gvgEventRankingData: GvgEventRankingDataRecord
    # guildShipData: GuildShipDataRecord
    # guildShipPickup: List[GuildShipPickupRecord]
