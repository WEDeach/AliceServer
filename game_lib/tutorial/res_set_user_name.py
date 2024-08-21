from dataclasses import dataclass

from ..user.record_user_data import UserDataRecord
from ..res_base import BaseRes


@dataclass
class SetUserNameRes(BaseRes):
    success: bool
    message: str
    userData: UserDataRecord
