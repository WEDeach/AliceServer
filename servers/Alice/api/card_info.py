from flask import Blueprint, request

from ....game_lib.card.res_card_data_list import CardDataListRes
from ....game_lib.req_container import ReqContainer
from ....game_lib.res_container import ResContainer


bp_api_card_info = Blueprint("CardInfo", __name__)


@bp_api_card_info.route("/get_card_data_by_user_id", methods=["POST"])
def get_character_data_list():
    req = ReqContainer.unwrap(request.data)

    res = CardDataListRes.get(700001)
    rc = ResContainer.new(200, res)
    return rc.dump_msgpack()
