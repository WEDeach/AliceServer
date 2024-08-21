from dataclasses import dataclass, field

from ..res_base import BaseRes


@dataclass
class CleaningBannerInfo(BaseRes):
    _id: int = field(default=0, metadata={"json_key": "id"})
    text: str = field(default="")
    assetBundleName: str = field(default="")
    resourceName: str = field(default="")
    announceMstId: int = field(default=0)
