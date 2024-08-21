from dataclasses import dataclass
from typing import List

from .record_mst_version_summary import MstVersionSummaryRecord
from ..res_base import BaseRes


@dataclass
class MstVersionRes(BaseRes):
    lastMstVersionCreatedTime: int
    lastCreatedTime: str
    mstVersionSummaryList: List[MstVersionSummaryRecord]
