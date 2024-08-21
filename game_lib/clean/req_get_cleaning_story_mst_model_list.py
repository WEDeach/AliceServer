from dataclasses import dataclass

from ..req_base import BaseReq


@dataclass
class GetCleaningStoryMstModelListReq(BaseReq):
    characterUniqueId: int
