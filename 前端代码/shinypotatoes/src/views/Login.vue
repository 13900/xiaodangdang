<template>
    <v-row class="blue-grey darken-3" align="center" justify="center">
    <v-col cols="12">
      <v-expand-transition>
        <v-card
          v-if="show2"
          class="mx-auto lime darken-4"
          max-width="500"
        >
          <v-card-title class="title font-weight-regular justify-space-between white--text">
            <span>{{ currecntRegTitle }}</span>
            <v-avatar
              color="primary lighten-2"
              class="subheading white--text"
              size="24"
              v-text="step"
            ></v-avatar>
          </v-card-title>

          <v-window v-model="step">
            <v-window-item :value="1">
              <v-card-text class="white--text">
                <v-text-field
                  label="电子邮件"
                  v-model="regEmaill"
                  class="white--text"
                  color="white"
                ></v-text-field>
                <span class="caption black--text">
                 这是您将用来登录Vuetify帐户的电子邮件
                </span>
              </v-card-text>
            </v-window-item>

            <v-window-item :value="2">
              <v-card-text>
                <v-text-field
                  label="密码"
                  type="password"
                  color="white"
                  v-model="regPwd"
                ></v-text-field>
                <v-text-field
                  label="确认密码"
                  type="password"
                  color="white"
                  v-model="regPwd2"
                ></v-text-field>
                <span class="caption black--text">
                  请输入您的帐户密码
                </span>
              </v-card-text>
            </v-window-item>

            <v-window-item :value="3">
              <div class="pa-4 text-center">
                <v-img
                  class="mb-4"
                  contain
                  height="128"
                ></v-img>
                <h3 class="title font-weight-light mb-2">欢迎来到potatoes</h3>
                <span class="caption grey--text">感谢您的注册！</span>
              </div>
            </v-window-item>
          </v-window>

          <v-divider></v-divider>

          <v-card-actions class="brown darken-2">
            <v-btn v-if="step != 1"
              text
              @click="step--"
            >
              上一步
            </v-btn>

            <v-btn v-if="step === 1"
              class="purple darken-1 white--text"
              text
              @click="turnPage"
            >
              登录
            </v-btn>

            <v-spacer></v-spacer>
            <v-btn
              v-if="step != 3"
              color="primary"
              depressed
              @click="step++"
            >
              下一步
            </v-btn>

            <v-btn
              v-if="step === 3"
              color="primary"
              depressed
              @click="registered"
            >
              提交
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-expand-transition>
      <!-- dfdf -->
      <v-expand-transition>
        <v-card
          v-if="show"
          class="mx-auto light-green lighten-3"
          max-width="500"
        >
          <v-card-title class="title font-weight-regular justify-space-between">
            <span>{{ currentLogTitle }}</span>
            <v-avatar
              color="primary lighten-2"
              class="subheading white--text"
              size="24"
              v-text="step"
            ></v-avatar>
          </v-card-title>

          <v-window v-model="step">
            <v-window-item :value="1">
              <v-card-text>
                <v-text-field
                  label="电子邮件"
                  v-model="logEmaill"
                ></v-text-field>
                <span class="caption grey--text text--darken-1">
                 请输入你注册的电子邮件
                </span>
              </v-card-text>
            </v-window-item>

            <v-window-item :value="2">
              <v-card-text>
                <v-text-field
                  label="密码"
                  type="password"
                  v-model="logPwd"
                ></v-text-field>
                <span class="caption grey--text text--darken-1">
                  请输入您的帐户密码
                </span>
              </v-card-text>
            </v-window-item>

            <v-window-item :value="3">
              <div class="pa-4 text-center">
                <v-img
                  class="mb-4"
                  contain
                  height="128"
                ></v-img>
                <h3 class="title font-weight-light mb-2">欢迎来到potatoes</h3>
                <span class="caption grey--text">欢迎你的登录</span>
              </div>
            </v-window-item>
          </v-window>

          <v-divider></v-divider>

          <v-card-actions class="lime darken-2">
            <v-btn v-if="step != 1"
              text
              @click="step--"
            >
              上一步
            </v-btn>

            <v-btn v-if="step === 1"
              class="purple darken-1 white--text"
              text
              @click="turnPage"
            >
              注册
            </v-btn>

            <v-spacer></v-spacer>
            <v-btn
              v-if="step != 3"
              color="primary"
              depressed
              @click="step++"
            >
              下一步
            </v-btn>
            <v-btn
              v-if="step === 3"
              color="primary"
              depressed
              @click="login"
            >
              登录
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-expand-transition>
    </v-col>
    </v-row>
</template>

<script>
export default {
  data: () => ({
    step: 1,
    alert: false,
    show: true,
    show2: false,
    logEmaill: '',
    logPwd: '',
    regEmaill: '',
    regPwd: '',
    regPwd2: ''
  }),
  computed: {
    currentLogTitle () {
      switch (this.step) {
        case 1: return '登录'
        case 2: return '输入密码'
        default: return '欢迎登录'
      }
    },
    currecntRegTitle () {
      switch (this.step) {
        case 1: return '注册'
        case 2: return '创建一个密码'
        default: return '帐户已建立'
      }
    }
  },
  methods: {
    turnPage () {
      this.show = !this.show
      this.show2 = !this.show2
      this.logEmaill = ''
      this.logPwd = ''
      this.regEmaill = ''
      this.regPwd = ''
      this.regPwd2 = ''
    },
    registered () {
      if (this.regEmaill !== '' && this.regEmaill !== null && this.regPwd !== '' && this.regPwd !== null && this.regPwd2 !== '' & this.regPwd2 !== null) {
        this.$axios.post('/registered', {
          email: this.regEmaill,
          password: this.regPwd
        }).then((req) => {
          const api = req.data
          console.info(api)
          this.$router.go(0)
        })
      } else {
        this.alert = true
      }
    },
    login () {
      this.$axios.post('/login', {
        email: this.logEmaill,
        password: this.logPwd
      }).then((req) => {
        const logApi = req.data
        this.$store.commit('LOGIN', logApi)
        localStorage.setItem('stoken', logApi)
        this.$router.push('/')
      })
    }
  }
}
</script>

<style lang="scss" scoped>
    .ff {
      float: top;
    }
</style>
