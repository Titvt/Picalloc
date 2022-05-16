<template>
  <div class="item"
       @click="viewItem">
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
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'viewComicItem',
  props: [
    'name',
    'comic',
    'cover',
    'author',
    'likeCount',
  ],
  methods: {
    viewItem() {
      this.$router.push(`/comic/${this.comic}`)
    },
  },
}
</script>

<style scoped>
.item {
  display: flex;
  margin: 10px;
  border: #ffc0cb 1px solid;
  border-radius: 5px;
}

.item:hover {
  background: #ffc0cb20;
}

.item > img {
  width: 36vw;
  height: 48vw;
  margin: 5px;
  border-radius: 5px;
}

.item > div {
  display: flex;
  flex-direction: column;
  margin: 5px;
}

.item > div > span:nth-child(1) {
  margin-bottom: 5px;
  color: #ff69b4;
  font-size: 17px;
}

.item > div > span:nth-child(2) {
  flex-grow: 1;
  color: #00bfff;
  font-size: 14px;
}

.item > div > div {
  display: flex;
}

.item > div > div > img {
  width: 20px;
  height: 20px;
  margin: 2px;
}

.item > div > div > span {
  flex-grow: 1;
  color: #ec75a1;
  font-size: 15px;
  line-height: 24px;
}
</style>
