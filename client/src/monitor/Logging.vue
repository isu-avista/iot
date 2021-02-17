<template>
  <b-card title='System Log'>
    <b-card-text>
      <pre class="text-left">{{ this.log }}</pre>
    </b-card-text>
  </b-card>
</template>

<script>
import axios from 'axios';
import authHeader from '@/services/auth-header';
import paths from '@/paths';

const host = window.location.protocol + '//' + window.location.host;

export default {
  name: 'Logger',
  data() {
    return {
      log: '',
    };
  },
  methods: {
    getData() {
      const path = host + paths.log;
      axios.get(path, { headers: authHeader() })
        .then((res) => {
          this.log = res.data.log;
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
