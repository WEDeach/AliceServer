from dataclasses import dataclass, field
from typing import List, Optional

from ..record_base import BaseRecord
from ...utils.shared import AliceShared


@dataclass
class GachaDataRecord(BaseRecord):
    gachaMstId: Optional[int] = field(default=0)
    gachaGroupId: Optional[int] = field(default=0)
    gachaSeriesMstId: Optional[int] = field(default=0)
    drawTotalCount: Optional[int] = field(default=0)
    drawDailyCount: Optional[int] = field(default=0)
    loopRemainCount: Optional[int] = field(default=0)
    minCost: Optional[int] = field(default=0)
    recycleMinRarity: Optional[int] = field(default=0)
    gachaType: Optional[int] = field(default=0)
    isCollectionComplete: Optional[bool] = field(default=False)
    isFirstMinRarity: Optional[bool] = field(default=False)

    @staticmethod
    def fetch_datas(gachaMstId: int):
        db = AliceShared.get_database()
        mst = db.get_mst_table("gacha")
        res: List[GachaDataRecord] = []
        for i in mst:
            if i["gachaMstId"] == gachaMstId:
                res.append(
                    GachaDataRecord(
                        gachaMstId=i["gachaMstId"],
                        gachaSeriesMstId=i["gachaSeriesMstId"],
                        gachaType=i["gachaType"],
                    )
                )
        return res
