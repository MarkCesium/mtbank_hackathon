<script setup lang="ts">
import { useRouter } from 'vue-router'
import { useQuery } from '@tanstack/vue-query'
import { authApi } from '@/shared/api/auth'
import { useUserStore } from '@/entities/user'
import { BattlePassCarousel } from '@/features/battlepass'
import coinImg from '@/assets/star.png'
import countImg from '@/assets/attempts.png'
import heroImg from '@/assets/blockbust.jpg'

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
</script>

<template>
  <div class="flex-1 w-full flex flex-col gap-2">
    <BattlePassCarousel class="w-full" />

    <main class="flex-1 w-full flex flex-col items-center justify-start gap-4 text-center">
      <div class="w-full grid grid-cols-2 gap-3">
        <div class="bg-brand-white rounded-2xl p-4 flex flex-col items-center gap-2 shadow-sm">
          <img :src="coinImg" alt="бонусы" class="w-10 h-10 object-contain" />
          <span class="text-brand-secondary font-digital text-3xl leading-none">
            {{ meQuery.data.value?.bonus ?? '0.00' }}
          </span>
          <span class="text-brand-dark/50 font-main text-xs uppercase tracking-wide">Бонусы</span>
        </div>
        <div class="bg-brand-white rounded-2xl p-4 flex flex-col items-center gap-2 shadow-sm">
          <img :src="countImg" alt="попытки" class="w-10 h-10 object-contain rounded-lg" />
          <span class="text-brand-dark font-digital text-3xl leading-none">
            {{ meQuery.data.value?.attempts_remaining ?? 0 }}/3
          </span>
          <span class="text-brand-dark/50 font-main text-xs uppercase tracking-wide">Попытки</span>
        </div>
      </div>

      <div class="bg-brand-primary w-full rounded-2xl p-5 flex flex-col gap-4 mb-12">
        <div class="flex items-center gap-4">
          <img :src="heroImg" alt="BlockBust" class="w-20 h-20 object-contain flex-shrink-0 drop-shadow-lg" />
          <div class="flex flex-col items-start text-left">
            <span class="text-brand-white font-digital text-2xl leading-tight">BlockBust</span>
            <span class="text-brand-white/70 font-main text-sm mt-1">Разрушай блоки — зарабатывай бонусы</span>
          </div>
        </div>
        <button
          class="bg-brand-white hover:bg-brand-white/90 disabled:bg-brand-white/30 disabled:cursor-not-allowed text-brand-primary disabled:text-brand-white font-main font-semibold py-3 rounded-xl transition w-full"
          :disabled="(meQuery.data.value?.attempts_remaining ?? 0) === 0"
          @click="goGame"
        >
          Играть
        </button>
        <p
          v-if="(meQuery.data.value?.attempts_remaining ?? 0) === 0"
          class="text-brand-white/60 text-xs font-main -mt-2 text-center"
        >
          На сегодня попытки закончились.
        </p>
      </div>
    </main>
  </div>
</template>
