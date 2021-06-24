<template>
  <v-app class="grey darken-4">
    <router-view></router-view>
  </v-app>
</template>

<script>
export default {
  name: 'App',
  data: () => ({
    //
  })
}
</script>

<style lang="scss">
  html, body, *{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    cursor: url('./assets/img/pencil.png'), default;
  }
</style>
