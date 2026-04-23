<script setup lang="ts">
import { useRouter } from 'vue-router'
import { useQuery } from '@tanstack/vue-query'
import { authApi } from '@/shared/api/auth'
import { useUserStore } from '@/entities/user'

const router = useRouter()
const userStore = useUserStore()

const meQuery = useQuery({
  queryKey: ['auth', 'me'],
  queryFn: async () => {
    const { data } = await authApi.me()
    userStore.setUser(data)
    return data
  },
})

function goGame() {
  router.push('/game')
}

function logout() {
  userStore.logout()
  router.push('/login')
}
</script>

<template>
  <div class="min-h-[100dvh] bg-brand-dark flex flex-col items-center p-6">
    <header class="w-full max-w-md flex items-center justify-between">
      <h1 class="text-brand-white font-accent text-2xl">MTBank</h1>
      <button
        class="text-brand-gray hover:text-brand-white text-sm font-main transition"
        @click="logout"
      >
        Выйти
      </button>
    </header>

    <main
      class="flex-1 w-full max-w-md flex flex-col items-center justify-center gap-6 text-center"
    >
      <div v-if="meQuery.data.value" class="flex flex-col items-center gap-1">
        <p class="text-brand-gray font-main text-sm">Привет,</p>
        <p class="text-brand-white font-main text-xl font-semibold">
          {{ meQuery.data.value.username }}
        </p>
      </div>

      <div
        class="bg-brand-white/5 border border-brand-white/10 rounded-2xl p-5 w-full flex items-center justify-around"
      >
        <div class="flex flex-col items-center">
          <span class="text-brand-gray font-main text-xs uppercase tracking-wide">Бонусы</span>
          <span class="text-brand-secondary font-digital text-3xl mt-1">
            {{ meQuery.data.value?.bonus ?? '0.00' }}
          </span>
        </div>
        <div class="w-px h-10 bg-brand-white/10"></div>
        <div class="flex flex-col items-center">
          <span class="text-brand-gray font-main text-xs uppercase tracking-wide">Попытки</span>
          <span class="text-brand-white font-digital text-3xl mt-1">
            {{ meQuery.data.value?.attempts_remaining ?? 0 }}/3
          </span>
        </div>
      </div>

      <div class="flex flex-col items-center gap-3 mt-4">
        <h2 class="text-brand-white font-accent text-4xl">BlockBust</h2>
        <p class="text-brand-gray font-main text-sm max-w-xs">
          Очищай ряды и столбцы. Набери 1000 очков и получи бонус.
        </p>
      </div>

      <button
        class="bg-brand-primary hover:bg-brand-primary/90 disabled:bg-brand-gray/40 disabled:cursor-not-allowed text-brand-white font-main font-semibold px-10 py-3 rounded-xl transition"
        :disabled="(meQuery.data.value?.attempts_remaining ?? 0) === 0"
        @click="goGame"
      >
        Играть
      </button>
      <p
        v-if="(meQuery.data.value?.attempts_remaining ?? 0) === 0"
        class="text-brand-gray text-xs font-main"
      >
        На сегодня попытки закончились.
      </p>
    </main>
  </div>
</template>
