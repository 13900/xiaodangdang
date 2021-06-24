<template>
<div fluid class="One">
        <One></One>
        <Twe></Twe>
</div>
</template>
<script>
export default {
  name: 'MainOne',
  data: () => ({

  }),
  components: {
    One: () => import('../MainChildren/One.vue'),
    Twe: () => import('../MainChildren/Twe.vue')
  }
}
</script>

<style lang="scss" scoped>
    .One {
        display: flex;
        flex-wrap: wrap;
    }
</style>
