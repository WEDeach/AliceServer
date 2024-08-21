import os
from flask import Blueprint

static_folder_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../assetbundles')
bp_sw_assetbundle = Blueprint('Assetbundle', __name__, static_folder=static_folder_path, static_url_path='/')

@bp_sw_assetbundle.route('/test')
def test():
    return "working"