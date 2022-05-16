<template>
  <view-search-box prop-keyword=""/>
  <div class="header">
    <span>
      | 随机本子推荐
    </span>
    <div @click="getRandom">
      <img src="@/assets/refresh.png"
           alt=""/>
      <span>
        换一批
      </span>
    </div>
  </div>
  <view-comic-item v-for="item in items"
                   :key="item.comic"
                   v-bind="item"/>
</template>

<script>
import viewComicItem from '@/components/viewComicItem'
import viewSearchBox from '@/components/viewSearchBox'
import { request } from '@/util'

export default {
  name: 'pageHome',
  components: {
    viewComicItem,
    viewSearchBox,
  },
  data() {
    return {
      items: [],
    }
  },
  mounted() {
    this.getRandom()
  },
  methods: {
    getRandom() {
      this.items = []
      request('/random', {}, data => {
        this.items = data
      })
    },
  },
}
</script>

<style scoped>
.header {
  display: flex;
  margin-bottom: 10px;
  color: #ec75a1;
  line-height: 30px;
}

.header > span {
  flex-grow: 1;
  margin-left: 10px;
  font-size: 20px;
}

.header > div {
  display: flex;
  margin-right: 15px;
  border: #ec75a1 1px solid;
  border-radius: 30px;
}

.header > div:hover {
  background: #ec75a120;
}

.header > div > img {
  width: 20px;
  height: 20px;
  margin: 5px;
}

.header > div > span {
  margin-right: 10px;
}
</style>
