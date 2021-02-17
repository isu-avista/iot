<template>
  <b-card header-tag='header'>
    <template #header>
      <b-row>
        <b-col><h3 style="float: left;">System Information</h3></b-col>
        <b-col>
          <h3 style="float: right;">
            <b-button-group>
              <b-button><b-icon icon="hdd"/></b-button>
              <b-button><b-icon icon="arrow-repeat"/></b-button>
              <b-button v-b-modal.sys-update-modal
               @click="editData()"><b-icon icon="pencil-square"/></b-button>
            </b-button-group>
          </h3>
        </b-col>
      </b-row>
    </template>
    <b-table hover :items='sys_data'></b-table>
    <br><br>
    <b-table hover :items='db_data'>
      <template v-slot:cell(db_item)="row">
        {{ row.item.item }}
      </template>
      <template v-slot:cell(value)="row" v-if="editable">
        <b-form-input v-model="row.item.value"/>
      </template>
      <template v-slot:cell(value)="row" v-else>
        {{ row.item.value }}
      </template>
    </b-table>
    <!--ConfigComp editable='False'/>-->
    <b-modal ref="editSysData"
             id="sys-update-modal"
             title="Update"
             hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
        <b-form-group id="form-equip-edit-group"
                      label="Equipment Monitored:"
                      label-for="form-equip-edit-input">
          <b-form-input id="form-equip-edit-input"
                        type="text"
                        v-model="editForm.equip"
                        required
                        placeholder="Enter equipment monitored">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-loc-edit-group"
                      label="Location:"
                      label-for="form-loc-edit-input">
          <b-form-input id="form-loc-edit-input"
                        type="text"
                        v-model="editForm.location"
                        required
                        placeholder="Enter equipment location">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-period-edit-group"
                      label="Data Collection Periodicity:"
                      label-for="form-period-edit-input">
          <b-form-input id="form-period-edit-input"
                        type="text"
                        v-model="editForm.period"
                        required
                        placeholder="Enter update periodicity">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-port-edit-group"
                      label="Server Port"
                      label-for="form-port-edit-input">
          <b-form-input id="form-port-edit-input"
                        type="number"
                        v-model="editForm.port"
                        required
                        placeholder="5000">
          </b-form-input>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </b-card>
</template>

<script>
// import ConfigComp from '@/config/ConfigComp.vue';
import axios from 'axios';
import authHeader from '@/services/auth-header';
import paths from '@/paths';

const host = `${window.location.protocol}//${window.location.hostname}`;

export default {
  name: 'SystemConfig',
  data() {
    return {
      sys_data: [],
      db_data: [],
      editable: false,
      editForm: {
        equip: '',
        location: '',
        period: '',
        port: 0,
      },
    };
  },
  components: {
    // ConfigComp,
  },
  methods: {
    setEditable() {
      this.editable = !this.editable;
    },
    save() {

    },
    refresh() {

    },
    getData() {
      const path = host + paths.systemCfg;
      //const path = 'http://localhost:5000/api/sysdata';
      axios.get(path, { headers: authHeader() })
        .then((res) => {
          this.sys_data = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    editData() {
      this.editForm = this.sys_data;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editSysData.hide();
      const payload = [
        { sys_item: 'System Identifier', value: this.sys_data[0].value },
        { sys_item: 'Equipment Monitored', value: this.editForm.equip },
        { sys_item: 'Location', value: this.editForm.location },
        { sys_item: 'Data Collection Periodicity', value: this.editForm.period },
        { sys_item: 'Server Port', value: this.editForm.port },
      ];
      this.updateData(payload, this.editForm.id);
    },
    updateData(payload) {
      const path = host + paths.systemCfg;
      //const path = 'http://localhost:5000/config/sysdata';
      axios.put(path, payload, { headers: authHeader() })
        .then(() => {
          this.getData();
          this.message = 'Configuration Updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getData();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editSysData.hide();
      this.initForm();
      this.getData();
    },
    initForm() {
      this.editForm.equip = '';
      this.editForm.location = '';
      this.editForm.period = '';
      this.editForm.port = 0;
    },
  },
  created() {
    this.getData();
  },
};
</script>
