from dataclasses import dataclass, field

from ..record_base import BaseRecord


@dataclass
class QuestAreaMovieDataRecord(BaseRecord):
    canShowNoticeMovie: bool = field(default=False)
    canShowIntroductionMovie: bool = field(default=False)
    movieResourceMstId: int = field(default=0)
