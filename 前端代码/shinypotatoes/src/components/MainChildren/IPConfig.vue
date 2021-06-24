<template>
<v-card>
<!--  -->
    <r-row
        justify="center"
        align="center">
      <v-chip-group
        column
        multiple
      >
        <!-- <v-chip :filter='show1' outlined @click="dat_init">数据库初始化</v-chip> -->
        <v-chip :filter='show1' outlined @click="ip_scrip">IP代理蜘蛛</v-chip>
        <v-chip :filter='show1' outlined @click="hot_scrip">热搜榜蜘蛛</v-chip>
        <v-chip :filter='show1' outlined @click="praise_scrip">好评榜蜘蛛</v-chip>
        <v-chip :filter='show1' outlined @click="internet_scrip">互联网·IT榜蜘蛛</v-chip>
        <v-chip :filter='show1' outlined @click="literature_scrip">文学榜蜘蛛</v-chip>
        <v-chip :filter='show1' outlined @click="children_scrip">童书榜蜘蛛</v-chip>
        <v-chip :filter='show1' outlined @click="natural_scrip">自然科学榜蜘蛛</v-chip>
      </v-chip-group>
    </r-row>
<!--  -->
  <v-card-title>
      IP池管理
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Search"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
  <v-data-table
    :headers="headers"
    :items="IPPOOL"
    :search="search"
    sort-by="calories"
    class="elevation-1"
  >
    <template v-slot:[`item.actions`]="{ item }">
        存活
      <v-icon
        small
        @click="deleteItem(item)"
      >
        mdi-delete
      </v-icon>
    </template>
  </v-data-table>
</v-card>

</template>

<script>
export default {
  data: () => ({
    show1: false,
    circu1: false,
    show2: false,
    show3: false,
    alert: false,
    msg: '',
    dialog: false,
    search: '',
    headers: [
      {
        text: 'IP',
        align: 'start',
        sortable: false,
        value: 'name'
      },
      { text: '代理位置', value: 'AgentLocation' },
      { text: '代理类型', value: 'AgentType' },
      { text: 'Actions', value: 'actions', sortable: false }
    ],
    IPPOOL: [],
    editedIndex: -1,
    editedItem: {
      name: '',
      AgentLocation: 0,
      AgentType: 0
    },
    defaultItem: {
      name: '',
      AgentLocation: 0,
      AgentType: 0
    }
  }),
  created () {
    this.get_dat()
  },
  methods: {
    get_dat () {
      this.$axios.get('/ip/Inquire').then((req) => {
        const ipApi = req.data
        this.IPPOOL = ipApi
      })
    },
    // dat_init () {
    //   this.circu1 = true
    //   this.$axios.get('/data/init').then((req) => {
    //     const datApi = req.data
    //     console.log('dddd')
    //     console.log(datApi)
    //     this.circu1 = false
    //     this.show1 = !this.show1
    //   })
    // },
    ip_scrip () {
      this.$axios.get('/ip/add').then((req) => {
        const ipApi = req.data
        alert(ipApi)
      })
    },
    hot_scrip () {
      this.$axios.get('/dangdang/hot_spider').then((req) => {
        const ipApi = req.data
        alert(ipApi)
      })
    },
    praise_scrip () {
      this.$axios.get('/dangdang/praise_spdier').then((req) => {
        const ipApi = req.data
        alert(ipApi)
      })
    },
    internet_scrip () {
      this.$axios.get('/dangdang/internet_spider').then((req) => {
        const ipApi = req.data
        alert(ipApi)
      })
    },
    literature_scrip () {
      this.$axios.get('/dangdang/literature_spider').then((req) => {
        const ipApi = req.data
        alert(ipApi)
      })
    },
    children_scrip () {
      this.$axios.get('/dangdang/children_spider').then((req) => {
        const ipApi = req.data
        alert(ipApi)
      })
    },
    natural_scrip () {
      this.$axios.get('/dangdang/natural_sciences_spider').then((req) => {
        const ipApi = req.data
        alert(ipApi)
      })
    },
    deleteItem (item) {
      const index = this.IPPOOL.indexOf(item)
      var judgment = confirm('您确定要删除此IP？')
      if (judgment === true) {
        console.log(this.IPPOOL[index].name)
        const ip = this.IPPOOL[index].name
        this.$axios.post('/ip/del', {
          address: ip
        }).then((req) => {
          const delMsg = req.data
          console.info(delMsg)
        })
        this.IPPOOL.splice(index, 1)
      } else {
        console.log('取消删除IP')
      }
    }
  }
}
</script>
