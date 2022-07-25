import { createApp } from 'vue'
import App from './App.vue'
import axios from "axios";
import router from './router/index'

import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"

axios.defaults.baseURL = 'http://django'

if (localStorage.getItem("token") !== null){
    axios.defaults.headers.common["Authorization"] = "Token " + localStorage.getItem("token");
}

createApp(App).use(router).mount('#app')
