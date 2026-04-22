import { createRouter, createWebHistory } from 'vue-router'
import { LoginPage } from '@/pages/login'
import { RegisterPage } from '@/pages/register'
import { HomePage } from '@/pages/home'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'home', component: HomePage },
    { path: '/login', name: 'login', component: LoginPage },
    { path: '/register', name: 'register', component: RegisterPage },
  ],
})

router.beforeEach((to) => {
  const isAuthenticated = !!localStorage.getItem('access_token')

  if ((to.name === 'login' || to.name === 'register') && isAuthenticated) {
    return { name: 'home' }
  }

  if (to.name === 'home' && !isAuthenticated) {
    return { name: 'login' }
  }
})

export default router
