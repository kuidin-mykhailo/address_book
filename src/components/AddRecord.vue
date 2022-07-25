<template>
  <form>
    <div class="container-md">
      <div class="row mb-4">
        <div class="col">
          <label for="city">City</label>
          <input class="form-control" id="city" aria-describedby="faxHelp" placeholder="Enter city"
          v-model="city">
        </div>
        <div class="col">
          <label for="fax">Address</label>
          <input class="form-control" id="address" aria-describedby="faxHelp" placeholder="Enter address"
                 v-model="address">
        </div>
      </div>
      <div class="row mb-4">
        <div class="col">
          <label for="inputFullName">First name</label>
          <input class="form-control" id="inputFullName" aria-describedby="fullNameHelp" placeholder="Enter first name"
                 v-model="first_name">
          <small id="fullNameHelp" class="form-text text-muted">Maximum 200 characters.</small>
        </div>
        <div class="col">
          <label for="inputLastName">Last name</label>
          <input class="form-control" id="inputLastName" aria-describedby="lastNameHelp" placeholder="Enter last name"
                 v-model="last_name">
          <small id="lastNameHelp" class="form-text text-muted">Maximum 200 characters.</small>
        </div>
      </div>
      <div class="form-group mb-2">
        <label for="inputEmail">Email</label>
        <input class="form-control" id="inputEmail" aria-describedby="emailHelp" placeholder="Enter email"
               v-model="email">
        <small id="emailHelp" class="form-text text-muted">Maximum 200 characters.</small>
      </div>
      <div class="form-group mb-2">
        <label for="homeNumber">Home number</label>
        <input class="form-control" id="homeNumber" aria-describedby="homeNumberHelp"
               placeholder="Enter home number (Optional)">
        <small id="homeNumberHelp" class="form-text text-muted">Maximum 15 characters.</small>
      </div>
      <div class="form-group mb-2">
        <label for="workNumber">Work number</label>
        <input class="form-control" id="workNumber" aria-describedby="workNumberHelp"
               placeholder="Enter work number (Optional)">
        <small id="workNumberHelp" class="form-text text-muted">Maximum 15 characters.</small>
      </div>
      <div class="form-group mb-2">
        <label for="fax">Fax</label>
        <input class="form-control" id="fax" aria-describedby="faxHelp" placeholder="Enter fax (Optional)">
      </div>
      <div class="col">
        <label for="fax">Zipcode</label>
        <input class="form-control" id="Zipcode" aria-describedby="ZipcodeHelp" placeholder="Enter zipcode"
               v-model="zipcode">
      </div>
      <button type="submit" class="btn btn-primary" v-on:click="submitForm">Submit</button>
    </div>
  </form>
</template>

<script>
import axios from "axios";

export default {
  name: "AddRecord",
  data() {
    return {
      first_name: '',
      last_name: '',
      email: '',
      home_number: '',
      work_number: '',
      fax: '',
      address: '',
      city: '',
      zipcode: ''
    }
  },
  methods: {
    submitForm() {
      const form_data = {
        'person_first_name': this.first_name,
        'person_last_name': this.last_name,
        'person_email': this.email,
        'home_number': this.home_number,
        'work_number': this.work_number,
        'fax': this.fax,
        'address': this.address,
        'city_name': this.city,
        'zipcode': this.zipcode
      }

      axios
          .post('/api/v1/address_book/', form_data)
          .catch(error => {
            window.alert(error.request.responseText)
          })
    }
  }
}
</script>

<style scoped>

</style>