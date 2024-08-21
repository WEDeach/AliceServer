from flask import Blueprint
from .admission import bp_sw_admission
from .assetbundle import bp_sw_assetbundle
from .standalone import bp_sw_standalone

bp_sw_base = Blueprint('SnowWhite', __name__)

@bp_sw_base.after_request
def update_headers(response):
    response.headers['X-Server-Handler'] = "SnowWhite"
    return response

bp_sw_base.register_blueprint(bp_sw_admission, url_prefix='/admission')
bp_sw_base.register_blueprint(bp_sw_standalone)
bp_sw_base.register_blueprint(bp_sw_assetbundle, url_prefix='/assetbundle')