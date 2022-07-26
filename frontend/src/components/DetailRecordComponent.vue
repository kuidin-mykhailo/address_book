<template>
  <form v-on:submit.prevent="onSubmit">
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
               placeholder="Enter home number (Optional)"
        v-model="home_number">
        <small id="homeNumberHelp" class="form-text text-muted">Maximum 15 characters.</small>
      </div>
      <div class="form-group mb-2">
        <label for="workNumber">Work number</label>
        <input class="form-control" id="workNumber" aria-describedby="workNumberHelp"
               placeholder="Enter work number (Optional)"
        v-model="work_number">
        <small id="workNumberHelp" class="form-text text-muted">Maximum 15 characters.</small>
      </div>
      <div class="form-group mb-2">
        <label for="fax">Fax</label>
        <input class="form-control" id="fax" aria-describedby="faxHelp" placeholder="Enter fax (Optional)"
        v-model="fax">
      </div>
      <div class="col my-2">
        <label for="fax">Zipcode</label>
        <input class="form-control" id="Zipcode" aria-describedby="ZipcodeHelp" placeholder="Enter zipcode"
               v-model="zipcode">
      </div>
      <button type="submit" class="btn btn-primary">Update</button>
      <button class="btn btn-danger mx-4" v-on:click="deleteRecord">Delete</button>
    </div>
  </form>
</template>

<script>
import axios from "axios";

export default {
  name: "DetailRecordComponent",
  data() {
    return {
      recordId: null,
      cityId: null,
      personId: null,
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
  async mounted() {
    await this.getRecord();
  },
  methods: {
    getRecord() {
      this.recordId = this.$route.params.id
      axios
          .get('/api/v1/address_book/' + this.recordId + '/')
          .then(response => {
            console.log(response);
            this.cityId = response.data.city.id;
            this.city = response.data.city.name;
            this.personId = response.data.person.id;
            this.first_name = response.data.person.first_name;
            this.last_name = response.data.person.last_name;
            this.email = response.data.person.email;
            this.home_number = response.data.person.home_number;
            this.work_number = response.data.person.work_number;
            this.fax = response.data.person.fax;
            this.address = response.data.address;
            this.zipcode = response.data.zipcode;
          })
          .catch(error => {
            window.alert(error)
          })
    },

    deleteRecord() {
      axios
          .delete('api/v1/address_book/' + this.recordId + '/')
          .then(response => {
            if (response.status === 204) {
              window.alert('Successfully deleted!')
              this.$router.push("/");
            }
          })
          .catch(error => {
            window.alert(error)
          });
    },

    onSubmit() {
      const form_data = {
        'city': this.cityId,
        'person': this.personId,
        'address': this.address,
        'zipcode': this.zipcode
      }

      const city_data = {
        'id': this.cityId,
        'name': this.city,
      }

      const person_data = {
        'first_name': this.first_name,
        'last_name': this.last_name,
        'home_number': this.home_number,
        'work_number': this.work_number,
        'fax': this.fax,
        'email': this.email
      }
      axios
          .post('/api/v1/city/', city_data)
          .then(response => {
            console.log(response)
            this.cityId = response.data.city.id;
          })
          .catch(error => {
            window.alert(error.request.responseText)
          })

      axios
          .patch('/api/v1/person/' + this.personId + '/', person_data)
          .then(response => {
            console.log(response)
          })
          .catch(error => {
            window.alert(error.request.responseText)
          })

      axios
          .patch('/api/v1/address_book/' + this.recordId + '/', form_data)
          .then(response => {
            console.log(response.status)
            console.log(response.status === 201)
            if (response.status === 201) {
              window.alert("Successfully updated.")
            }
          })
          .catch(error => {
            window.alert(error.request.responseText)
          })
    }
  }
}
</script>

<style scoped>

</style>