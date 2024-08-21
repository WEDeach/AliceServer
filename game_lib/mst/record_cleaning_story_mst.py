from dataclasses import dataclass, field

from ..record_base import BaseRecord


@dataclass
class CleaningStoryMstRecord(BaseRecord):
    cleaningStoryMstId: int = field(default=0)
    characterUniqueId: int = field(default=0)
    storyType: int = field(default=0)
    storyStartTime: int = field(default=0)
    storyEndTime: int = field(default=0)
    storyText: str = field(default="")
    storyViewTime: int = field(default=0)
    assetBundleName: str = field(default="")
    thumbResourceName: str = field(default="")
    thumbPosition: int = field(default=0)
    voiceQueueSheet: str = field(default="")
    voiceQueueName: str = field(default="")
    refineCharacterMstId: int = field(default=0)
    rate: int = field(default=0)
    createdTime: int = field(default=0)
