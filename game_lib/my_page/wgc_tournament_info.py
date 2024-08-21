from dataclasses import dataclass

from ..record_base import BaseRecord


@dataclass
class WgcTournamentInfo(BaseRecord):
    isShowWgcTournamentButton: bool
    isShowWgcTournamentButtonBadge: bool
