from avista_iot.api import api_bp as bp
from flask import request, jsonify, current_app
from avista_data.server import Server
from avista_iot.api import role_required
from avista_data.role import Role


@bp.route('/api/servers', methods=['POST'])
@role_required(Role.ADMIN)
def create_server():
    response_object = {'status': 'success'}

    post_data = request.get_json()
    serv = Server(post_data)
    current_app.session.add(serv)
    current_app.session.commit()
    response_object['message'] = 'Server added!'

    return jsonify(response_object)


@bp.route('/api/servers', methods=['GET'])
@role_required(Role.ADMIN)
def read_servers():
    servers = []
    for server in current_app.session.query(Server).all():
        servers.append(server.to_dict())
    response_object = servers

    return jsonify(response_object)


@bp.route('/api/servers/<server_id>', methods=['PUT'])
@role_required(Role.ADMIN)
def update_server(server_id):
    response_object = {'status': 'success'}

    post_data = request.get_json()
    server = current_app.session.query(Server).filter_by(id=server_id).first()
    server.update(post_data)
    response_object['message'] = 'Server updated!'

    return jsonify(response_object)


@bp.route('/api/servers/<server_id>', methods=['DELETE'])
@role_required(Role.ADMIN)
def delete_server(server_id):
    response_object = {'status': 'success'}

    server = current_app.session.query(Server).filter_by(id=server_id).first()
    current_app.session.delete(server)
    current_app.session.commit()
    response_object['message'] = 'Server deleted!'

    return jsonify(response_object)
