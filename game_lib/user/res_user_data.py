from dataclasses import dataclass

from .record_user_data import UserDataRecord
from ..res_base import BaseRes

@dataclass
class UserDataRes(BaseRes):
    userData: UserDataRecord