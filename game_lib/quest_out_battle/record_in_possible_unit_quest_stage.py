from dataclasses import dataclass, field

from ..record_base import BaseRecord


@dataclass
class InPossibleUnitQuestStageRecord(BaseRecord):
    questStageMstId: int = field(default=0)
    questDataId: int = field(default=0)
    termsType1: int = field(default=0)
    termsType2: int = field(default=0)
    termsType3: int = field(default=0)
    termsType4: int = field(default=0)
    termsType5: int = field(default=0)
    termsType6: int = field(default=0)
    termsType7: int = field(default=0)
    termsType8: int = field(default=0)
    termsType9: int = field(default=0)
    termsType10: int = field(default=0)
    termsType11: int = field(default=0)
