from flask import Blueprint, request


from ....game_lib.req_container import ReqContainer
from ....game_lib.res_container import ResContainer
from ....game_lib.life_time.res_get_life_time import GetLifeTimeRes


bp_api_lifetime = Blueprint("LifeTime", __name__)


@bp_api_lifetime.route("/get_life_time", methods=["POST"])
def get_life_time():
    req = ReqContainer.unwrap(request.data)

    res = GetLifeTimeRes(lifeTime="貪婪香蕉")
    rc = ResContainer.new(200, res)
    return rc.dump_msgpack()
