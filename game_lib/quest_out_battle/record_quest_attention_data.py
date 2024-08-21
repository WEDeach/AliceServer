from dataclasses import dataclass, field

from ..record_base import BaseRecord


@dataclass
class QuestAttentionDataRecord(BaseRecord):
    isUnitQuest: bool = field(default=False)
    isEventGuerrillaQuest: bool = field(default=False)
    campaignText: str = field(default="")
    isRaidOpen: bool = field(default=False)
    isRaidEncounting: bool = field(default=False)
