from avista_iot.api import api_bp as bp
from flask import request, jsonify
from avista_data.role import Role
from avista_iot.api import role_required
from avista_iot import server


@bp.route('/api/config/<section_id>', methods=['GET'])
@role_required(Role.ADMIN)
def read_config(section_id):
    response_object = server.IoTServer.get_instance().get_config(section_id)
    return jsonify(response_object), 200


@bp.route('/api/config/<section_id>', methods=['PUT'])
@role_required(Role.ADMIN)
def update_config(section_id):
    response_object = {'status': 'success'}

    post_data = request.get_json()
    server.IoTServer.get_instance().set_config(section_id, post_data)
    response_object['message'] = 'Config Updated!'

    return jsonify(response_object)