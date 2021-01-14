import Vue from 'vue'
import Index from './Index.vue'
import router from './router.js'
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)

Vue.config.productionTip = false


new Vue({
  render: h => h(Index),
  router,
}).$mount('#app')
