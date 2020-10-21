import Vue from 'vue'
import Index from './Index.vue'
import router from './router.js'

Vue.config.productionTip = false

new Vue({
  render: h => h(Index),
  router,
}).$mount('#app')
