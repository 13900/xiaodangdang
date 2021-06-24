import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import echarts from 'echarts'
import http from './utils/http'

Vue.prototype.$echarts = echarts
Vue.prototype.$axios = http
http.defaults.withCredentials = true

router.beforeEach((to, from, next) => {
  if (to.path === '/login') {
    next()
  } else {
    const token = localStorage.getItem('token')

    if (token === '' || token === null) {
      alert('请登录访问')
      next('/login')
    } else {
      next()
    }
  }
})
Vue.config.productionTip = false

new Vue({
  http,
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
