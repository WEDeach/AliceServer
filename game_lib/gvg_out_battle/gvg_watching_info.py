from dataclasses import dataclass

from ..record_base import BaseRecord


@dataclass
class GvgWatchingInfo(BaseRecord):
    firestoreShardId: int
    battleNum: int
    gvgDataId: int
