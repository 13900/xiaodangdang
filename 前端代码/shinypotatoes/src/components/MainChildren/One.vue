<template>
    <v-col class="pa-0" cols="12" ml='4' md="4">
        <div class="Basic">
            <h5 class="accent--text "><v-icon color="accent text--accent-4">mdi-pac-man</v-icon>基本信息</h5>
            <h5 class="indigo--text text--lighten-4">当你征服一座山峰时，它已经在你脚下了，你必须再找一座山峰去征服，否则，你只有下山，走下坡路了</h5>
                    <v-col cols="12" class="pa-1 indigo--text text--lighten-1">
                        <div class="d-inline ml-3">目标网站：{{ Website }}</div>
                        <div class="d-inline ml-3">畅销总量：{{ BestSelling }}本</div>
                    </v-col>

                    <v-col cols="12" class="ma-0 pa-1 indigo--text text--lighten-1">
                            <div class="d-inline ml-3">代理网站: {{ Ipweb }}</div>
                            <div class="d-inline ml-3">IP可用量：{{ IpNumber }}</div>
                    </v-col>
        </div>
            <v-row>
              <v-col cols="12">
              <div ref="box1" class="box1"></div>
              </v-col>
            </v-row>
    </v-col>
</template>
<script>
export default {
  name: 'One',
  data: () => ({
    Website: '当当',
    BestSelling: '',
    Ipweb: '西刺代理',
    IpNumber: '',
    dat: []
  }),
  methods: {
    get_tet () {
      this.$axios.get('/all/data').then((req) => {
        this.IpNumber = req.data.ip
        this.BestSelling = req.data.sum
      })
    },
    get_dat () {
      this.$axios.get('/dangdang/hotList').then((req) => {
        const ipApi = req.data
        this.dat = ipApi
        console.info(this.dat)
        this.init_echar()
      })
    },
    init_echar () {
      const option = {
        title: {
          text: '热搜榜',
          left: 'center',

          textStyle: {
            color: '#ccc'
          }
        },
        tooltip: {
          trigger: 'item',
          formatter: '{a} <br/>{b}: {c} ({d}%)'
        },
        series: [
          {
            name: '人气',
            type: 'pie',
            radius: ['50%', '70%'],
            avoidLabelOverlap: false,
            label: {
              show: false,
              position: 'center'
            },
            emphasis: {
              label: {
                show: true,
                fontSize: '30',
                fontWeight: 'bold'
              }
            },
            labelLine: {
              show: false
            },
            data: this.dat
          }
        ]
      }
      const myEchar = this.$echarts.init(this.$refs.box1)
      myEchar.setOption(option)
      window.onresize = function () {
        myEchar.resize()
      }
    }
  },
  mounted () {
    this.get_tet()
    this.get_dat()
  }
}
</script>

<style lang="scss" scoped>
    .Basic {
        border: 2px solid yellowgreen;
        border-radius: 3px;
        li {
            list-style: none;
            font-size: .2rem;
            color: rgb(29, 17, 17);
            width: 50%;
            height: .4rem;
            line-height: .4rem;
            padding: .2rem;
        }
    }

    .box1 {
        margin: auto;
        width: 360px;
        height: 300px;

    }
</style>
