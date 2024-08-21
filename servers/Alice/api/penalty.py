from flask import Blueprint, request


from ....game_lib.req_container import ReqContainer
from ....game_lib.res_container import ResContainer
from ....game_lib.penalty.record_penalty_user_data import PenaltyUserDataRecord
from ....game_lib.penalty.res_penalty_user_data import PenaltyUserDataRes


bp_api_penalty = Blueprint("Penalty", __name__)


@bp_api_penalty.route("/get_penalty_user_data", methods=["POST"])
def get_penalty_user_data():
    req = ReqContainer.unwrap(request.data)

    res = PenaltyUserDataRes(
        penaltyUserData=PenaltyUserDataRecord(
            isPenaltyTime=False,
            endPenaltyTime=0,
        )
    )
    rc = ResContainer.new(200, res)
    return rc.dump_msgpack()
