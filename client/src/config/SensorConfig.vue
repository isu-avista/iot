<template>
  <b-container fluid>
    <div v-for="sensor in sensors" :key="sensor.name">
    <b-row>
      <b-col>
        <b-card header-tag="header">
          <template #header>
            <b-row>
              <b-col><h3 style="float: left;">{{ sensor.name }}</h3></b-col>
              <b-col>
                <h3 style="float: right;">
                  <b-button-group>
                    <b-button v-b-modal.edit-sensor-modal @click="editSensor(sensor)">
                      <b-icon icon="pencil-square"/></b-button>
                    <b-button variant="danger" @click="onDeleteSensor(sensor)">
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
                <td>Measured Quantity</td>
                <td>{{ sensor.quantity }}</td>
              </tr>
              <tr>
                <td>Measurement Unit</td>
                <td>{{ sensor.unit }}</td>
              </tr>
              <tr>
                <td>Sensor Module</td>
                <td>{{ sensor.module }}</td>
              </tr>
              <tr>
                <td>Sensor Class</td>
                <td>{{ sensor.cls }}</td>
              </tr>
            </tbody>
          </table>
          <div>
            <b-button v-b-toggle.pinout-collapse variant="secondary">Toggle Pin Out</b-button>
            <b-collapse id="pinout-collapse" class="mt-2">
              <b-card>
                <b-table hover :items="sensor.pinout" show-empty>
                  <template v-slot:cell(var)="row">
                    {{ row.item.var }}
                  </template>
                  <template v-slot:cell(pin)="row">
                    {{ row.item.pin }}
                  </template>
                </b-table>
              </b-card>
            </b-collapse>
          </div>
        </b-card>
      </b-col>
    </b-row>
    <br/>
    </div>
    <br/>
    <div class="text-right">
    <b-button variant="success" v-b-modal.sensor-modal>
      <b-icon icon="plus-circle"/>&nbsp;&nbsp;Add sensor
    </b-button>
    </div>

    <b-modal ref="addSensorModal"
             id="sensor-modal"
             title="Add new Sensor"
             hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-name-group"
                      label="Name:"
                      label-for="form-name-input">
          <b-form-input id="form-name-input"
                        type="text"
                        v-model="addSensorForm.name"
                        required
                        placeholder="Enter sensor name">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-quantity-group"
                      label="Measured Quantity:"
                      label-for="form-quantity-input">
          <b-form-input id="form-quantity-input"
                        type="text"
                        v-model="addSensorForm.quantity"
                        required
                        placeholder="Enter quantity">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-unit-group"
                      label="Measurement Unit:"
                      label-for="form-unit-select">
          <b-form-select id="form-unit-select"
                         v-model="addSensorForm.unit"
                         :options="units">
          </b-form-select>
        </b-form-group>
        <b-form-group id="form-module-group"
                      label="Sensor Module:"
                      label-for="form-module-input">
          <b-form-input id="form-module-input"
                        type="text"
                        v-model="addSensorForm.mod"
                        required
                        placeholder="Enter qualified module name">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-class-group"
                      label="Sensor Class:"
                      label-for="form-class-input">
          <b-form-input id="form-class-input"
                        type="text"
                        v-model="addSensorForm.cls"
                        required
                        placeholder="Enter class name">
          </b-form-input>
        </b-form-group>
        <div>
          <b-row>
            <b-col>
              <h5>Pin Out:</h5>
            </b-col>
            <b-col>
            <h5 class="text-right"><b-button variant='success' @click="onAddPinoutRowAdd()">
              <b-icon icon='plus-circle'/></b-button></h5>
            </b-col>
          </b-row>

          <b-table hover :items="addSensorForm.pinout" show-empty :fields="add_pin_fields">
            <template v-slot:cell(var)="row">
              <b-form-input v-model="row.item.var"/>
            </template>
            <template v-slot:cell(pin)="row">
              <b-form-input v-model="row.item.pin"/>
            </template>
            <template v-slot:cell(actions)="row">
              <b-button-group>
                <b-button variant='danger' @click="onDeletePinoutAdd(row.item)">
                <b-icon icon='x-circle'/></b-button>
              </b-button-group>
            </template>
          </b-table>
        </div>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>

    <b-modal ref="editSensorModal"
             id="edit-sensor-modal"
             title="Update Sensor"
             hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
        <b-form-group id="form-name-edit-group"
                      label="Name:"
                      label-for="form-name-edit-input">
          <b-form-input id="form-name-edit-input"
                        type="text"
                        v-model="editSensorForm.name"
                        required
                        placeholder="Enter sensor name">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-quantity-edit-group"
                      label="Measured Quantity:"
                      label-for="form-quantity-edit-input">
          <b-form-input id="form-quantity-edit-input"
                        type="text"
                        v-model="editSensorForm.quantity"
                        required
                        placeholder="Enter quantity">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-unit-edit-group"
                      label="Measurement Unit:"
                      label-for="form-unit-edit-select">
          <b-form-select id="form-unit-edit-select"
                         v-model="editSensorForm.unit"
                         :options="units">
          </b-form-select>
        </b-form-group>
        <b-form-group id="form-mod-edit-group"
                      label="Sensor Module:"
                      label-for="form-mod-edit-input">
          <b-form-input id="form-mod-edit-input"
                        type="text"
                        v-model="editSensorForm.mod"
                        required
                        placeholder="Enter qualified module name">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-class-edit-group"
                      label="Sensor Class:"
                      label-for="form-class-edit-input">
          <b-form-input id="form-class-edit-input"
                        type="text"
                        v-model="editSensorForm.cls"
                        required
                        placeholder="Enter class name">
          </b-form-input>
        </b-form-group>
        <div>
          <b-row>
            <b-col>
              <h5>Pin Out:</h5>
            </b-col>
            <b-col>
            <h5 class="text-right"><b-button variant='success' @click="onAddPinoutRowEdit()">
              <b-icon icon='plus-circle'/></b-button></h5>
            </b-col>
          </b-row>

          <b-table hover :items="editSensorForm.pinout" show-empty :fields="edit_pin_fields">
            <template v-slot:cell(var)="row">
              <b-form-input v-model="row.item.var"/>
            </template>
            <template v-slot:cell(pin)="row">
              <b-form-input v-model="row.item.pin"/>
            </template>
            <template v-slot:cell(actions)="row">
              <b-button-group>
                <b-button variant='danger' @click="onDeletePinoutEdit(row.item)">
                <b-icon icon='x-circle'/></b-button>
              </b-button-group>
            </template>
          </b-table>
        </div>
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

const API_URL = 'http://localhost:5000/api/';

export default {
  name: 'SensorConfig',
  data() {
    return {
      sensors: {},
      add_pin_fields: [
        { key: 'var', label: 'Var' },
        { key: 'pin', label: 'Pin' },
        { key: 'actions', label: 'Actions' },
      ],
      edit_pin_fields: [
        { key: 'var', label: 'Var' },
        { key: 'pin', label: 'Pin' },
        { key: 'actions', label: 'Actions' },
      ],
      units: [
        { value: 'Hz', text: 'Hertz (Hz)' },
        { value: 'kWh', text: 'Kilo-watt Hours (kWh)' },
        { value: 'J', text: 'Joules (J)' },
        { value: 'Db', text: 'Decibels (dB)' },
        { value: 'F', text: 'Degrees Farenheit (F)' },
        { value: 'C', text: 'Degrees Celcius (C)' },
      ],
      addSensorForm: {
        name: '',
        quantity: '',
        unit: '',
        module: '',
        cls: '',
        pinout: [],
      },
      editSensorForm: {
        id: '',
        name: '',
        quantity: '',
        unit: '',
        module: '',
        cls: '',
        pinout: [],
      },
    };
  },
  methods: {
    getData() {
      const path = `${API_URL}sensors`;
      axios.get(path, { headers: authHeader() })
        .then((res) => {
          this.sensors = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    initForm() {
      this.addSensorForm.name = '';
      this.addSensorForm.quantity = '';
      this.addSensorForm.unit = '';
      this.addSensorForm.mod = '';
      this.addSensorForm.class = '';
      this.addSensorForm.pinout = [];
      this.editSensorForm.id = '';
      this.editSensorForm.name = '';
      this.editSensorForm.quantity = '';
      this.editSensorForm.unit = '';
      this.editSensorForm.mod = '';
      this.editSensorForm.class = '';
      this.editSensorForm.pinout = [];
    },
    addSensor(payload) {
      const path = `${API_URL}sensors`;
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
    editSensor(sensor) {
      this.editSensorForm = sensor;
    },
    updateSensor(payload, sensorID) {
      const path = `${API_URL}sensors/${sensorID}`;
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
    removeSensor(sensorID) {
      const path = `${API_URL}sensors/${sensorID}`;
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
      this.$refs.addSensorModal.hide();
      const payload = {
        name: this.addSensorForm.name,
        quantity: this.addSensorForm.quantity,
        unit: this.addSensorForm.unit,
        module: this.addSensorForm.mod,
        cls: this.addSensorForm.cls,
        pinout: this.addSensorForm.pinout,
      };
      this.addSensor(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addSensorModal.hide();
      this.initForm();
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editSensorModal.hide();
      const payload = {
        name: this.editSensorForm.name,
        quantity: this.editSensorForm.quantity,
        unit: this.editSensorForm.unit,
        module: this.editSensorForm.mod,
        cls: this.editSensorForm.cls,
        pinout: this.editSensorForm.pinout,
      };
      this.updateSensor(payload, this.editSensorForm.id);
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editSensorModal.hide();
      this.initForm();
      this.getSensors();
    },
    onDeleteSensor(sensor) {
      this.removeSensor(sensor.id);
    },
    onAddPinoutRowEdit() {
      this.editSensorForm.pinout.push({ var: 'new', pin: -1 });
    },
    onAddPinoutRowAdd() {
      this.addSensorForm.pinout.push({ var: 'new', pin: -1 });
    },
    onDeletePinoutEdit(pinout) {
      // eslint-disable-next-line
      console.log("Pinout = " + pinout.var)
      this.editSensorForm.pinout.pop(pinout.var);
    },
    onDeletePinoutAdd(pinout) {
      this.addSensorForm.pinout.pop(pinout.var);
    },
  },
  created() {
    this.getData();
  },
};
</script>
