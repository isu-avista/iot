<template>
<div class="container-md">
  <b-card header-tag="header" title="Sensors">
    <div id="wrapper">
      <div v-for="sensor in sensors" :key="sensor.id">
        <div :id="'chart-line-' + sensor.id">
          <apexchart type="line" height="160" :options="sensor.chartOptions"
           :series="sensor.series"></apexchart>
        </div>
      </div>
    </div>
  </b-card>
</div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts';
import axios from 'axios';
import authHeader from '@/services/auth-header';
import paths from '@/paths';

const host = `${window.location.protocol}//${window.location.hostname}`;

export default {
  name: 'Sensors',
  components: {
    apexchart: VueApexCharts,
  },
  data() {
    return {
      sensors: [],
    };
  },
  methods: {
    getData() {
      const path = host + paths.sensor;
      axios.get(path, { headers: authHeader() })
        .then((res) => {
          this.sensors = [];
          res.data.forEach((item) => {
            this.sensors.push({
              id: item.id,
              series: [{
                data: item.data,
                name: item.name,
              }],
              chartOptions: {
                chart: {
                  id: item.id,
                  group: 'sensors',
                  type: 'line',
                },
                title: {
                  text: item.name,
                },
                colors: ['#008FFB'],
                yaxis: {
                  labels: {
                    minWidth: 40,
                  },
                  title: {
                    text: item.units,
                  },
                },
                xaxis: {
                  type: 'datetime',
                },
                dataLabels: {
                  enabled: false,
                },
              },
            });
          });
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getData();
  },
};
</script>

<style>
#chart, .chart-box {
    padding-top: 20px;
    padding-left: 10px;
    background: #fff;
    border: 1px solid #ddd;
    box-shadow: 0 22px 35px -16px rgba(0,0,0, 0.1);
}

.apexcharts-canvas {
    margin: 0 auto;
}
</style>
