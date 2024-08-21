from flask import Blueprint, request


from ....game_lib.req_container import ReqContainer
from ....game_lib.res_container import ResContainer
from ....game_lib.guild.record_guild_data import GuildDataRecord
from ....game_lib.guild.res_guild_data import GuildDataRes


bp_api_guild = Blueprint("Guild", __name__)


@bp_api_guild.route("/guild_data", methods=["POST"])
def guild_data():
    req = ReqContainer.unwrap(request.data)

    res = GuildDataRes()
    rc = ResContainer.new(200, res)
    return rc.dump_msgpack()
