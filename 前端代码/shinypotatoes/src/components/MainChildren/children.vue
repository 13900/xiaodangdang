<template>
<div>
<div class="d-flex flex-wrap" v-for="(its, y) in items" :key="y">

<v-col cols="12" md="6" lg="6"
          v-for="(item, i) in its"
          :key="i"
        >
          <v-card
            :color="item.color"
            dark
          >
            <div class="d-flex flex-wrap justify-space-between">
              <div>
                  <v-chip
      class="ma-2"
      color="green"
      text-color="white"
    >
      <v-avatar
        left
        class="green darken-4"
      >
        {{item.id}}
      </v-avatar>
      {{item.chip}}
    </v-chip>

                <v-card-title
                  class="headline"
                  v-text="item.title"
                ></v-card-title>
                <v-card-subtitle class="pt-2 pb-0" v-text="item.name"></v-card-subtitle>
                <v-card-subtitle class="pt-0 pb-2" v-text="item.artist"></v-card-subtitle>

    <div class="ml-4">
    <v-dialog
      v-model="item.dialog"
      width="500"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn elevation="0"
          color="red lighten-2"
          small
          dark
          v-bind="attrs"
          v-on="on"
        >
        <v-icon left>mdi-cloud-upload</v-icon>
          URL
        </v-btn>
      </template>

      <v-card elevation="0">
        <v-card-title
          class="headline grey lighten-2"
          primary-title
        >
         {{item.url}}
        </v-card-title>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            @click="item.dialog = !item.dialog"
          >
           关闭
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
              </div>

              <v-avatar
                class="ma-3"
                size="125"
                tile
              >
                <v-img :src="item.src"></v-img>
              </v-avatar>
            </div>
            <v-card-actions>
      <v-spacer></v-spacer>

      <v-btn
        icon
        @click="dat(item.option, i, y); item.show = !item.show"
      >
        <v-icon>{{ item.show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
      </v-btn>
    </v-card-actions>
            <v-expand-transition>
                <div v-show="item.show">
                <v-divider></v-divider>
                <v-col cols="12">
                <div class="da d-flex" ref="lis"></div>
                </v-col>
             </div>
            </v-expand-transition>
          </v-card>
        </v-col>

    <v-card class="text-center flex" v-if="load">
      <v-progress-circular
      :width="3"
      color="amber"
      indeterminate
    ></v-progress-circular>

    <v-progress-circular
      :width="5"
      :size="50"
      color="red"
      indeterminate
      class="dlex"
    ></v-progress-circular>
    <v-progress-circular
      :width="3"
      color="green"
      indeterminate
    ></v-progress-circular>
    </v-card>
  </div>
  </div>
</template>

<script>
export default {
  data: () => ({
    items: [],
    load: false,
    page3: 0
  }),
  methods: {
    get_dat () {
      this.$axios.get('/dangdang/children',
        {
          params: { page3: this.page3 }
        }).then((req) => {
        const ipApi = req.data
        this.items.push(ipApi)
        this.load = false
        this.page3 = this.page3 + 1
      })
    },
    dat (option, i, y) {
      const index = i + (y * 20)
      var myEchar = this.$echarts.init(this.$refs.lis[index])
      myEchar.setOption(option)
      window.onresize = function () {
        myEchar.resize()
      }
    },
    scroll3 () {
      window.onscroll = () => {
        const bottomOfWindow = document.documentElement.offsetHeight - document.documentElement.scrollTop - window.innerHeight <= 5
        if (bottomOfWindow) {
          this.load = true
          this.get_dat()
        }
      }
    }
  },
  created () {
    this.get_dat()
  },
  mounted () {
    window.addEventListener('scroll', this.scroll3(), true)
  },
  destroyed () {
    window.removeEventListener('scroll', this.scroll3(), true)
  }
}
</script>

<style lang="scss" scoped>
    .da {
        margin: auto;
        width: 300px;
        height: 300px;
    }
</style>
