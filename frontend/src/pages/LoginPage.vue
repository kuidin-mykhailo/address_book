<template>
  <div id="app">
    <HeaderComponent/>
    <LoginComponent/>
  </div>
</template>

<script>

import HeaderComponent from "@/components/HeaderComponent";
import LoginComponent from "@/components/LoginComponent";

export default {
  name: "LoginPage",
  components: {HeaderComponent, LoginComponent}
}
</script>

<style scoped>

</style>