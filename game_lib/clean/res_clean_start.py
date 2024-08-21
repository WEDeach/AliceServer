from dataclasses import dataclass, field
from typing import List, Optional

from .cleaning_deck_data import CleaningDeckData
from .cleaning_wave_data import CleaningWaveData
from ..item.record_item_data import ItemDataRecord
from ..user.record_user_data import UserDataRecord
from ..res_base import BaseRes


@dataclass
class CleanStartRes(BaseRes):
    cleaningWaveData: CleaningWaveData = field(default=CleaningWaveData())
    cleaningDeckData: CleaningDeckData = field(default=CleaningDeckData())
    itemDataList: List[ItemDataRecord] = field(default_factory=list)
    userData: Optional[UserDataRecord] = field(default=None)
    staminaOverRecover: int = field(default=3)
