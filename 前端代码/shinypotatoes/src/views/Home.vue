<template>
  <v-app>
    <AppBer></AppBer>
    <NavigationDrawer></NavigationDrawer>
    <Main></Main>
    <Footer></Footer>
  </v-app>
</template>

<script>
export default {
  name: 'Home',
  data: () => ({
  }),
  components: {
    AppBer: () => import('../components/AppBer.vue'),
    NavigationDrawer: () => import('../components/Navigation_Drawer.vue'),
    Main: () => import('../components/Main.vue'),
    Footer: () => import('../components/Footer.vue')
  }
}
</script>
