from dataclasses import dataclass

from ..record_base import BaseRecord


@dataclass
class GachiColosseumInfo(BaseRecord):
    penaltyDateTime: int
    penaltyPopupTitle: str
    penaltyPopupBody: str
    penaltyPopupValue: str
