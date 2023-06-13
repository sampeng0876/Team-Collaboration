import SignupPage from '../components/SignupPage.vue';
import LoginPage from '../components/LoginPage.vue';
import HomePage from '../components/HomePage.vue';
import { createRouter, createWebHistory } from 'vue-router';



const routes = [
  {
    name: 'Home',
    path: '/',
    component: HomePage
  },
  {
    name: 'Signup',
    path: '/signup',
    component: SignupPage
  },
  {
    name: 'Login',
    path: '/login',
    component: LoginPage
  },

  // Add any additional routes as needed
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
