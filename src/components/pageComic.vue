<template>
  <div class="header" v-if="cover!==''">
    <img :src="cover"
         alt=""/>
    <div>
      <span>
        {{ name }}
      </span>
      <span>
        {{ author }}
      </span>
      <div>
        <img src="@/assets/love.png"
             alt=""/>
        <span>
          {{ likeCount }}
        </span>
        <span>
          {{ `(${pictureCount}P)` }}
        </span>
      </div>
    </div>
  </div>
  <div class="tags" v-if="tags.length!==0">
    <div v-for="tag in tags"
         :key="tag">
      <span @click="search(tag)">
        {{ tag }}
      </span>
    </div>
  </div>
  <div class="description" v-if="description!==''">
    {{ description }}
  </div>
  <div class="eps" v-if="eps.length!==0">
    <div v-for="ep in eps"
         :key="ep.eps">
      <span @click="viewComic(ep.eps)">
        {{ ep.name }}
      </span>
    </div>
  </div>
  <div class="recom" v-if="recoms.length!==0">
    <span>
      猜你喜欢
    </span>
    <view-comic-item v-for="recom in recoms"
                     :key="recom.comic"
                     v-bind="recom"/>
  </div>
</template>

<script>
import viewComicItem from '@/components/viewComicItem'
import { addHistoryKeywords, request } from '@/util'

export default {
  name: 'pageComic',
  components: {
    viewComicItem,
  },
  data() {
    return {
      comic: this.$route.params.comic,
      name: '',
      tags: [],
      cover: '',
      author: '',
      likeCount: 0,
      description: '',
      pictureCount: 0,
      eps: [],
      recoms: [],
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
      this.comic = this.$route.params.comic
      this.name = ''
      this.tags = []
      this.cover = ''
      this.author = ''
      this.likeCount = 0
      this.description = ''
      this.pictureCount = 0
      this.eps = []
      this.recoms = []
      request('/comic_info', {
        comic: this.comic,
      }, data => {
        this.name = data['name']
        this.tags = data['tags']
        this.cover = data['cover']
        this.author = data['author']
        this.likeCount = data['likeCount']
        this.description = data['description']
        this.pictureCount = data['pictureCount']
        this.getEps(1)
        request('/comic_recom', {
          comic: this.comic,
        }, data => {
          this.recoms = data
        })
      })
    },
    getEps(page) {
      request('/comic_eps', {
        comic: this.comic,
        page: page,
      }, data => {
        this.eps.push(...data['epsList'])

        if (page < data['pageCount']) {
          this.getEps(page + 1)
        }
      })
    },
    search(keyword) {
      addHistoryKeywords(keyword)
      this.$router.push(`/search/${encodeURIComponent(keyword)}/1`)
    },
    viewComic(eps) {
      this.$router.push(`/comic/${this.comic}/${eps}`)
    }
  },
}
</script>

<style scoped>
.header {
  display: flex;
  padding: 10px;
  background: #ffc0cb20;
}

.header > img {
  width: 36vw;
  height: 48vw;
  margin: 5px;
  border-radius: 5px;
}

.header > div {
  display: flex;
  flex-direction: column;
  margin: 5px;
}

.header > div > span:nth-child(1) {
  margin-bottom: 5px;
  color: #ff69b4;
  font-size: 17px;
}

.header > div > span:nth-child(2) {
  flex-grow: 1;
  color: #00bfff;
  font-size: 14px;
}

.header > div > div {
  display: flex;
}

.header > div > div > img {
  width: 20px;
  height: 20px;
  margin: 2px;
}

.header > div > div > span:nth-child(2) {
  flex-grow: 1;
  color: #ec75a1;
  font-size: 15px;
  line-height: 24px;
}

.header > div > div > span:nth-child(3) {
  color: #ff69b4;
  font-size: 15px;
  line-height: 24px;
}

.description {
  padding: 10px 15px 10px 15px;
  background: #ffc0cb20;
}

.tags {
  display: flex;
  flex-wrap: wrap;
  padding: 10px;
}

.tags > div {
  display: flex;
  width: fit-content;
  margin: 3px;
  border: #ffa500 1px solid;
  border-radius: 10px;
  color: #ffa500;
}

.tags > div:hover {
  background: #ffa50020;
}

.tags > div > span {
  min-width: 40px;
  padding: 5px;
  text-align: center;
}

.eps {
  display: flex;
  flex-wrap: wrap;
  padding: 10px;
}

.eps > div {
  display: flex;
  width: fit-content;
  margin: 3px;
  border: #ffc0cb 1px solid;
  border-radius: 3px;
  color: #ffc0cb;
}

.eps > div:hover {
  background: #ffc0cb20;
}

.eps > div > span {
  min-width: 40px;
  padding: 5px;
  text-align: center;
}

.recom {
  padding: 10px 0 10px 0;
  background: #ffc0cb20;
}

.recom > span {
  margin-left: 15px;
  color: #ec75a1;
  font-size: 20px;
}
</style>
