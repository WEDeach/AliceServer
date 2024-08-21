import json
from flask import Blueprint

bp_aka_auth = Blueprint('Auth', __name__)

@bp_aka_auth.route('/initialize')
def initialize():
    return json.dumps({"result":"OK","app_id":"831556760402145","uuid":"831556760402145b39f1e04a14d885cb08a30db40bcf7d4"})