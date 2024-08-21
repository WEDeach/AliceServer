from dataclasses import dataclass, field

from ..record_base import BaseRecord


@dataclass
class RelationshipConfig(BaseRecord):
    relationshipNum: int = field(default=0)
    maxFollowerNum: int = field(default=0)
    maxBlockNum: int = field(default=0)
