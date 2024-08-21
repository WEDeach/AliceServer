from dataclasses import dataclass

from ..res_base import BaseRes


@dataclass
class GetLifeTimeRes(BaseRes):
    lifeTime: str
