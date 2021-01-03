<template>
  <b-card title="System Status">
    <b-card-text>
      <div v-for="item in items" :key="item.id">
        <b-row>
          <b-col>
            <p class="text-left">{{ item.name }}</p>
          </b-col>
          <b-col>
            <h3 class="text-right"><b-icon :icon="item.icon" :variant="item.variant"/></h3>
          </b-col>
        </b-row>
      </div>
    </b-card-text>
  </b-card>
</template>

<script>
import axios from 'axios';
import authHeader from '@/services/auth-header';
import paths from '@/paths';

export default {
  name: 'Status',
  data() {
    return {
      items: [],
      icons: ['slash-circle', 'exclamation-circle', 'check-circle'],
      variants: ['danger', 'warning', 'success'],
    };
  },
  methods: {
    getData() {
      const path = paths.status;
      axios.get(path, { headers: authHeader() })
        .then((res) => {
          this.items = [];
          res.data.forEach((d) => {
            this.items.push({
              id: d.id,
              name: d.name,
              icon: this.icons[d.value],
              variant: this.variants[d.value],
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
