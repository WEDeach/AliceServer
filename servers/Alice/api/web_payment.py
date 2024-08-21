from flask import Blueprint, request


from ....game_lib.req_container import ReqContainer
from ....game_lib.res_container import ResContainer
from ....game_lib.web_payment.res_cancel_latest import CancelLatestRes


bp_api_wpay = Blueprint("WebPayment", __name__)


@bp_api_wpay.route("/cancel_latest", methods=["POST"])
def cancel_latest():
    req = ReqContainer.unwrap(request.data)

    res = CancelLatestRes(result="OK")
    rc = ResContainer.new(200, {})
    return rc.dump_msgpack()
