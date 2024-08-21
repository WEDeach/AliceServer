from flask import Blueprint, request


from ....game_lib.deck.req_deck_detail_data_list import DeckDetailDataListReq
from ....game_lib.deck.req_get_bonus_deck import GetBonusDeckReq
from ....game_lib.deck.res_deck_data_list import DeckDataListRes
from ....game_lib.deck.res_deck_detail_data_list import DeckDetailDataListRes
from ....game_lib.deck.res_get_bonus_deck import GetBonusDeckRes
from ....game_lib.req_container import ReqContainer
from ....game_lib.res_container import ResContainer


bp_api_deck = Blueprint("Deck", __name__)


@bp_api_deck.route("/get_deck_data_list", methods=["POST"])
def get_deck_data_list():
    req = ReqContainer.unwrap(request.data)

    res = DeckDataListRes.get(700001)
    rc = ResContainer.new(200, res)
    return rc.dump_msgpack()


@bp_api_deck.route("/get_deck_detail_data", methods=["POST"])
def get_deck_detail_data():
    req = ReqContainer.unwrap(request.data, DeckDetailDataListReq)
    deckDataId = 0
    if req.payload is not None:
        deckDataId = req.payload.deckDataId

    res = DeckDetailDataListRes.get(deckDataId)
    rc = ResContainer.new(200, res)
    return rc.dump_msgpack()


@bp_api_deck.route("/get_bonus_deck_id_list", methods=["POST"])
def get_bonus_deck_id_list():
    req = ReqContainer.unwrap(request.data, GetBonusDeckReq)

    questAreaMstId = 0
    questStageMstId = 0
    if req.payload is not None:
        questAreaMstId = req.payload.questAreaMstId
        questStageMstId = req.payload.questStageMstId

    res = GetBonusDeckRes.get(questAreaMstId, questStageMstId)
    rc = ResContainer.new(200, res)
    return rc.dump_msgpack()
