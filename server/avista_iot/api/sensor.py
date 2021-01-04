from avista_iot.api import api_bp as bp
from avista_data import db
from avista_data.sensor import Sensor
from flask import request, jsonify
from avista_iot.api import role_required
from avista_data.role import Role
import avista_iot.server as svc
import avista_sensors.processor_loader as pl


@bp.route('/api/sensors', methods=['POST'])
@role_required(Role.ADMIN)
def create_sensor():
    response_object = {'status': 'success'}

    post_data = request.get_json()
    sensor = Sensor(post_data)
    db.session.add(sensor)
    db.session.commit()

    svc.IoTServer.get_instance().processor_manager.processors.append(pl.load_sensor_from_dict(sensor.to_dict()))

    response_object['message'] = 'Sensor added!'

    return jsonify(response_object)


@bp.route('/api/sensors', methods=['GET'])
@role_required(Role.ADMIN)
def read_sensors():
    sensors = []
    for s in Sensor.query.all():
        sensors.append(s.to_dict())
    response_object = sensors

    return jsonify(response_object)


@bp.route('/api/sensors/<sensor_id>', methods=['PUT'])
@role_required(Role.ADMIN)
def update_sensor(sensor_id):
    response_object = {'status': 'success'}

    post_data = request.get_json()
    sensor = Sensor.query.filter_by(id=sensor_id).first()

    for i in range(0, len(svc.IoTServer.get_instance().processor_manager.processors)):
        if svc.IoTServer.get_instance().processor_manager.processors[i].get_name() == sensor.get_name():
            sensor.update(post_data)
            svc.IoTServer.get_instance().processor_manager.processors[i] = pl.load_sensor_from_dict(sensor.to_dict())

    response_object['message'] = 'Sensor updated!'

    return jsonify(response_object)


@bp.route('/api/sensors/<sensor_id>', methods=['DELETE'])
@role_required(Role.ADMIN)
def delete_sensor(sensor_id):
    response_object = {'status': 'success'}

    sensor = Sensor.query.filter_by(id=sensor_id).first()

    for sensor_obj in svc.IoTServer.get_instance().processor_manager.processors:
        if sensor_obj.get_name() == sensor.get_name():
            svc.IoTServer.get_instance().processor_manager.processors.remove(sensor_obj)

    db.session.delete(sensor)
    db.session.commit()
    response_object['message'] = 'Sensor deleted!'

    return jsonify(response_object)
