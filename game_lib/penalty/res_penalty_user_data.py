from dataclasses import dataclass
from typing import Optional

from .record_penalty_user_data import PenaltyUserDataRecord
from ..res_base import BaseRes


@dataclass
class PenaltyUserDataRes(BaseRes):
    penaltyUserData: Optional[PenaltyUserDataRecord] = None
