from dataclasses import dataclass, field

from ..record_base import BaseRecord


@dataclass
class GetQuestCalendarRecord(BaseRecord):
    questCalendarMstId: int = field(default=0)
    bannerMstId: int = field(default=0)
    startTime: int = field(default=0)
    endTime: int = field(default=0)
    announceMstId: int = field(default=0)
    priority: int = field(default=0)
    assetBundleName: str = field(default="")
    resourceName: str = field(default="")
    isNotification: bool = field(default=False)
