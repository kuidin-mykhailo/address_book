import {createRouter, createWebHashHistory } from "vue-router";
import LoginPage from "@/pages/LoginPage";
import MainPage from "@/pages/MainPage";
import AddRecordPage from "@/pages/AddRecordPage";

const routes = [
    {
        path: '/login',
        component: LoginPage
    },
    {   path: '/add',
        component: AddRecordPage},
    {
        path: '/',
        component: MainPage
    }]

const router = createRouter({
    history: createWebHashHistory(),
    routes,
})

export default router

