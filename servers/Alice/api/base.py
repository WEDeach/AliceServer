import os

from flask import Blueprint, request

from .card_info import bp_api_card_info
from .character import bp_api_chara
from .cleaning import bp_api_cleaning
from .config import bp_api_config
from .deck import bp_api_deck
from .guild import bp_api_guild
from .gvg_out_battle import bp_api_gvg_out_battle
from .item import bp_api_item
from .life_time import bp_api_lifetime
from .login import bp_api_login
from .mst import bp_api_mst
from .my_page import bp_api_my_page
from .notification import bp_api_notification
from .penalty import bp_api_penalty
from .quest import bp_api_quest
from .quest_calendar import bp_api_quest_calendar
from .scenario import bp_api_scenario
from .terminal_phase import bp_api_terminal_phase
from .tutorial import bp_api_tutorial
from .user import bp_api_user
from .user_config import bp_api_user_config
from .web_payment import bp_api_wpay
from ....game_lib.res_container import ResContainer
from ....game_lib.res_error import ResError
from ....utils.crypto import AliceCrypto

bp_api_base = Blueprint("Api", __name__)


@bp_api_base.before_app_request
def middleware_decrypt_body():
    if request.method == "POST":
        # 先解密
        k = (os.getenv("R_API_KEY") or "").encode()
        d = AliceCrypto.decrypt(request.get_data(parse_form_data=True), k)

        # 將解密的資料取代原有Body
        request._cached_data = d
        setattr(request, "resp_need_enc", True)


@bp_api_base.app_errorhandler(404)
def api_not_handler(error=None):
    e = ResError(domain=request.path, code=40004, field="", reason=str(error))
    ec = ResContainer.new_with_error(404, e)
    print("api not handler:", ec)
    return ec.dump_msgpack()


@bp_api_base.app_errorhandler(500)
def api_error(error):
    e = ResError(domain=request.path, code=50000, field="", reason=str(error))
    ec = ResContainer.new_with_error(200, e)
    print("error handler:", ec)
    return ec.dump_msgpack()


@bp_api_base.after_app_request
def middleware_encrypt_body(response):
    need_enc = getattr(request, "resp_need_enc", False)
    if need_enc:
        response.data = encrypt_data(response.data)
        response.mimetype = "application/x-msgpack"
    return response


def encrypt_data(data: bytes):
    k = (os.getenv("R_API_KEY") or "").encode()
    i = os.urandom(16)
    d = AliceCrypto.encrypt(data, k, i)
    return i + d


bp_api_base.register_blueprint(bp_api_card_info, url_prefix="/card_info")
bp_api_base.register_blueprint(bp_api_chara, url_prefix="/character")
bp_api_base.register_blueprint(bp_api_cleaning, url_prefix="/cleaning")
bp_api_base.register_blueprint(bp_api_config, url_prefix="/config")
bp_api_base.register_blueprint(bp_api_deck, url_prefix="/deck")
bp_api_base.register_blueprint(bp_api_guild, url_prefix="/guild")
bp_api_base.register_blueprint(bp_api_gvg_out_battle, url_prefix="/gvg_out_battle")
bp_api_base.register_blueprint(bp_api_lifetime, url_prefix="/life_time")
bp_api_base.register_blueprint(bp_api_item, url_prefix="/item")
bp_api_base.register_blueprint(bp_api_login, url_prefix="/login")
bp_api_base.register_blueprint(bp_api_mst, url_prefix="/mst")
bp_api_base.register_blueprint(bp_api_my_page, url_prefix="/my_page")
bp_api_base.register_blueprint(bp_api_notification, url_prefix="/notification")
bp_api_base.register_blueprint(bp_api_penalty, url_prefix="/penalty")
bp_api_base.register_blueprint(bp_api_quest_calendar, url_prefix="/quest_calendar")
bp_api_base.register_blueprint(bp_api_quest, url_prefix="/quest")
bp_api_base.register_blueprint(bp_api_scenario, url_prefix="/scenario")
bp_api_base.register_blueprint(bp_api_terminal_phase, url_prefix="/terminal_phase")
bp_api_base.register_blueprint(bp_api_tutorial, url_prefix="/tutorial")
bp_api_base.register_blueprint(bp_api_user_config, url_prefix="/user_config")
bp_api_base.register_blueprint(bp_api_user, url_prefix="/user")
bp_api_base.register_blueprint(bp_api_wpay, url_prefix="/web_payment")
