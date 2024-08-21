from dataclasses import dataclass, field
from typing import List, Optional


from .clean_nightmare_info import CleanNightmareInfo
from .clean_special_background_effect_info import CleanSpecialBackgroundEffectInfo
from .subscription_info import SubscriptionInfo
from ..item.record_item_data import ItemDataRecord
from ..user.record_user_data import UserDataRecord
from ..res_base import BaseRes


@dataclass
class CleanCheckRes(BaseRes):
    success: bool = field(default=True)
    message: str = field(default="")
    cleaningType: int = field(default=1)
    itemDataList: List[ItemDataRecord] = field(default_factory=list)
    remainingSecond: int = field(default=0)
    userData: Optional[UserDataRecord] = field(default=None)
    isRoyalUser: bool = field(default=False)
    cleanItemMstId: int = field(default=1424)
    cleanItemNum: int = field(default=0)
    cleanNightmareInfo: CleanNightmareInfo = field(default=CleanNightmareInfo(
        assetBundleName="clean_enemy_spine_prefab/01",
        resourceName="clean_enemy_spine_prefab_01",
    ))
    cleanSpecialBackgroundEffectInfo: CleanSpecialBackgroundEffectInfo = field(default=CleanSpecialBackgroundEffectInfo(
        assetBundleName="",
        resourceName="",
        effectRateInfo=None
    ))
    navigatorTalkMstId: int = field(default=0)
    cleanSpecialSceneName: str = field(default="")
    subscriptionInfo: SubscriptionInfo = field(default=SubscriptionInfo())
    isSubscriptionGold: bool = field(default=False)
    isSubscriptionSilver: bool = field(default=False)
    subscriptionText: str = field(default="")

    IsCanShowSubscriptionButton: bool = field(default=True)
    IsSubscriptionValid: bool = field(default=False)

    @staticmethod
    def get(userId: int):
        user_data = UserDataRecord.get(userId)
        items = [
            ItemDataRecord(
                itemDataId=0,
                userId=userId,
                itemMstId=10,
                num=0,
                createdTime=0,
                updatedTime=0,
            )
        ]

        # TODO: fetch data
        return CleanCheckRes(
            userData=user_data,
            itemDataList=items
        )
