<script setup lang="ts">
import { useRouter } from 'vue-router'
import { useQuery } from '@tanstack/vue-query'
import { authApi } from '@/shared/api/auth'
import { useUserStore } from '@/entities/user'
import { BattlePassCarousel } from '@/features/battlepass'

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
  <div class="min-h-[100dvh] bg-brand-gray flex flex-col items-center p-6">
    <header class="w-full max-w-md flex flex-col gap-4">
      <div class="flex items-center justify-between">
        <h1 class="text-brand-dark font-accent text-2xl">MTBank</h1>
        <button
          class="text-brand-dark/50 hover:text-brand-dark text-sm font-main transition"
          @click="logout"
        >
          Выйти
        </button>
      </div>
      <BattlePassCarousel class="w-full" />
    </header>

    <main
      class="flex-1 w-full max-w-md flex flex-col items-center justify-center gap-6 text-center"
    >
      <div
        class="bg-brand-white rounded-2xl p-5 w-full flex items-center justify-around shadow-sm"
      >
        <div class="flex flex-col items-center">
          <span class="text-brand-dark/50 font-main text-xs uppercase tracking-wide">Бонусы</span>
          <span class="text-brand-secondary font-digital text-3xl mt-1">
            {{ meQuery.data.value?.bonus ?? '0.00' }}
          </span>
        </div>
        <div class="w-px h-10 bg-brand-gray/50"></div>
        <div class="flex flex-col items-center">
          <span class="text-brand-dark/50 font-main text-xs uppercase tracking-wide">Попытки</span>
          <span class="text-brand-dark font-digital text-3xl mt-1">
            {{ meQuery.data.value?.attempts_remaining ?? 0 }}/3
          </span>
        </div>
      </div>

      <button
        class="bg-brand-primary hover:bg-brand-primary/90 disabled:bg-brand-gray/40 disabled:cursor-not-allowed text-brand-white font-main font-semibold px-10 py-3 rounded-xl transition w-full"
        :disabled="(meQuery.data.value?.attempts_remaining ?? 0) === 0"
        @click="goGame"
      >
        Играть
      </button>
      <p
        v-if="(meQuery.data.value?.attempts_remaining ?? 0) === 0"
        class="text-brand-dark/50 text-xs font-main -mt-4"
      >
        На сегодня попытки закончились.
      </p>
    </main>
  </div>
</template>
