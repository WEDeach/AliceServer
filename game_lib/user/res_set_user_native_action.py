from dataclasses import dataclass

from ..res_base import BaseRes


@dataclass
class SetUserNativeActionRes(BaseRes):
    success: bool
