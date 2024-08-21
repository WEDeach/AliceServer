from dataclasses import dataclass

from ..enums import BanType, EUserStatus
from ..res_base import BaseRes

@dataclass
class LoginRes(BaseRes):
    sessionId: str
    userId: int
    status: EUserStatus
    banType: BanType