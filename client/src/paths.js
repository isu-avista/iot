const basePath = 'http://192.168.0.210:5000/api';

export default {
  basePath,
  status: `${basePath}/monitor/status`,
  sensor: `${basePath}/monitor/sensors`,
  log: `${basePath}/monitor/log`,
  userCfg: `${basePath}/users`,
  systemCfg: `${basePath}/config/sysdata`,
  databaseCfg: `${basePath}/config/dbdata`,
  serverCfg: `${basePath}/servers`,
  sensorCfg: `${basePath}/sensors`,
  keyCfg: `${basePath}/keys`,
};
