from dataclasses import dataclass

from ..record_base import BaseRecord


@dataclass
class WatchingInfo(BaseRecord):
    battleNum: int
    gvgDataId: int
    fireShardId: int
    winWgcGuildDataId: int
