import axios from 'axios'
import router from '../router'
import store from '../store'

const instance = axios.create({
  baseURL: '/api',
  timeout: 500000
})

instance.interceptors.request.use(
  config => {
    console.info(store.state.Authorization)
    if (localStorage.getItem('token')) {
      config.headers.authorization = `${localStorage.getItem('token')}`
    }
    return config
  },
  err => {
    return Promise.reject(err)
  }
)

instance.interceptors.response.use(
  response => {
    return response
  },
  error => {
    if (error.response) {
      switch (error.response.status) {
        case 401:
          //  返回401末认正， 清除token信息
          this.store.commit('LOGOUT')
          router.replace({
            path: 'login',
            query: { redirect: router.currentRoute.fullPath }
          })
      }
    }
    return Promise.reject(error.response.data) // 返回接口返回的错误信息
  }
)

export default instance
