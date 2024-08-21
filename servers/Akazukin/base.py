from flask import Blueprint
from .auth import bp_aka_auth

bp_aka_base = Blueprint('Akazukin', __name__)

@bp_aka_base.after_request
def update_headers(response):
    response.headers['X-Server-Handler'] = "Akazukin"
    return response

bp_aka_base.register_blueprint(bp_aka_auth, url_prefix='/auth')