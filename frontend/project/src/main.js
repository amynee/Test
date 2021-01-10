import Vue from 'vue'
import App from './App.vue'
import './assets/app.scss'
import router from './router'
import VueSession from 'vue-session'
Vue.use(VueSession)


Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
