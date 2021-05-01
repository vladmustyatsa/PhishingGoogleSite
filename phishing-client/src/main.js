import Vue from 'vue'
import App from './App.vue'
import VueSocketIO from 'vue-socket.io'
import router from './router' 
Vue.use(new VueSocketIO({
    debug: true,
    connection: 'http://localhost:5000'
}))

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
