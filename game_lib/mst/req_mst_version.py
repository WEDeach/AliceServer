from dataclasses import dataclass
from typing import List

from .record_mst_version_summary import MstVersionSummaryRecord
from ..req_base import BaseReq


@dataclass
class MstVersionReq(BaseReq):
    mstVersionSummaryList: List[MstVersionSummaryRecord]
