import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginPage.vue'),
    },
    {
      path: '/interactive-games',
      name: 'interactive-games',
      component: () => import('../views/InteractiveGames.vue'),
    },
    {
      path: '/child-help',
      name: 'child-help',
      component: () => import('../views/ChildHelpPage.vue'),
    },
    {
      path: '/safe-sharing',
      name: 'safe-sharing',
      component: () => import('../views/SafeStoryShare.vue'),
    },
    {
      path:'/memory-match',
      name:'memory-match',
      component: () => import('../views/MemoryMatch.vue')
    },
    {
      path: '/games/math-puzzle',
      name: 'games/math-puzzle',
      component: () => import('../views/MathPuzzle.vue')
    },
    {
      path: '/games/word-scramble',
      name: 'games/word-scramble',
      component: () => import('../views/WordScramble.vue')
    },
    {
      path: '/games/coloring-fun',
      name: 'games/coloring-fun',
      component: () => import('../views/ColouringFun.vue')
    }



  ],
})

export default router
