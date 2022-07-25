<template>
  <div class="m-auto container-sm">
    <div class="input-group mb-3">
      <input type="text" class="form-control" placeholder="Search by name, surname or city"
             aria-label="Search by name, surname or city" aria-describedby="basic-addon2"
             v-model="searchField">
      <div class="input-group-append">
        <button class="btn btn-outline-secondary mx-2" type="button" v-on:click="getBySearch()">Search</button>
      </div>
    </div>
    <table class="table table-striped">
      <thead>
      <tr>
        <th scope="col">#</th>
        <th scope="col">Name</th>
        <th scope="col">Surname</th>
        <th scope="col">City</th>
        <th scope="col">Address</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="record in addressBookData" :key="record.id">
        <th scope="row">{{ record.id }}</th>
        <td>{{ record.person_first_name }}</td>
        <td>{{ record.person_last_name }}</td>
        <td>{{ record.city_name }}</td>
        <td>{{ record.address }}</td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "MainComponent",
  data() {
    return {
      addressBookData: null,
      searchField: ''
    }
  },
  methods: {
    getBySearch() {
      if (this.searchField === ''){
        this.getAddressBookData()
      } else {
        this.getAddressBookDataFiltered()
      }
    },
    getAddressBookData() {
      axios
          .get('/api/v1/address_book_compact')
          .then(response => {
            this.addressBookData = response.data.results
            console.log(this.addressBookData)
            console.log(response.data)
          })
          .catch(error => {
            console.log(error)
          })
    },
    getAddressBookDataFiltered() {
      axios
          .get('/api/v1/address_book_compact?search=' + this.searchField)
          .then(response => {
            this.addressBookData = response.data.results
            console.log(this.addressBookData)
            console.log(response.data)
          })
          .catch(error => {
            console.log(error)
          })
    }
  },

  async mounted() {
    await this.getAddressBookData();
  },

}
</script>

<style scoped>

</style>