from avista_iot.api import api_bp as bp
from flask import request, jsonify
import uuid


APIKEYS = [
    {
        'name': 'foo',
        'key': uuid.uuid4().hex,
        'created_on': '11/01/2020',
    },
    {
        'name': 'bar',
        'key': uuid.uuid4().hex,
        'created_on': '11/02/2020',
    },
]


@bp.route('/api/keys', methods=['GET', 'POST'])
def handle_api_keys():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        APIKEYS.append(request.get_json())
        response_object['message'] = 'Api key added!'
    else:
        response_object = APIKEYS
    return jsonify(response_object)


@bp.route('/api/keys/<key_id>', methods=['PUT'])
def update_api_key(key_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        APIKEYS[key_id] = request.get_json()
        response_object['message'] = 'Api key updated!'
    return jsonify(response_object)


@bp.route('/api/keys/<key_id>', methods=['DELETE'])
def delete_api_key(key_id):
    pass
