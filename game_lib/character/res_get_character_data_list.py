from dataclasses import dataclass, field
from typing import List, Optional

from .record_character_data import CharacterDataRecord
from ..res_base import BaseRes


@dataclass
class GetCharacterDataListRes(BaseRes):
    characterDataList: Optional[List[CharacterDataRecord]] = field(default_factory=list)
    maxJobLevelTotal: Optional[int] = field(default=0)
