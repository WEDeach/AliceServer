from dataclasses import dataclass
from .res_base import BaseRes

@dataclass
class ResError(BaseRes):
    domain: str
    code: int
    field: str
    reason: str