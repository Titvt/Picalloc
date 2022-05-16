<template>
  <div class="group">
    <span class="title">
      | 服务器设置
    </span>
    <span class="succ msg" v-if="authSuccMsg!==''">
      {{ authSuccMsg }}
    </span>
    <span class="fail msg" v-else-if="authFailMsg!==''">
      {{ authFailMsg }}
    </span>
    <span class="msg" v-else>
      {{ authMsg }}
    </span>
    <input type="text"
           placeholder="Server"
           v-model="server"/>
    <input type="password"
           placeholder="Key"
           v-model="key"/>
    <div class="btn" @click="auth">
      连接
    </div>
  </div>
  <div class="group">
    <a class="footer"
       href="https://github.com/Titvt/Picalloc">
      https://github.com/Titvt/Picalloc
    </a>
  </div>
</template>

<script>
import { globals, request } from '@/util'
import axios from 'axios'

export default {
  name: 'pageSetting',
  data() {
    return {
      server: localStorage.getItem('server') ?? '',
      key: localStorage.getItem('key') ?? '',
      authSuccMsg: '',
      authFailMsg: '',
      authMsg: '服务器地址末尾不要加“/”哦~',
    }
  },
  methods: {
    auth() {
      globals.authed = false
      this.authSuccMsg = ''
      this.authFailMsg = ''
      this.authMsg = '正在连接中……'
      localStorage.setItem('server', this.server)
      localStorage.setItem('key', this.key)
      axios.defaults.baseURL = this.server
      request('/auth', {
        key: this.key,
      }, () => {
        globals.authed = true
        this.authSuccMsg = '连接服务器成功(*^_^*)'
      }, () => {
        this.authFailMsg = '连接服务器失败(T_T)'
      })
    },
  },
}
</script>

<style scoped>
.group {
  display: flex;
  flex-direction: column;
  margin: 15px;
}

.title {
  margin: 5px 10px 15px 10px;
  color: #ec75a1;
  font-size: 21px;
}

.msg {
  margin: 0 10px 5px 10px;
  color: #808080;
  font-size: 14px;
}

.succ {
  color: #60dd60;
}

.fail {
  color: #ff0000;
}

input {
  min-width: 0;
  margin: 0 10px 10px 10px;
  padding: 5px 10px 5px 10px;
  outline: none;
  border: #80808040 1px solid;
  border-radius: 5px;
  box-shadow: #80808020 0 0 5px 0;
  font-size: 18px;
}

.btn {
  margin: 0 10px 10px 10px;
  padding: 5px;
  border: #ffc0cb 1px solid;
  border-radius: 10px;
  color: #ffc0cb;
  font-size: 18px;
  text-align: center;
}

.btn:hover {
  background: #ffc0cb20;
}

.footer {
  color: #696969;
  font-size: 12px;
  text-align: center;
}
</style>
