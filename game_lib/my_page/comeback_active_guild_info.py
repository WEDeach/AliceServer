from dataclasses import dataclass

from ..record_base import BaseRecord


@dataclass
class ComebackActiveGuildInfo(BaseRecord):
    assetBundleName: str
    resourceName: str
    title: str
    explanation: str
