from dataclasses import dataclass, field

from ..record_base import BaseRecord


@dataclass
class CampaignListRecord(BaseRecord):
    questAreaMstId: int = field(default=0)
    campaignType: int = field(default=0)
    campaignValue: float = field(default=0.0)
    remainTime: int = field(default=0)
    everydayEndTime: int = field(default=0)
