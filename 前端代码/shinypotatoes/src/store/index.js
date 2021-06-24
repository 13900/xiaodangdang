import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    drawer: null,
    Authorization: null
  },
  mutations: {
    SET_DRAWER (state, payload) {
      state.drawer = payload
    },
    LOGIN (state, data) {
      localStorage.setItem('token', data)
      state.Authorization = data
    },
    LOGOUT (state) {
      localStorage.removeItem('token')
      state.Authorization = null
    }
  },
  actions: {
  },
  modules: {
  }
})
