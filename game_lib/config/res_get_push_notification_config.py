from dataclasses import dataclass, field

from ..res_base import BaseRes


@dataclass
class GetPushNotificationConfigRes(BaseRes):
    isNotification: bool = field(default=False)
    isGvgNotification: bool = field(default=False)
    isGvcNotification: bool = field(default=False)
    isEventNotification: bool = field(default=False)
    isGuerrillaNotification: bool = field(default=False)
    isCleaningNotification: bool = field(default=False)
    isStaminaNotification: bool = field(default=False)
    isDirectChatNotification: bool = field(default=False)
    isGroupChatNotification: bool = field(default=False)
    isNightmareSearchNotification: bool = field(default=False)
    isRoyalUserServiceNotification: bool = field(default=False)
    isGainPresentAutoSale: bool = field(default=False)
    isGainPresentAutoSaleRarityB: bool = field(default=False)
    isGainPresentJobExpAutoUse: bool = field(default=False)
    isGachaResultSendToPresentBox: bool = field(default=False)
    isSubjugationTimeType1Notification: bool = field(default=False)
    isSubjugationTimeType2Notification: bool = field(default=False)
    isSubjugationTimeType3Notification: bool = field(default=False)
    isSubjugationTimeType4Notification: bool = field(default=False)
    isSubjugationTimeType5Notification: bool = field(default=False)
    isSubjugationTimeType6Notification: bool = field(default=False)
    isSubjugationTimeType7Notification: bool = field(default=False)
