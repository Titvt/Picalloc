<template>
  <div class="viewer">
    <img v-for="pic in pics"
         :key="pic"
         :src="pic"
         alt=""/>
  </div>
</template>

<script>
import { request } from "@/util";

export default {
  name: 'pageViewer',
  data() {
    return {
      comic: this.$route.params.comic,
      eps: this.$route.params.eps,
      pics: [],
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
      this.eps = this.$route.params.eps
      this.pics = []
      this.getPicture(1)
    },
    getPicture(page) {
      request('/comic_pic', {
        comic: this.comic,
        eps: this.eps,
        page: page,
      }, data => {
        this.pics.push(...data['pictureList'])

        if (page < data['pageCount']) {
          this.getPicture(page + 1)
        }
      })
    },
  },
}
</script>

<style scoped>
.viewer {
  font-size: 0;
}

.viewer > img {
  width: 100%;
}
</style>
