<template>
  <b-card header-tag="header">
    <template #header>
      <b-row>
        <b-col><h3 style="float: left;">API Keys</h3></b-col>
        <b-col>
          <h3 style="float: right;">
            <b-button-group>
              <b-button variant="success">
                <b-icon icon="plus-circle"/>
              </b-button>
            </b-button-group>
          </h3>
        </b-col>
      </b-row>
    </template>
    <b-table hover :items="keys" :fields="key_fields">
      <template #cell(actions)>
        <b-button-group>
          <b-button><b-icon icon='pencil-square'/></b-button>
          <b-button variant='danger'><b-icon icon='x-circle'/></b-button>
        </b-button-group>
      </template>
    </b-table>
  </b-card>
</template>

<script>
import axios from 'axios';
import authHeader from '@/services/auth-header';

export default {
  name: 'ApiKeyConfig',
  data() {
    return {
      keys: [],
      key_fields: ['name', 'key', 'created_on', 'actions'],
    };
  },
  methods: {
    getData() {
      const path = 'http://localhost:5000/keys';
      axios.get(path, { headers: authHeader() })
        .then((res) => {
          this.keys = res.data;
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
