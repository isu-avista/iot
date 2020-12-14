<template>
  <div class="sensors">
    <br/>
    <b-container>
      <b-row no-gutters cols-md='2'>
        <b-col>
          <Status/>
          <br>
          <Logger/>
        </b-col>
        <b-col>
          <Sensors/>
        </b-col>
      </b-row>
      <br/>
    </b-container>
  </div>
</template>

<script>
// @ is an alias to /src
import Sensors from '@/monitor/Sensor.vue';
import Logger from '@/monitor/Logging.vue';
import Status from '@/monitor/Status.vue';

export default {
  name: 'Monitor',
  components: {
    Sensors,
    Logger,
    Status,
  },
};
</script>
