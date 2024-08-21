from dataclasses import dataclass

from ..req_base import BaseReq


@dataclass
class GetScenarioStoryMstReq(BaseReq):
    storyIndex: int
    storyNo: int
