from flask import Blueprint, request

from ....game_lib.req_container import ReqContainer
from ....game_lib.res_container import ResContainer
from ....game_lib.config.res_get_push_notification_config import GetPushNotificationConfigRes


bp_api_user_config = Blueprint("UserConfig", __name__)


@bp_api_user_config.route("/get_user_config", methods=["POST"])
def get_user_config():
    req = ReqContainer.unwrap(request.data)

    res = GetPushNotificationConfigRes()
    rc = ResContainer.new(200, res)
    return rc.dump_msgpack()
