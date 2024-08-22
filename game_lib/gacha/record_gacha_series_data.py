from dataclasses import dataclass, field
from typing import List, Optional

from ..record_base import BaseRecord
from ...utils.shared import AliceShared


@dataclass
class GachaSeriesDataRecord(BaseRecord):
    gachaSeriesMstId: Optional[int] = field(default=0)
    gachaGroupId: Optional[int] = field(default=0)
    bannerMstId: Optional[int] = field(default=0)
    lapLimit: Optional[int] = field(default=0)
    definitionText: Optional[str] = field(default=None)
    cueSheetName: Optional[str] = field(default=None)
    cueName: Optional[str] = field(default=None)
    isShowMedalButton: Optional[bool] = field(default=False)
    definitionText1: Optional[str] = field(default=None)
    definitionText2: Optional[str] = field(default=None)
    definitionText3: Optional[str] = field(default=None)
    definitionText4: Optional[str] = field(default=None)
    definitionText5: Optional[str] = field(default=None)

    @staticmethod
    def fetch(gachaSeriesMstId: int):
        db = AliceShared.get_database()
        mst = db.get_mst_table("gacha_series")
        res: List[GachaSeriesDataRecord] = []
        for i in mst:
            if i["gachaSeriesMstId"] == gachaSeriesMstId:
                res.append(
                    GachaSeriesDataRecord(
                        gachaSeriesMstId=i["gachaSeriesMstId"],
                        gachaGroupId=i["gachaGroupId"],
                        bannerMstId=i["bannerMstId"],
                        definitionText="definitionText",
                    )
                )
        return res
