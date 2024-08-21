from dataclasses import dataclass, field
from typing import List


from .record_boost_item import BoostItemRecord
from .record_can_use_boost_item import CanUseBoostItemRecord
from ..res_base import BaseRes


@dataclass
class GetBoostItemRes(BaseRes):
    boostItemList: List[BoostItemRecord] = field(default_factory=list)
    canUseBoostItemList: List[CanUseBoostItemRecord] = field(default_factory=list)
