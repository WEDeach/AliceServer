from flask import Blueprint, request


from ....game_lib.req_container import ReqContainer
from ....game_lib.res_container import ResContainer
from ....game_lib.user.record_user_data import UserDataRecord
from ....game_lib.user.req_set_user_native_action import SetUserNativeActionReq
from ....game_lib.user.req_user_data import UserDataReq
from ....game_lib.user.res_set_user_native_action import SetUserNativeActionRes
from ....game_lib.user.res_user_data import UserDataRes


bp_api_user = Blueprint("User", __name__)


@bp_api_user.route("/get_user_data", methods=["POST", "GET"])
def get_user_data():
    req = ReqContainer.unwrap(request.data, UserDataReq)

    # TODO: user data fetch...

    user_data = UserDataRecord.get(700001)
    res = UserDataRes(userData=user_data)
    rc = ResContainer.new(200, res)
    return rc.dump_msgpack()


@bp_api_user.route("/set_user_native_action_to_pot", methods=["POST"])
def set_user_native_action_to_pot():
    req = ReqContainer.unwrap(request.data, SetUserNativeActionReq)
    print("set_user_native_action_to_pot:", req.payload)

    # TODO: update user settings...

    res = SetUserNativeActionRes(success=True)
    rc = ResContainer.new(200, res)
    return rc.dump_msgpack()
