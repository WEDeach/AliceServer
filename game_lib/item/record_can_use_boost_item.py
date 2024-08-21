from dataclasses import dataclass

from ..record_base import BaseRecord


@dataclass
class CanUseBoostItemRecord(BaseRecord):
    itemMstId: int
