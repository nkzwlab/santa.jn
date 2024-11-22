import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/participants',
      name: 'participants',
      component: () => import('../views/Participants.vue')
    },
    {
      path: '/join',
      name: 'join',
      component: () => import('../views/ContactPage.vue')
    }
  ]
})

export default router
