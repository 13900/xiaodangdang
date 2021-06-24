<template>
    <v-col cols="12" md="8" ml="8" class="pa-0">
      <v-card elevation="0">
        <div class="tew" ref="box">
        </div>
      </v-card>
    </v-col>

</template>

<script>
export default {
  name: 'Twe',
  data: () => ({
    id: [],
    variance: [],
    comment: [],
    good_comment: []
  }),
  mounted () {
    this.get_praise()
  },
  methods: {
    get_praise () {
      this.$axios.get('/dangdang/prase').then((req) => {
        this.id = req.data[0]
        this.comment = req.data[1]
        this.good_comment = req.data[2]
        this.variance = req.data[3]
        this.init_echarts()
      })
    },
    init_echarts () {
      const option = {
        title: {
          text: '好评榜',
          color: '#81C784'
        },
        tooltip: {
          trigger: 'axis'
        },
        legend: {
          data: ['总评', '五星好评', '方差']
        },
        xAxis: [
          {
            type: 'category',
            data: this.id,
            axisPointer: {
              type: 'shadow'
            }
          }
        ],
        yAxis: [
          {
            type: 'value',
            name: '评论人数',
            interval: 30000,
            axisLabel: {
              name: '评论人数',
              formatter: '{value} 人',
              color: '#FF6E40'
            }
          },
          {
            type: 'value',
            name: '方差',
            interval: 3000,
            axisLabel: {
              formatter: '{value}',
              color: '#F5F5F5'
            },
            color: '#F5F5F5'
          }
        ],
        series: [
          {
            name: '总评',
            type: 'bar',
            data: this.comment,
            color: '#81C784'
          },
          {
            name: '五星好评',
            type: 'bar',
            data: this.good_comment
          },
          {
            name: '方差',
            type: 'line',
            yAxisIndex: 1,
            data: this.variance,
            color: '#BDBDBD'
          }
        ]
      }

      var myEchar = this.$echarts.init(this.$refs.box, 'dark')
      myEchar.setOption(option)
      window.onresize = function () {
        myEchar.resize()
      }
    }
  }
}
</script>

<style lang="scss" scoped>
  .tew {

    float: left;
    width: 100%;
    height: 550px;
  }

</style>
