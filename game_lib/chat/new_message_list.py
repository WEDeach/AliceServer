from dataclasses import dataclass

from ..record_base import BaseRecord


@dataclass
class NewMessageList(BaseRecord):
    roomId: int
    roomType: int
    lastMessageId: int
