from flask import Blueprint, request

from ....game_lib.item.res_get_boost_item import GetBoostItemRes
from ....game_lib.item.res_item_data_list import ItemDataListRes
from ....game_lib.req_container import ReqContainer
from ....game_lib.res_container import ResContainer


bp_api_item = Blueprint("Item", __name__)


@bp_api_item.route("/get_boost_item", methods=["POST"])
def get_boost_item():
    req = ReqContainer.unwrap(request.data)

    res = GetBoostItemRes()
    rc = ResContainer.new(200, res)
    return rc.dump_msgpack()

@bp_api_item.route("/get_item_data_list", methods=["POST"])
def get_item_data_list():
    req = ReqContainer.unwrap(request.data)

    res = ItemDataListRes()
    rc = ResContainer.new(200, res)
    return rc.dump_msgpack()
