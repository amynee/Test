import Vue from 'vue'
import App from './App.vue'
import './assets/app.scss'
import router from './router'
sessionStorage.setItem('cart', JSON.stringify([]))

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
