<template>
  <div class="mb-3">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <a class="navbar-brand mx-2" href="#">Address Book</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
              aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item active">
            <router-link class="nav-link" :to="{ name: 'main'}">Dashboard</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'add' }">Add Record</router-link>
          </li>
        </ul>
      </div>
      <button class="btn btn-dark" v-if="checkToken()" v-on:click="logout()">
        <span>Logout</span>
      </button>
      <button class="btn btn-dark" v-else>
        <router-link to="login"
                     class="nav-link mx-2"
        >Login
        </router-link>
      </button>
    </nav>
  </div>
</template>

<script>

import axios from "axios";

export default {
  name: "HeaderComponent",
  methods: {
    logout() {
      localStorage.removeItem('token');
      delete axios.defaults.headers.common["Authorization"];
      location.reload();
    },
    checkToken() {
      return localStorage.getItem('token') !== null
    }
  }
}
</script>

<style scoped>

</style>