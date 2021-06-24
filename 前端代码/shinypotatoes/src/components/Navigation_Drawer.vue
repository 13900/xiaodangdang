<template>
    <v-navigation-drawer
        v-model="drawer"
        :expand-on-hover="drawer"
        :mini-variant="miniVariant"
        clipped
        app
        dark
      >
        <v-list
          nav
          app
          class="py-0"
        >
          <v-list-item
            v-for="item in items"
            :key="item.title"
            link
            :to="item.to"
          >
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>

        <v-list-item class="positioning" @click="logOut">
          <v-list-item-icon>
            <v-icon>mdi-exit-to-app</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
              <v-list-item-title>退出登录</v-list-item-title>
            </v-list-item-content>
        </v-list-item>
      </v-navigation-drawer>
</template>

<script>
import { mapState } from 'vuex'
export default {
  name: 'Navigation',
  data: () => ({
    permanent: true,
    miniVariant: true,
    items: [
      { title: '首页', icon: 'mdi-view-dashboard', to: '/' },
      { title: '计算机·IT', icon: 'mdi-certificate', to: '/internet' },
      { title: '文学', icon: 'mdi-library-shelves', to: '/literature' },
      { title: '童书', icon: 'mdi-library', to: '/children' },
      { title: '自然科学', icon: 'mdi-web', to: '/natural_sciences' },
      { title: '管理', icon: 'mdi-ship-wheel', to: '/ipConfig' }
    ]
  }),
  computed: {
    ...mapState(['drawer']),
    drawer: {
      get () {
        return this.$store.state.drawer
      },
      set (val) {
        this.$store.commit('SET_DRAWER', val)
      }
    }
  },
  methods: {
    logOut () {
      this.$store.commit('LOGOUT')
      console.info(localStorage.getItem('token'))
      this.$router.push('/login')
    }
  }
}
</script>

<style lang="scss" scoped>
    .positioning {
      position: absolute;
      width: 100%;
      bottom: 0;
    }
</style>
