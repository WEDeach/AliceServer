from dataclasses import dataclass, field

from ..res_base import BaseRes


@dataclass
class CleaningRematchInfo(BaseRes):
    isShowRematchButton: bool = field(default=True)
    isNeedTicket: bool = field(default=False)
    ticketNum: int = field(default=0)
    IsCanRematch: bool = field(default=True)
    IsShowTicketNum: bool = field(default=False)
