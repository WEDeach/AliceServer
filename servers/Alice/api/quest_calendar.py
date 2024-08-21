from flask import Blueprint, request

from ....game_lib.quest_out_battle.res_get_quest_calendar_mst_data import (
    GetQuestCalendarMstDataRes,
)
from ....game_lib.req_container import ReqContainer
from ....game_lib.res_container import ResContainer

bp_api_quest_calendar = Blueprint("QuestCalendar", __name__)


@bp_api_quest_calendar.route("/get_quest_calendar_mst_data", methods=["POST"])
def get_quest_calendar_mst_data():
    req = ReqContainer.unwrap(request.data)

    res = GetQuestCalendarMstDataRes()
    rc = ResContainer.new(200, res)
    return rc.dump_msgpack()
