import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    naem: 'Login',
    meta: {
      requiresAuth: true
    },
    component: () => import('../views/Login.vue')
  },
  {
    path: '/',
    name: 'Home',
    component: Home,
    children: [
      {
        path: '/',
        name: 'MainOne',
        component: () => import('../components/MainChildren/MainOne.vue')
      },
      {
        path: '/search',
        name: 'Search',
        component: () => import('../components/MainChildren/Search.vue')
      },
      {
        path: '/internet',
        name: 'BestSeller',
        meta: {
          requireAuth: true
        },
        component: () => import('../components/MainChildren/Internet.vue')
      },
      {
        path: '/literature',
        name: 'Literature',
        meta: {
          requireAuth: true
        },
        component: () => import('../components/MainChildren/literature.vue')
      },
      {
        path: '/children',
        name: 'Children',
        meta: {
          requireAuth: true
        },
        component: () => import('../components/MainChildren/children.vue')
      },
      {
        path: '/natural_sciences',
        name: 'NaturalSciences',
        meta: {
          requireAuth: true
        },
        component: () => import('../components/MainChildren/NaturalSciences.vue')
      },

      {
        path: '/ipConfig',
        name: 'IPConfig',
        component: () => import('../components/MainChildren/IPConfig.vue')
      }
    ]
  }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
