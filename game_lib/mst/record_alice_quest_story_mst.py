from dataclasses import dataclass, field

from ..record_base import BaseRecord


@dataclass
class AliceQuestStoryMstRecord(BaseRecord):
    questStoryMstId: int = field(default=0)
    storyIndex: int = field(default=0)
    storyNo: int = field(default=0)
    storyType: int = field(default=0)
    positionX: int = field(default=0)
    positionY: int = field(default=0)
    direction: int = field(default=0)
    isFin: int = field(default=0)
    storyText: str = field(default="")
    assetBundleName: str = field(default="")
    bgResourceName: str = field(default="")
    assetBundleName1: str = field(default="")
    bgResourceName1: str = field(default="")
    assetBundleName2: str = field(default="")
    bgResourceName2: str = field(default="")
    bgmQueueSheet: str = field(default="")
    bgmQueueName: str = field(default="")
    voiceQueueSheet: str = field(default="")
    voiceQueueName: str = field(default="")
    createdTime: int = field(default=0)
