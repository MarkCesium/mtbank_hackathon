<script setup lang="ts">
import { useRouter } from 'vue-router'
import { useUserStore } from '@/entities/user'
import logo from '@/assets/logo.png'

const router = useRouter()
const userStore = useUserStore()

function logout() {
  userStore.logout()
  router.push('/login')
}
</script>

<template>
  <div class="flex items-center justify-between bg-brand-primary text-brand-white rounded-2xl p-4 shadow-sm">
    <div class="flex items-center gap-3">
      <div class="w-10 h-10 flex items-center justify-center">
        <img :src="logo" alt="MTBank Logo" class="w-full h-full object-contain" />
      </div>
      <div class="flex flex-col">
        <h1 class="font-accent text-2xl leading-none font-bold tracking-wide">MTBank</h1>
        <div class="flex items-center gap-1.5 mt-1">
          <div class="bg-brand-dark/20 px-2 py-0.5 rounded-full text-[10px] font-main flex items-center gap-1">
            <span>1-й сезон</span>
          </div>
        </div>
      </div>
    </div>

    <button
      class="text-brand-white/80 hover:text-brand-white text-sm font-main transition"
      @click="logout"
    >
      Выйти
    </button>
  </div>
</template>
