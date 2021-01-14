import Vue from 'vue';
import Router from 'vue-router';
import Ping from './components/Ping.vue';
import Home from './components/Home.vue'

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      // this is just for testing
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
    {
      // Change component to actual home page
      path: '/',
      name: 'Hello World',
      component: Home,
    }
  ],
});
