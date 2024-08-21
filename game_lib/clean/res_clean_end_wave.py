from dataclasses import dataclass, field

from .cleaning_wave_data import CleaningWaveData
from .req_clean_end_wave import CleanEndWaveReq
from ..res_base import BaseRes


@dataclass
class CleanEndWaveRes(BaseRes):
    cleaningWaveData: CleaningWaveData = field(default=CleaningWaveData())

    @staticmethod
    def get(req: CleanEndWaveReq):
        r = CleanEndWaveRes()

        r.cleaningWaveData.nextWave = req.currentWave + 1
        return r
