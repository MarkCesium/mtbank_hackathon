<script setup lang="ts">
import { useRoute } from 'vue-router'
import { Home, ShoppingBag, Users } from '@lucide/vue'

const route = useRoute()

const navItems = [
  { to: '/', label: 'Главная', icon: Home },
  { to: '/shop', label: 'Магазин', icon: ShoppingBag },
  { to: '/friends', label: 'Друзья', icon: Users },
]

function isActive(path: string): boolean {
  if (path === '/') return route.path === '/'
  return route.path.startsWith(path)
}
</script>

<template>
  <div class="fixed bottom-0 left-0 right-0 flex justify-center px-6 pb-6 z-50 pointer-events-none">
    <nav class="w-full max-w-md bg-brand-white rounded-2xl shadow-md flex items-center justify-around py-3 px-4 pointer-events-auto">
      <RouterLink
        v-for="item in navItems"
        :key="item.to"
        :to="item.to"
        class="flex flex-col items-center gap-1 px-4 py-1 rounded-xl transition-colors"
        :class="isActive(item.to) ? 'text-brand-primary' : 'text-brand-dark/40'"
      >
        <component :is="item.icon" class="w-5 h-5" />
        <span class="text-[10px] font-main font-medium">{{ item.label }}</span>
      </RouterLink>
    </nav>
  </div>
</template>
