from dataclasses import dataclass, field

from ..record_base import BaseRecord


@dataclass
class QuestOutBattleEffectRecord(BaseRecord):
    doReleaseNewArea: bool = field(default=False)
    doReleaseNewMap: bool = field(default=False)
    doReleaseUnitRelease: bool = field(default=False)
    doReleaseEventRelease: bool = field(default=False)
    doEnergySavingTutorial: bool = field(default=False)
    doRankUp: bool = field(default=False)
    doStageFirstClear: bool = field(default=False)
    doMissionComplete: bool = field(default=False)
    doNoticeMovie: bool = field(default=False)
    doNoticeMovieMstId: int = field(default=0)
