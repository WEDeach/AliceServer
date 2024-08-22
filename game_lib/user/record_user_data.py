from dataclasses import dataclass, field
from typing import Optional

from ..record_base import BaseRecord


@dataclass
class UserDataRecord(BaseRecord):
    userId: Optional[int] = None
    name: Optional[str] = field(default="")
    playerId: Optional[int] = None
    comment: Optional[str] = field(default="")
    currentCharacterMstId: Optional[int] = field(default=1)
    currentJobRoleType: Optional[int] = field(default=5)
    currentJobMstId: Optional[int] = field(default=5)
    currentCostumeMstId: Optional[int] = field(default=1)
    currentUserTitleMstId: Optional[int] = field(default=0)
    currentTotalPower: Optional[int] = field(default=0)
    gvgCharacterMstId: Optional[int] = field(default=1)
    gameStatus: Optional[int] = field(default=0)
    level: Optional[int] = field(default=1)
    leaderCardMstId: Optional[int] = field(default=0)
    deckCost: Optional[int] = field(default=100)
    maxCard: Optional[int] = field(default=100)
    maxProtector: Optional[int] = field(default=50)
    maxNightMare: Optional[int] = field(default=50)
    maxOtherCard: Optional[int] = field(default=500)
    maxStorageCard: Optional[int] = field(default=100)
    maxStorageProtector: Optional[int] = field(default=50)
    maxStorageNightMare: Optional[int] = field(default=50)
    maxStorageOtherCard: Optional[int] = field(default=100)
    maxItem: Optional[int] = field(default=0)
    maxFriend: Optional[int] = field(default=0)
    favoriteAkbMember1: Optional[int] = field(default=0)
    favoriteAkbMember2: Optional[int] = field(default=0)
    favoriteAkbMember3: Optional[int] = field(default=0)
    isFrontRowChange: Optional[bool] = field(default=True)
    isGameMaster: Optional[int] = field(default=0)
    exp: Optional[int] = field(default=0)
    stamina: Optional[int] = field(default=20)
    staminaMax: Optional[int] = field(default=30)
    staminaUpdatedTime: Optional[int] = None
    gvgWin: Optional[int] = field(default=0)
    gvgLose: Optional[int] = field(default=0)
    gvgDraw: Optional[int] = field(default=0)
    gvgWinning: Optional[int] = field(default=0)
    gvgMaxWinning: Optional[int] = field(default=0)
    money: Optional[int] = field(default=0)
    characterPoint: Optional[int] = field(default=0)
    lastAccessTime: Optional[int] = None
    recentLoginTime: Optional[str] = field(default="很久以前")
    maxDeckNum: Optional[int] = field(default=15)
    maxDeckCardNum: Optional[int] = field(default=5)
    maxSubDeckCardNum: Optional[int] = field(default=10)
    maxMainLimitBreakSkill: Optional[int] = field(default=0)
    maxSubLimitBreakSkill: Optional[int] = field(default=0)
    maxSupportJob: Optional[int] = field(default=0)
    cleaningUpdatedTime: Optional[int] = field(default=0)
    cleaningStatus: Optional[int] = field(default=0)
    createdTime: Optional[int] = field(default=0)
    additionalDeckNum: Optional[int] = field(default=0)
    goldRoyalCardWeaponAdd: Optional[int] = field(default=0)
    goldRoyalCardProtectorAdd: Optional[int] = field(default=0)
    goldRoyalCardNightMareAdd: Optional[int] = field(default=0)
    goldRoyalVaildTime: Optional[int] = field(default=0)
    subscriptionGoldWeaponAdd: Optional[int] = field(default=0)
    subscriptionGoldProtectorAdd: Optional[int] = field(default=0)
    subscriptionGoldNightMareAdd: Optional[int] = field(default=0)
    subscriptionGoldVaildTime: Optional[int] = field(default=0)
    subscriptionSilverWeaponAdd: Optional[int] = field(default=0)
    subscriptionSilverProtectorAdd: Optional[int] = field(default=0)
    subscriptionSilverNightMareAdd: Optional[int] = field(default=0)
    subscriptionSilverVaildTime: Optional[int] = field(default=0)

    @staticmethod
    def get(uid: int):
        if uid == 700001:
            return UserDataRecord(
                userId=uid,
                name="",
                playerId=100117793,
                comment="",
                isGameMaster=1,
                gameStatus=10,
                lastAccessTime=0,
                currentCharacterMstId=1,
                currentTotalPower=0,
                createdTime=1780000000,
                stamina=30,
                staminaUpdatedTime=1780000000,
                cleaningUpdatedTime=0,
                goldRoyalVaildTime=0,
                subscriptionGoldVaildTime=0,
                subscriptionSilverVaildTime=0,
            )
        raise IndexError(f"UserDataRecord not found: {uid}")
