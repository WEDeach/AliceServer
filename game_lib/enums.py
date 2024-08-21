from enum import IntEnum


class BanType(IntEnum):
    NoBan = 0
    CannotLogin = 1
    All = 0xFF


class EUserStatus(IntEnum):
    NewUserStatus = 100
    NormalUserStatus = 200
    BannedUserStatus = 300
    UnknownUserStatus = 999


class TutorialMstId(IntEnum):
    LegalAgreement = 1
    Gacha = 2
    UserName = 3
    CharacterSelection = 4
    Clean = 5
    Quest = 6
    QuestResult = 7
    Complete = 100
