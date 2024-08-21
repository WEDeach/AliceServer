from dataclasses import dataclass, field

from .record_quest_attention_data import QuestAttentionDataRecord
from ..res_base import BaseRes


@dataclass
class GetAttentionRes(BaseRes):
    attentionData: QuestAttentionDataRecord = field(default=QuestAttentionDataRecord())
