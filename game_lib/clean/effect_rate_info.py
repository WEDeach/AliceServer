from dataclasses import dataclass

from ..res_base import BaseRes


@dataclass
class EffectRateInfo(BaseRes):
    numerator: int
    denominator: int
