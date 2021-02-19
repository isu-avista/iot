from avista_iot.api import api_bp as bp
from avista_data.sensor import Sensor
from flask import request, jsonify, current_app
from avista_iot.api import role_required
from avista_data.role import Role


@bp.route('/api/sensors', methods=['POST'])
@role_required(Role.ADMIN)
def create_sensor():
    response_object = {'status': 'success'}

    post_data = request.get_json()
    sensor = Sensor(post_data)
    current_app.session.add(sensor)
    current_app.session.commit()

    response_object['message'] = 'Sensor added!'

    return jsonify(response_object)


@bp.route('/api/sensors', methods=['GET'])
@role_required(Role.ADMIN)
def read_sensors():
    sensors = []
    for s in current_app.session.query(Sensor).all():
        sensors.append(s.to_dict())
    response_object = sensors

    return jsonify(response_object)


@bp.route('/api/sensors/<sensor_id>', methods=['PUT'])
@role_required(Role.ADMIN)
def update_sensor(sensor_id):
    response_object = {'status': 'success'}

    post_data = request.get_json()
    sensor = current_app.session.query(Sensor).filter_by(id=sensor_id).first()
    sensor.update(post_data)

    response_object['message'] = 'Sensor updated!'

    return jsonify(response_object)


@bp.route('/api/sensors/<sensor_id>', methods=['DELETE'])
@role_required(Role.ADMIN)
def delete_sensor(sensor_id):
    response_object = {'status': 'success'}

    sensor = current_app.session.query(Sensor).filter_by(id=sensor_id).first()

    current_app.session.delete(sensor)
    current_app.session.commit()
    response_object['message'] = 'Sensor deleted!'

    return jsonify(response_object)
