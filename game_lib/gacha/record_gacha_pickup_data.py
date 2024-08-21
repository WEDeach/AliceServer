from dataclasses import dataclass, field
from typing import List, Optional

from ..record_base import BaseRecord
from ...utils.shared import AliceShared


@dataclass
class GachaPickupDataRecord(BaseRecord):
    gachaPickupMstId: Optional[int] = field(default=0)
    gachaGroupId: Optional[int] = field(default=0)
    gachaSeriesMstId: Optional[int] = field(default=0)

    @staticmethod
    def fetch_datas(
        gachaPickupMstId: Optional[int] = None, gachaSeriesMstId: Optional[int] = None
    ):
        db = AliceShared.get_database()
        mst = db.get_mst_table("gacha_pickup")
        res: List[GachaPickupDataRecord] = []
        for i in mst:
            if (
                i["gachaPickupMstId"] == gachaPickupMstId
                or i["gachaSeriesMstId"] == gachaSeriesMstId
            ):
                res.append(
                    GachaPickupDataRecord(
                        gachaPickupMstId=i["gachaPickupMstId"],
                        gachaSeriesMstId=i["gachaSeriesMstId"],
                    )
                )
        return res
