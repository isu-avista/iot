from avista_iot.api import api_bp as bp
from flask import request, jsonify
from avista_data.server import Server
from avista_data import db
from avista_iot.api import role_required
from avista_data.role import Role


@bp.route('/api/servers', methods=['POST'])
@role_required(Role.ADMIN)
def create_server():
    response_object = {'status': 'success'}

    post_data = request.get_json()
    serv = Server(post_data)
    db.session.add(serv)
    db.session.commit()
    response_object['message'] = 'Server added!'

    return jsonify(response_object)


@bp.route('/api/servers', methods=['GET'])
@role_required(Role.ADMIN)
def read_servers():
    servers = []
    for server in Server.query.all():
        servers.append(server.to_dict())
    response_object = servers

    return jsonify(response_object)


@bp.route('/api/servers/<server_id>', methods=['PUT'])
@role_required(Role.ADMIN)
def update_server(server_id):
    response_object = {'status': 'success'}

    post_data = request.get_json()
    server = Server.query.filter_by(id=server_id).first()
    server.update(post_data)
    response_object['message'] = 'Server updated!'

    return jsonify(response_object)


@bp.route('/api/servers/<server_id>', methods=['DELETE'])
@role_required(Role.ADMIN)
def delete_server(server_id):
    response_object = {'status': 'success'}

    server = Server.query.filter_by(id=server_id).first()
    db.session.delete(server)
    db.session.commit()
    response_object['message'] = 'Server deleted!'

    return jsonify(response_object)
