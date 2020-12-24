<template>
  <b-container>
    <b-jumbotron class="text-center">
      <template #header>
        {{ currentUser.first_name }} {{ currentUser.last_name }}
      </template>

      <div class="text-left">
        <b-card title="Profile Information" class="mb-2">
          <b-card-text>
            <strong>Email Address: </strong>{{ currentUser.email }}
          </b-card-text>
          <b-card-text>
            <strong>Roles: </strong>
            <ul>
              <li>{{ currentUser.role }}</li>
            </ul>
          </b-card-text>
        </b-card>

        <b-card title="Token">
          <b-button v-b-toggle.collapse-1 variant="success">Show Token</b-button>
          <b-collapse id="collapse-1" class="mt-2">
            <b-card-text>
              {{ currentUser.token.substring(0, 20) }} ...
              {{ currentUser.token.substr(currentUser.token.length - 20) }}
            </b-card-text>
          </b-collapse>
        </b-card>
      </div>

    </b-jumbotron>
  </b-container>
</template>

<script>
export default {
  name: 'Profile',
  computed: {
    currentUser() {
      return this.$store.state.auth.user;
    },
  },
  mounted() {
    if (!this.currentUser) {
      this.$router.push('/login');
    }
  },
};
</script>
