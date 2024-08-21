from dataclasses import dataclass
from typing import Optional

from ..res_base import BaseRes


@dataclass
class GetUserQuestDesirePhaseNoRes(BaseRes):
    phaseNo: Optional[int] = None
