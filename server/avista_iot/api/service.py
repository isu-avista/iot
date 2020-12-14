from avista_iot.api import api_bp as bp
from flask import jsonify


# sanity check route
@bp.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')
