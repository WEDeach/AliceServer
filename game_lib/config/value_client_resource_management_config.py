from dataclasses import dataclass

from .value_attention_resource_download import AttentionResourceDownloadValue
from ..value_base import BaseValue


@dataclass
class ClientResourceManagementConfigValue(BaseValue):
    attentionResourceDownload: AttentionResourceDownloadValue
