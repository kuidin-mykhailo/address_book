<template>
  <div id="app">
    <HeaderComponent/>
    <MainComponent v-if="checkToken()"/>
    <div class="m-auto" v-else>Please login to get an access</div>
  </div>
</template>

<script>
import HeaderComponent from "@/components/HeaderComponent";
import MainComponent from "@/components/MainComponent";

export default {
  name: "MainPage",
  components: {
    MainComponent,
    HeaderComponent,
  },
  methods: {
    checkToken() {
      return localStorage.getItem('token') !== null
    }
  }
}
</script>

<style scoped>

</style>