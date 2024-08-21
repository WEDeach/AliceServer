from dataclasses import dataclass
from ..res_base import BaseRes

@dataclass
class CancelLatestRes(BaseRes):
    result: str