<template>
  <b-container class="config text-left">
    <br/>
    <b-card no-body>
      <b-tabs card>
        <b-tab title="Server Configuration">
          <b-container fluid>
            <b-row>
              <b-col>
                <ServiceConfig name="Service Configuration" id="sysdata"
                 :path="paths.systemCfg"/>
              </b-col>
            </b-row>
            <br/><br/>
            <b-row>
              <b-col>
                <DbConfig name="Database Configuration" id="dbdata"
                 :path="paths.databaseCfg"/>
              </b-col>
            </b-row>
            <br/><br/>
          </b-container>
        </b-tab>
        <b-tab title="Servers">
          <server-config/>
        </b-tab>
        <b-tab title="Sensors">
          <sensor-config/>
        </b-tab>
        <b-tab title="Security Configuration">
          <b-container fluid>
            <b-row>
              <b-col>
                <user-config/>
              </b-col>
            </b-row>
            <br/><br/>
            <b-row>
              <b-col>
                <api-key-config/>
              </b-col>
            </b-row>
          </b-container>
        </b-tab>
      </b-tabs>
    </b-card>
    <br/><br/>
  </b-container>
</template>

<script>
// @ is an alias to /src
import ServiceConfig from '@/config/ServiceConfig.vue';
import DbConfig from '@/config/DbConfig.vue';
import SensorConfig from '@/config/SensorConfig.vue';
import ServerConfig from '@/config/ServerConfig.vue';
import UserConfig from '@/config/UserConfig.vue';
import ApiKeyConfig from '@/config/ApiKeyConfig.vue';
import paths from '@/paths';

export default {
  name: 'Config',
  components: {
    ServiceConfig,
    DbConfig,
    SensorConfig,
    ServerConfig,
    UserConfig,
    ApiKeyConfig,
  },
  data() {
    return {
      paths,
    };
  },
};
</script>
