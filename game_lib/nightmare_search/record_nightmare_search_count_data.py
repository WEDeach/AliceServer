from dataclasses import dataclass

from ..record_base import BaseRecord


@dataclass
class NightmareSearchCountDataRecord(BaseRecord):
    nightmareSearchButtonType: int
    nightmareSearchCount: int
