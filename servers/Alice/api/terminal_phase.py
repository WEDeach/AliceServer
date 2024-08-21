from flask import Blueprint, request


from ....game_lib.req_container import ReqContainer
from ....game_lib.res_container import ResContainer
from ....game_lib.quest_out_battle.res_get_user_quest_desire_phase_no import (
    GetUserQuestDesirePhaseNoRes,
)


bp_api_terminal_phase = Blueprint("TerminalPhase", __name__)


@bp_api_terminal_phase.route("/get_phase_no", methods=["POST"])
def GetUserPhasNo():
    req = ReqContainer.unwrap(request.data)

    res = GetUserQuestDesirePhaseNoRes(phaseNo=0)
    rc = ResContainer.new(200, res)
    return rc.dump_msgpack()
