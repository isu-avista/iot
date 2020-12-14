<template>
  <b-container fluid>
    <div v-for="server in servers" :key="server.name">
    <b-row>
      <b-col>
        <b-card header-tag="header">
          <template #header>
            <b-row>
              <b-col><h3 style="float: left;">{{ server.name }}</h3></b-col>
              <b-col>
                <h3 style="float: right;">
                  <b-button-group>
                    <b-button v-b-modal.edit-server-modal @click="editServer(server)">
                      <b-icon icon="pencil-square"/></b-button>
                    <b-button variant="danger" @click="onDeleteServer(server)">
                      <b-icon icon="x-circle"/></b-button>
                  </b-button-group>
                </h3>
              </b-col>
            </b-row>
          </template>
          <table class="table table-hover">
            <thead>
              <tr>
                <th scope="col">Item</th>
                <th scope="col">Value</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>IP Address</td>
                <td>{{ server.ip_address }}</td>
              </tr>
              <tr>
                <td>Port</td>
                <td>{{ server.port }}</td>
              </tr>
              <tr>
                <td>Update Periodicity (ms)</td>
                <td>{{ server.periodicity }}</td>
              </tr>
            </tbody>
          </table>
        </b-card>
      </b-col>
    </b-row>
    <br/>
    </div>
    <br/>
    <div class="text-right">
    <b-button variant="success" v-b-modal.server-modal>
      <b-icon icon="plus-circle"/>&nbsp;&nbsp;Add server
    </b-button>
    </div>

    <b-modal ref="addServerModal"
             id="server-modal"
             title="Add new Server"
             hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-name-group"
                      label="Name:"
                      label-for="form-name-input">
          <b-form-input id="form-name-input"
                        type="text"
                        v-model="addServerForm.name"
                        required
                        placeholder="Enter Server name">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-ip-group"
                      label="IP Address:"
                      label-for="form-ip-input">
          <b-form-input id="form-ip-input"
                        type="text"
                        v-model="addServerForm.ip_address"
                        required
                        placeholder="Enter IP address">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-port-group"
                      label="Port:"
                      label-for="form-port-input">
          <b-form-input id="form-port-input"
                         v-model="addServerForm.port"
                         required
                         type="number">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-period-group"
                      label="Periodicity (ms):"
                      label-for="form-period-input">
          <b-form-input id="form-period-input"
                        type="number"
                        v-model="addServerForm.periodicity"
                        required>
          </b-form-input>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>

    <b-modal ref="editServerModal"
             id="edit-server-modal"
             title="Update Server"
             hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
        <b-form-group id="form-name-edit-group"
                      label="Name:"
                      label-for="form-name-edit-input">
          <b-form-input id="form-name-edit-input"
                        type="text"
                        v-model="editServerForm.name"
                        required
                        placeholder="Enter Server name">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-ip-edit-group"
                      label="IP Address:"
                      label-for="form-ip-edit-input">
          <b-form-input id="form-ip-edit-input"
                        type="text"
                        v-model="editServerForm.ip_address"
                        required
                        placeholder="Enter IP address">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-port-edit-group"
                      label="Port:"
                      label-for="form-port-edit-input">
          <b-form-input id="form-port-edit-input"
                         v-model="editServerForm.port"
                         required
                         type="number">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-period-edit-group"
                      label="Periodicity (ms):"
                      label-for="form-period-edit-input">
          <b-form-input id="form-period-edit-input"
                        type="number"
                        v-model="editServerForm.periodicity"
                        required>
          </b-form-input>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </b-container>
</template>

<script>
import axios from 'axios';
import authHeader from '@/services/auth-header';

const API_URL = 'http://localhost:5000/api';

export default {
  name: 'ServerConfig',
  data() {
    return {
      servers: {},
      units: [
        { value: 'HZ', text: 'Hertz (Hz)' },
        { value: 'KWH', text: 'Kilo-watt Hours (kWh)' },
        { value: 'J', text: 'Joules (J)' },
        { value: 'DB', text: 'Decibels (dB)' },
        { value: 'F', text: 'Degrees Farenheit (F)' },
        { value: 'C', text: 'Degrees Celcius (C)' },
      ],
      addServerForm: {
        name: '',
        ip_address: '',
        port: '',
        period: '',
      },
      editServerForm: {
        id: '',
        name: '',
        ip_address: '',
        port: '',
        period: '',
      },
    };
  },
  methods: {
    getData() {
      const path = `${API_URL}/servers`;
      axios.get(path, { headers: authHeader() })
        .then((res) => {
          this.servers = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    initForm() {
      this.addServerForm.name = '';
      this.addServerForm.ip_address = '';
      this.addServerForm.port = '';
      this.addServerForm.periodicity = 0;
      this.editServerForm.id = 0;
      this.editServerForm.name = '';
      this.editServerForm.ip_address = '';
      this.editServerForm.port = 0;
      this.editServerForm.periodicity = 0;
    },
    addServer(payload) {
      const path = `${API_URL}/servers`;
      axios.post(path, payload, { headers: authHeader() })
        .then(() => {
          this.getData();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getData();
        });
    },
    editServer(server) {
      this.editServerForm = server;
    },
    updateServer(payload, serverID) {
      const path = `${API_URL}/servers/${serverID}`;
      axios.put(path, payload, { headers: authHeader() })
        .then(() => {
          this.getData();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getData();
        });
    },
    removeServer(serverID) {
      const path = `${API_URL}/servers/${serverID}`;
      axios.delete(path, { headers: authHeader() })
        .then(() => {
          this.getData();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getData();
        });
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addServerModal.hide();
      const payload = {
        name: this.addServerForm.name,
        ip_address: this.addServerForm.ip_address,
        port: this.addServerForm.port,
        periodicity: this.addServerForm.periodicity,
      };
      this.addServer(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addServerModal.hide();
      this.initForm();
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editServerModal.hide();
      const payload = {
        name: this.editServerForm.name,
        ip_address: this.editServerForm.ip_address,
        port: this.editServerForm.port,
        periodicity: this.editServerForm.periodicity,
      };
      this.updateServer(payload, this.editServerForm.id);
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editServerModal.hide();
      this.initForm();
      this.getServers();
    },
    onDeleteServer(Server) {
      this.removeServer(Server.id);
    },
  },
  created() {
    this.getData();
  },
};
</script>
