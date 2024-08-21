from dataclasses import dataclass, field
from typing import Optional

from ..user.record_user_data import UserDataRecord
from ..res_base import BaseRes


@dataclass
class SetCharacterRes(BaseRes):
    success: Optional[bool] = field(default=False)
    message: Optional[str] = field(default="")
    userData: Optional[UserDataRecord] = field(default=None)
