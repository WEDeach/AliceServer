from dataclasses import dataclass
from typing import List

from .record_gacha_data import GachaDataRecord
from .record_gacha_pickup_data import GachaPickupDataRecord
from .record_gacha_series_data import GachaSeriesDataRecord
from ..res_base import BaseRes


@dataclass
class GetTutorialGachaTopRes(BaseRes):
    gachaSeriesList: List[GachaSeriesDataRecord]
    gachaList: List[GachaDataRecord]
    gachaPickupList: List[GachaPickupDataRecord]
