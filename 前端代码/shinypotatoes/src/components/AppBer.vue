<template>
  <v-app-bar
        app
        dark
        clipped-left

      >
        <v-app-bar-nav-icon @click.stop="setDrawer(!drawer)"></v-app-bar-nav-icon>
        <v-toolbar-title>ShinyPotatoes</v-toolbar-title>
<v-spacer></v-spacer>
      <v-col cols="6" md="4" lg="4">
        <router-link class="link" to="/search">
        <v-text-field
            color="pink"
            flat
            hide-details
            prepend-inner-icon="mdi-magnify"
            clearable
            max-width="370"
            label="商品搜索"
            outlined
            dense
          ></v-text-field>
        </router-link>
      </v-col>
  </v-app-bar>
</template>

<script>
import { mapState, mapMutations } from 'vuex'
export default {
  name: 'AppBer',
  data: () => ({

  }),
  computed: {
    ...mapState(['drawer'])
  },
  methods: {
    ...mapMutations({
      setDrawer: 'SET_DRAWER'
    })
  }
}
</script>

<style lang="scss" scoped>
  .link {
    text-decoration: none;
  }
</style>
