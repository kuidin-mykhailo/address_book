<template>

  <div class="container-sm">
    <form >
      <!-- Email input -->
      <div class="form-outline mb-4">
        <input id="form2Example1" class="form-control" v-model="username"/>
        <label class="form-label" for="form2Example1">Username</label>
      </div>

      <!-- Password input -->
      <div class="form-outline mb-4">
        <input type="password" id="form2Example2" class="form-control" v-model="password"/>
        <label class="form-label" for="form2Example2">Password</label>
      </div>

      <!-- Submit button -->
      <button type="button" class="btn btn-primary btn-block m-auto" v-on:click="login()">Login in</button>
    </form>
  </div>
</template>

<script>

import axios from "axios";

export default {
  name: "LoginComponent",
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    login() {
      axios
          .post('auth/token/login', {username: this.username, password: this.password})
          .then(response => {
            const token = response.data.auth_token;
            axios.defaults.headers.common["Authorization"] = "Token " + token;
            localStorage.setItem("token", token);
            this.$router.push("/");
          })
    }
  }
}
</script>

<style scoped>

</style>