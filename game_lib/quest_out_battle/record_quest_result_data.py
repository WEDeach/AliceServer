from dataclasses import dataclass, field

from ..record_base import BaseRecord


@dataclass
class QuestResultDataRecord(BaseRecord):
    questStageMstId: int = field(default=0)
    result: int = field(default=1)
    rewardCountAfter: int = field(default=0)
    characterMstId: int = field(default=0)
    joinType: int = field(default=0)
    hasGuildRelease: bool = field(default=False)
    hasQuestUnitRelease: bool = field(default=False)
    hasQuestEventRelease: bool = field(default=False)
    hasHatredClear: bool = field(default=False)
    hasEventEnded: bool = field(default=False)
    hasPlayedWithFriendOrGuildMember: bool = field(default=False)
    hasReachedMaxMedalNumLimit: bool = field(default=False)
    nextStageMstId: int = field(default=0)
    isRoyalUser: bool = field(default=False)
    questUseStamina: int = field(default=0)
    currentQuestUseStamina: int = field(default=0)
    hasRewardCard: bool = field(default=False)
    hasRewardItem: bool = field(default=False)
    hasRewardCharacter: bool = field(default=False)
    hasRewardCollection: bool = field(default=False)
    requestsRefreshLocalData: bool = field(default=False)
    isLockQuest: bool = field(default=False)
    raidRestartStageMstId: int = field(default=0)
    isRaidStage: bool = field(default=False)
    isGuildRaidStage: bool = field(default=False)
    isLimitCountQuest: bool = field(default=False)
    limitCountRestNum: int = field(default=0)
    maxFriendMedal: int = field(default=0)
    isSoloEventNoWeaponsLeft: bool = field(default=False)
    guildRaidPoint: int = field(default=0)
    guildRaidHighestPoint: int = field(default=0)
    guildRaidRanking: int = field(default=0)
