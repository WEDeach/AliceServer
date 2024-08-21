from flask import Blueprint
from ...standalone.remote_config import RemoteConfig

bp_sw_standalone = Blueprint('Standalone', __name__)

@bp_sw_standalone.route('/standalone.bin')
def bin_standalone():
    ins = RemoteConfig.new()
    ins.standaloneType = 0
    return ins.dump_bin()