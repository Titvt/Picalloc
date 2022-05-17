<template>
  <div class="search">
    <input v-model="keyword"
           type="text"
           @keydown.enter="search(keyword)"/>
    <img alt=""
         src="@/assets/search.png"
         @click="search(keyword)"/>
  </div>
  <div class="keywords">
    <div v-for="keyword in keywords.official"
         :key="keyword"
         class="official">
      <span @click="search(keyword)">
        {{ keyword }}
      </span>
    </div>
    <div v-for="keyword in keywords.history"
         :key="keyword"
         class="history">
      <span @click="search(keyword)">
        {{ keyword }}
      </span>
      <img alt=""
           src="@/assets/remove.png"
           @click="remove(keyword)"/>
    </div>
  </div>
</template>

<script>
import { addHistoryKeywords, getHistoryKeywords, getOfficialKeywords, removeHistoryKeywords } from '@/util'

export default {
  name: 'viewSearchBox',
  props: [
    'propKeyword',
  ],
  data() {
    return {
      keyword: this.propKeyword,
      keywords: {
        official: [],
        history: getHistoryKeywords(),
      },
    }
  },
  mounted() {
    getOfficialKeywords(value => {
      this.keywords.official = value
    })
  },
  methods: {
    search(keyword) {
      if (keyword !== '') {
        addHistoryKeywords(keyword)
        this.keywords.history = getHistoryKeywords()
        this.$router.push(`/search/${encodeURIComponent(keyword)}/1`)
      }
    },
    remove(keyword) {
      removeHistoryKeywords(keyword)
      this.keywords.history = getHistoryKeywords()
    }
  },
}
</script>

<style scoped>
.search {
  display: flex;
  margin: 10px;
  border: #ffc0cb 1px solid;
  border-radius: 10px;
  box-shadow: #ffc0cb80 0 0 10px 0;
}

.search > input {
  flex-grow: 1;
  min-width: 0;
  margin: 5px 0 5px 10px;
  border: none;
  outline: none;
  color: #ec75a1;
  font-size: 18px;
}

.search > img {
  width: 25px;
  height: 25px;
  padding: 10px;
}

.keywords {
  display: flex;
  flex-wrap: wrap;
  margin: 10px;
}

.keywords > div {
  display: flex;
  width: fit-content;
  margin: 3px;
  border: 1px solid;
  border-radius: 10px;
}

.keywords > div > span {
  min-width: 40px;
  padding: 5px;
  text-align: center;
}

.keywords > div > img {
  width: 20px;
  height: 20px;
  padding: 5px 5px 5px 0;
}

.official {
  border-color: #ffc0cb;
  color: #ffc0cb;
}

.official:hover {
  background: #ffc0cb20;
}

.history {
  border-color: #ffa500;
  color: #ffa500;
}

.history:hover {
  background: #ffa50020;
}
</style>
