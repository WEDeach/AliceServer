from dataclasses import dataclass, field

from ..record_base import BaseRecord


@dataclass
class ImpossibleQuestAreaListRecord(BaseRecord):
    questAreaMstId: int = field(default=0)
    termsType: int = field(default=0)
    termsValue: int = field(default=0)
    termsDate: int = field(default=0)
    isClear: bool = field(default=False)
