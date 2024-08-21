from flask import Blueprint, request

from ....game_lib.res_base import BaseRes

from ....game_lib.gvg_out_battle.current_gvg_schedule_value import CurrentGvgScheduleValue

from ....game_lib.req_container import ReqContainer
from ....game_lib.res_container import ResContainer
from ....game_lib.gvg_out_battle.res_get_current_gvg_schedule import GetCurrentGvgScheduleRes


bp_api_gvg_out_battle = Blueprint("GvgOutBattle", __name__)


@bp_api_gvg_out_battle.route("/get_current_gvg_schedule", methods=["GET", "POST"])
def get_current_gvg_schedule():
    if request.method == "POST":
        req = ReqContainer.unwrap(request.data)

    res = GetCurrentGvgScheduleRes()
    print(type(res))
    print(issubclass(type(res), BaseRes))
    print('get_current_gvg_schedule:', res)
    rc = ResContainer.new(200, res)
    return rc.dump_msgpack()
