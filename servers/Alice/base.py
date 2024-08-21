from flask import Blueprint
from .api.base import bp_api_base

bp_alice_base = Blueprint('Alice', __name__)

@bp_alice_base.after_request
def update_headers(response):
    response.headers['X-Server-Handler'] = "Alice"
    return response

bp_alice_base.register_blueprint(bp_api_base, url_prefix='/api')