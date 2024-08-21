from dataclasses import dataclass

from ..record_base import BaseRecord


@dataclass
class ScratchGachaInfo(BaseRecord):
    scratchGachaDataId: int
    transitionType: int
