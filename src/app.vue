<template>
  <div id="topbar">
    <img src="@/assets/home.png"
         alt=""
         @click="home"/>
    <span>
      哔咔漫画
    </span>
    <img src="@/assets/setting.png"
         alt=""
         @click="setting"/>
  </div>
  <router-view v-if="!authing"/>
</template>

<script>
import { globals, request } from '@/util'
import axios from 'axios'

export default {
  name: 'app',
  data() {
    return {
      authing: true,
    }
  },
  mounted() {
    this.$router.afterEach(to => {
      if (!this.authing && !globals.authed && to.path !== '/setting') {
        this.$router.push('/setting')
      }
    })
    let server = localStorage.getItem('server') ?? ''
    let key = localStorage.getItem('key') ?? ''
    axios.defaults.baseURL = server
    request('/auth', {
      key: key,
    }, () => {
      globals.authed = true
      this.authing = false
    }, () => {
      this.setting()
      this.authing = false
    })
  },
  methods: {
    home() {
      this.$router.push('/')
    },
    setting() {
      this.$router.push('/setting')
    }
  },
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  cursor: pointer;
}

body {
  background: #ffc0cb08;
}

#topbar {
  display: flex;
  background: #ec75a1;
}

#topbar > img {
  width: 25px;
  height: 25px;
  padding: 10px;
}

#topbar > span {
  flex-grow: 1;
  color: #ffffff;
  font-size: 20px;
  line-height: 45px;
}
</style>
