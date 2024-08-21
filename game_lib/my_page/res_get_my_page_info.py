from dataclasses import dataclass, field
from typing import List, Optional


from .comeback_active_guild_info import ComebackActiveGuildInfo
from .extra_mission_info import ExtraMissionInfo
from .gachi_colosseum_info import GachiColosseumInfo
from .mountain_event import MountainEvent
from .movie_resource_mst_id_model import MovieResourceMstIdModel
from .nekoalice import Nekoalice
from .product_payment_status import ProductPaymentStatus
from .record_login_bonus_data import LoginBonusDataRecord
from .scratch_gacha_info import ScratchGachaInfo
from .special_background_dust_effect_info import SpecialBackgroundDustEffectInfo
from .switchable_background_info import SwitchableBackgroundInfo
from .switchable_bgm_info import SwitchableBgmInfo
from .wall_banner_text import WallBannerText
from .wgc_mvp_award_info import WgcMvpAwardInfo
from .wgc_tournament_info import WgcTournamentInfo
from ..chat.new_message_list import NewMessageList
from ..clean.clean_info_data import CleanInfoData
from ..guild.record_guild_data import GuildDataRecord
from ..guild.guild_member_info import GuildMemberInfo
from ..mst.record_banner_mst import BannerMstRecord
from ..nightmare_search.record_nightmare_search_count_data import (
    NightmareSearchCountDataRecord,
)
from ..res_base import BaseRes


@dataclass
class GetMyPageInfoRes(BaseRes):
    guildData: Optional[GuildDataRecord] = field(default=None)
    presentNum: Optional[int] = field(default=0)
    guildMemberList: Optional[List[GuildMemberInfo]] = field(default_factory=list)
    myRankAtGuild: Optional[int] = field(default=0)
    missionClearCount: Optional[int] = field(default=0)
    guildInvitationCount: Optional[int] = field(default=0)
    bannerMstIds: Optional[List[int]] = field(default_factory=list)
    bannerMstList: Optional[List[BannerMstRecord]] = field(default_factory=list)
    badgeBannerMstId: Optional[int] = field(default=0)
    wallBannerMstIds: Optional[List[int]] = field(default_factory=list)
    wallBannerTextList: Optional[List[WallBannerText]] = field(default_factory=list)
    isQuestOpen: Optional[bool] = field(default=False)
    isLoseQuestExist: Optional[bool] = field(default=False)
    openQuestStageMstId: Optional[int] = field(default=0)
    isGveQuestOpen: Optional[bool] = field(default=False)
    cleanInfoData: Optional[CleanInfoData] = field(default=None)
    loginBonusDataList: Optional[List[LoginBonusDataRecord]] = field(
        default_factory=list
    )
    navigatorTalkMstId: Optional[int] = field(default=0)
    nightmareSearchCountData: Optional[NightmareSearchCountDataRecord] = field(default=None)
    newMessageList: Optional[List[NewMessageList]] = field(default_factory=list)
    productPaymentStatusList: Optional[List[ProductPaymentStatus]] = field(
        default_factory=list
    )
    refreshTime: Optional[int] = field(default=30)
    extraMissionInfo: Optional[ExtraMissionInfo] = field(default=None)
    gachaConduction: Optional[bool] = field(default=False)
    specialBackgroundDustEffectInfo: Optional[SpecialBackgroundDustEffectInfo] = field(
        default=None
    )
    switchableBackgroundInfo: Optional[SwitchableBackgroundInfo] = field(default=None)
    switchableBgmInfo: Optional[SwitchableBgmInfo] = field(default=None)
    movieResourceMstIds: Optional[MovieResourceMstIdModel] = field(default=None)
    scratchGacha: Optional[ScratchGachaInfo] = field(default=None)
    comebackActiveGuild: Optional[ComebackActiveGuildInfo] = field(default=None)
    isUnreadLetter: Optional[int] = field(default=0)
    wgcQualifierStatus: Optional[int] = field(default=0)
    wgcTournamentInfo: Optional[WgcTournamentInfo] = field(default=None)
    wgcMvpAwardInfo: Optional[WgcMvpAwardInfo] = field(default=None)
    isShowLetterButton: Optional[bool] = field(default=False)
    gachiColosseumInfo: Optional[GachiColosseumInfo] = field(default=None)
    nekoalice: Optional[Nekoalice] = field(default=None)
    summerCamp2022: Optional[MountainEvent] = field(default=None)
    yokubouButton: Optional[bool] = field(default=False)
