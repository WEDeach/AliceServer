from dataclasses import dataclass, field

from ..record_base import BaseRecord


@dataclass
class NavigatorTalkRes(BaseRecord):
    isNavigatorTalk: bool = field(default=False)
    navigatorTalkMstId: int = field(default=0)
