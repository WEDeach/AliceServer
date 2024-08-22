from dataclasses import dataclass

from ..record_base import BaseRecord
from ...database import MstTableVersions


@dataclass
class MstVersionSummaryRecord(BaseRecord):
    mstTableId: int
    version: int

    @staticmethod
    def get(mstTableId: int):
        r = MstVersionSummaryRecord(mstTableId, 0)

        for i in MstTableVersions:
            if i["mstTableId"] == mstTableId:
                r = MstVersionSummaryRecord(**i)
                break
        return r
