from flask import Blueprint, request



from ....game_lib.req_container import ReqContainer
from ....game_lib.res_container import ResContainer
from ....game_lib.penalty.record_penalty_user_data import PenaltyUserDataRecord
from ....game_lib.my_page.res_get_my_page_info import GetMyPageInfoRes


bp_api_notification = Blueprint("Notification", __name__)


@bp_api_notification.route("/register", methods=["POST"])
def register():
    req = ReqContainer.unwrap(request.data)

    print('register: ', req)
    # 
    res = {}
    rc = ResContainer.new(200, res)
    return rc.dump_msgpack()
