from typing import Optional
from dataclasses import dataclass, field

from ..record_base import BaseRecord


@dataclass
class MstVersionSummaryRecord(BaseRecord):
    mstTableId: int
    version: int
