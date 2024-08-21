from dataclasses import dataclass, field
from typing import List

from .record_item_data import ItemDataRecord
from ..res_base import BaseRes


@dataclass
class ItemDataListRes(BaseRes):
    itemDataList: List[ItemDataRecord] = field(default_factory=list)
