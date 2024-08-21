from dataclasses import dataclass, field

from ..record_base import BaseRecord


@dataclass
class QuestFriendRecord(BaseRecord):
    userId: int = field(default=0)
    name: str = field(default="")
    characterMstId: int = field(default=0)
    characterLevel: int = field(default=0)
    leaderCardMstId: int = field(default=0)
    level: int = field(default=0)
    jobRoleType: int = field(default=0)
    totalPower: int = field(default=0)
    fireCardNum: int = field(default=0)
    waterCardNum: int = field(default=0)
    windCardNum: int = field(default=0)
    darkCardNum: int = field(default=0)
    lightCardNum: int = field(default=0)
    lastAccessTime: int = field(default=0)
    relationship: str = field(default="")
    isGuild: bool = field(default=False)
    userType: int = field(default=0)
    questNpcMstId: int = field(default=0)
    questTotalPower: int = field(default=0)
