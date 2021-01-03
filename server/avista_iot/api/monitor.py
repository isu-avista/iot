from avista_iot.api import api_bp as bp
from avista_data.data_point import DataPoint
from avista_data.sensor import Sensor
from flask import request, jsonify
from avista_data.role import Role
from avista_iot import server
from avista_iot.api import role_required
import uuid

STATUS = [
    {'id': uuid.uuid4().hex, 'name': 'Power', 'value': 2},
    {'id': uuid.uuid4().hex, 'name': 'Network', 'value': 2},
    {'id': uuid.uuid4().hex, 'name': 'Sensors', 'value': 1},
    {'id': uuid.uuid4().hex, 'name': 'Servers', 'value': 1},
]


@bp.route('/api/monitor/status', methods=['GET'])
@role_required(Role.USER)
def read_status():
    return jsonify(STATUS)


@bp.route('/api/monitor/sensors/data/<sensor>', methods=['GET'])
@role_required(Role.USER)
def get_data(sensor):
    item = {
        'name': sensor.get_name(),
        'id': sensor.get_id(),
        'units': str(sensor.get_unit()),
    }
    data = []
    points = DataPoint.query.filter_by(sensor_id=sensor.get_id()).order_by(DataPoint.timestamp).all()
    for point in points:
        data.append([point.get_timestamp(), point.get_value()])
    item['data'] = data
    return item


@bp.route('/api/monitor/sensors/data/<sensor>/<since>', methods=['GET'])
@role_required(Role.USER)
def get_data_since(sensor, since):
    item = {
        'name': sensor.get_name(),
        'id': sensor.get_id(),
        'units': sensor.get_unit(),
    }
    data = []
    points = DataPoint.query.filter_by(sensor_id=sensor.get_id()).filter(DataPoint.timestamp >= since).order_by(
        DataPoint.timestamp).all()
    for point in points:
        data.append([point.get_timestamp(), point.get_value()])
    item['data'] = data
    return item


@bp.route('/api/monitor/sensors', methods=['GET'])
@role_required(Role.USER)
def read_sensor_data():
    items = []
    sensors = Sensor.query.all()
    since = request.args.get('since')
    if since is not None:
        for sensor in sensors:
            item = get_data(sensor)
            items.append(item)
    else:
        for sensor in sensors:
            item = get_data(sensor)
            items.append(item)
    return jsonify(items)


@bp.route('/api/monitor/sensors/<sensor_id>', methods=['GET'])
@role_required(Role.USER)
def read_sensor_data_since(sensor_id):
    since = request.args.get('since')
    sensor = Sensor.query.filter_by(sensor_id=sensor_id).first()
    if since is not None:
        get_data_since(sensor, since)
    else:
        get_data(sensor)


@bp.route('/api/monitor/log', methods=['GET'])
@role_required(Role.USER)
def read_logger_data():
    return jsonify(server.IoTServer.get_instance().get_log())
