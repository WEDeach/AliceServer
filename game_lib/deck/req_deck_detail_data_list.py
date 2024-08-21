from dataclasses import dataclass

from ..req_base import BaseReq


@dataclass
class DeckDetailDataListReq(BaseReq):
    deckDataId: int
