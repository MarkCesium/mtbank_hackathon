import { createRouter, createWebHistory } from 'vue-router'
import { LoginPage } from '@/pages/login'
import { RegisterPage } from '@/pages/register'
import { HomePage } from '@/pages/home'
import { GamePage } from '@/pages/game'
import { ShopPage } from '@/pages/shop'
import { FriendsPage } from '@/pages/friends'
import MainLayout from '@/shared/ui/layouts/MainLayout.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/login', name: 'login', component: LoginPage },
    { path: '/register', name: 'register', component: RegisterPage },
    {
      path: '/',
      component: MainLayout,
      meta: { requiresAuth: true },
      children: [
        { path: '', name: 'home', component: HomePage },
        { path: 'shop', name: 'shop', component: ShopPage },
        { path: 'friends', name: 'friends', component: FriendsPage },
      ],
    },
    { path: '/game', name: 'game', component: GamePage, meta: { requiresAuth: true } },
  ],
})

router.beforeEach((to) => {
  const isAuthenticated = !!localStorage.getItem('access_token')

  if ((to.name === 'login' || to.name === 'register') && isAuthenticated) {
    return { name: 'home' }
  }

  if (to.matched.some((r) => r.meta.requiresAuth) && !isAuthenticated) {
    return { name: 'login' }
  }
})

export default router
