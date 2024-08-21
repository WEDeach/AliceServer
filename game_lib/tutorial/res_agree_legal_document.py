from dataclasses import dataclass
from ..res_base import BaseRes

@dataclass
class AgreeLegalDocumentRes(BaseRes):
    success: bool
    message: str