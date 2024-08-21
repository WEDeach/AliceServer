from dataclasses import dataclass, field
from typing import List, Optional

from .job_change_gacha_data import JobChangeGachaData
from .record_costume_param import CostumeParamRecord
from .record_gacha_detail_log import GachaDetailLogRecord
from .record_multi_gacha_animation_param import MultiGachaAnimationParamRecord
from .record_single_gacha_animation_param import SingleGachaAnimationParamRecord
from ..character.record_character_data import CharacterDataRecord
from ..item.record_item_data import ItemDataRecord
from ..res_base import BaseRes
from ..user.record_user_data import UserDataRecord


@dataclass
class GachaExecRes(BaseRes):
    singleGachaAnimationParam: Optional[SingleGachaAnimationParamRecord] = field(
        default=None
    )
    multiGachaAnimationParam: Optional[MultiGachaAnimationParamRecord] = field(
        default=MultiGachaAnimationParamRecord()
    )
    costumeParam: CostumeParamRecord = field(default=CostumeParamRecord())
    gachaDetailLog: Optional[List[GachaDetailLogRecord]] = field(default=None)
    characterDataList: Optional[List[CharacterDataRecord]] = field(default=None)
    userData: Optional[UserDataRecord] = field(default=None)
    itemDataList: Optional[List[ItemDataRecord]] = field(default=None)
    jobChangeGachaData: Optional[JobChangeGachaData] = field(default=None)
    gachaMstId: Optional[int] = field(default=0)
    drawTotalCount: Optional[int] = field(default=0)
    drawDailyCount: Optional[int] = field(default=0)
    loopRemainCount: Optional[int] = field(default=0)
    repeatCount: Optional[int] = field(default=0)
    isReviewPromotion: Optional[bool] = field(default=False)
    step: Optional[int] = field(default=0)
    gachaStepUpLapBonusMstId: Optional[int] = field(default=0)
    gachaStepUpLapBonusReleaseCharacterMstId: Optional[int] = field(default=0)
    gachaCountBonusMstId: Optional[int] = field(default=0)
    gachaCountBonusReleaseCharacterMstId: Optional[int] = field(default=0)
    ItemData: Optional[ItemDataRecord] = field(default=None)
    isCollectionGachaComplete: Optional[bool] = field(default=False)
