from dataclasses import dataclass
from typing import Optional

from ..value_base import BaseValue


@dataclass
class AttentionResourceDownloadValue(BaseValue):
    enable: bool
    lowerLimitSize: int
    popupMessage:  Optional[str]
    popupMessageWhenReleaseGuild: Optional[str]
