from dataclasses import dataclass, field

from .cleaning_banner_info import CleaningBannerInfo
from .cleaning_rematch_info import CleaningRematchInfo
from .cleaning_result_data import CleaningResultData
from ..res_base import BaseRes


@dataclass
class CleanEndRes(BaseRes):
    cleaningResultData: CleaningResultData = field(default=CleaningResultData())
    bannerInfo: CleaningBannerInfo = field(default=CleaningBannerInfo())
    cleaningRematchInfo: CleaningRematchInfo = field(default=CleaningRematchInfo())
    miniTutorialId: int = field(default=0)
