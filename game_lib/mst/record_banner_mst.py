from dataclasses import dataclass

from ..record_base import BaseRecord


@dataclass
class BannerMstRecord(BaseRecord):
    bannerMstId: int
    type: int
    startTime: int
    endTime: int
    priority: int
    transitionSceneName: str
    objectId: int
    announceMstId: int
    osType: int
    isBeginner: bool
    assetBundleName: str
    resourceName: str
    badgeAssetBundleName: str
    badgeResourceName: str
    badgeEndTime: int
    optionType: int
    isDeleted: bool
    createdTime: int
