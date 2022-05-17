<template>
  <view-search-box :prop-keyword="keyword"/>
  <view-comic-item v-for="item in items"
                   :key="item.comic"
                   v-bind="item"/>
  <div v-if="total!==0"
       class="pager">
    <span v-if="page>1"
          @click="prev">
      上一页
    </span>
    <span>
      {{ `${page} / ${total}` }}
    </span>
    <span v-if="page<total"
          @click="next">
      下一页
    </span>
  </div>
</template>

<script>
import viewComicItem from '@/components/viewComicItem'
import viewSearchBox from '@/components/viewSearchBox'
import { request } from "@/util";

export default {
  name: 'pageSearch',
  components: {
    viewComicItem,
    viewSearchBox,
  },
  data() {
    return {
      keyword: this.$route.params.keyword,
      page: parseInt(this.$route.params.page.toString()),
      items: [],
      total: 0,
    }
  },
  mounted() {
    this.$watch(() => this.$route.params, () => {
      if (Object.keys(this.$route.params).length !== 0) {
        this.update()
      }
    }, {
      immediate: true,
    })
  },
  methods: {
    update() {
      this.keyword = this.$route.params.keyword
      this.page = parseInt(this.$route.params.page.toString())
      this.items = []
      this.total = 0
      request('/search', {
        keyword: this.keyword,
        page: this.page,
      }, data => {
        this.items = data['comicList']
        this.total = data['pageCount']
      })
    },
    prev() {
      if (this.page > 1) {
        this.$router.push(`/search/${encodeURIComponent(this.keyword)}/${this.page - 1}`)
      }
    },
    next() {
      if (this.page < this.total) {
        this.$router.push(`/search/${encodeURIComponent(this.keyword)}/${this.page + 1}`)
      }
    },
  },
}
</script>

<style scoped>
.pager {
  display: flex;
  justify-content: center;
  margin: 10px;
  color: #ec75a1;
}

.pager > span {
  padding: 10px;
}
</style>
