import app from '@/app'
import pageComic from '@/components/pageComic'
import pageHome from '@/components/pageHome'
import pageSearch from '@/components/pageSearch'
import pageSetting from '@/components/pageSetting'
import pageViewer from '@/components/pageViewer'
import { createApp } from 'vue'
import { createRouter, createWebHashHistory } from 'vue-router'

const vue = createApp(app)

vue.config.unwrapInjectedRef = true

vue.use(createRouter({
  routes: [
    {
      path: '/comic/:comic',
      component: pageComic,
    },
    {
      path: '/',
      component: pageHome,
    },
    {
      path: '/search/:keyword/:page',
      component: pageSearch,
    },
    {
      path: '/setting',
      component: pageSetting,
    },
    {
      path: '/comic/:comic/:eps',
      component: pageViewer,
    },
  ],
  history: createWebHashHistory(),
}))

vue.mount('#app')
