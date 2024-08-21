from dataclasses import dataclass

from ..res_base import BaseRes


@dataclass
class CleanNightmareInfo(BaseRes):
    assetBundleName: str
    resourceName: str
