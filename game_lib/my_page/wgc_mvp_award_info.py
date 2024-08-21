from dataclasses import dataclass

from .watching_info import WatchingInfo
from ..record_base import BaseRecord


@dataclass
class WgcMvpAwardInfo(BaseRecord):
    isShowMvpButton: bool
    isWinGuild: bool
    mvpAwardStartTime: int
    watchingInfo: WatchingInfo
