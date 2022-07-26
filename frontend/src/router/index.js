import {createRouter, createWebHistory} from "vue-router";
import LoginPage from "@/pages/LoginPage";
import MainPage from "@/pages/MainPage";
import AddRecordPage from "@/pages/AddRecordPage";
import DetailRecordPage from "@/pages/DetailRecordPage";

const routes = [
    {
        path: '/login',
        component: LoginPage
    },
    {   path: '/detail/:id/',
        component: DetailRecordPage,
        name: 'detail'
    },
    {   path: '/add',
        component: AddRecordPage,
        name: 'add'
    },
    {
        path: '/',
        component: MainPage,
        name: 'main'
    }]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router

