from flask import Blueprint, request



from ....game_lib.req_container import ReqContainer
from ....game_lib.res_container import ResContainer
from ....game_lib.penalty.record_penalty_user_data import PenaltyUserDataRecord
from ....game_lib.my_page.res_get_my_page_info import GetMyPageInfoRes


bp_api_my_page = Blueprint("MyPage", __name__)


@bp_api_my_page.route("/get_my_page_info_for_alice_11", methods=["POST"])
def get_my_page_info_for_alice_11():
    req = ReqContainer.unwrap(request.data)

    # 
    res = GetMyPageInfoRes(
        bannerMstIds = [12]
    )
    rc = ResContainer.new(200, res)
    return rc.dump_msgpack()
