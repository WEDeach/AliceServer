from flask import Blueprint, request, g


from ....game_lib.enums import EUserStatus, BanType
from ....game_lib.req_container import ReqContainer
from ....game_lib.res_container import ResContainer
from ....game_lib.login.req_login import LoginReq
from ....game_lib.login.res_login import LoginRes


bp_api_login = Blueprint('Login', __name__)

@bp_api_login.route('', methods=['POST', 'GET'])
def login():
    req = ReqContainer[LoginReq].unwrap(request.data, LoginReq)
    print("login req:", req)

    g.user_700001_login_action = req.actionTime

    # TODO: user login...

    res = LoginRes(
        sessionId="test",
        userId=700001,
        status=EUserStatus.NewUserStatus,
        banType=BanType.NoBan
    )
    rc = ResContainer.new(200, res)
    print("login res [test]:", rc)
    return rc.dump_msgpack()