from typing import List
from dataclasses import dataclass

from ..record_base import BaseRecord


@dataclass
class MovieResourceMstIdModel(BaseRecord):
    orderA: List[int]
    orderB: List[int]
