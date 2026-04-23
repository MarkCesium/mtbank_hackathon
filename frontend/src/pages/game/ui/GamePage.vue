<script setup lang="ts">
import { computed, ref, watch, type Ref } from 'vue'
import { useRouter } from 'vue-router'
import { useMutation, useQuery, useQueryClient } from '@tanstack/vue-query'
import { authApi } from '@/shared/api/auth'
import { gameApi, type FinishAttemptResponse } from '@/shared/api/game'
import { useGame, VictoryModal } from '@/features/blockbust'
import { BATTLEPASS_QUERY_KEY } from '@/features/battlepass'
import { GameBoard } from '@/widgets/game-board'
import { useUserStore } from '@/entities/user'

function useAnimatedNumber(source: Ref<number>, duration = 450) {
  const displayed = ref(source.value)
  let rafId: number | null = null
  let startTime: number | null = null
  let from = source.value
  let to = source.value

  watch(source, (newVal) => {
    from = displayed.value
    to = newVal
    startTime = null
    if (rafId !== null) cancelAnimationFrame(rafId)

    function step(ts: number) {
      if (startTime === null) startTime = ts
      const t = Math.min((ts - startTime) / duration, 1)
      const eased = 1 - Math.pow(1 - t, 3)
      displayed.value = Math.round(from + (to - from) * eased)
      if (t < 1) {
        rafId = requestAnimationFrame(step)
      } else {
        displayed.value = to
        rafId = null
      }
    }

    rafId = requestAnimationFrame(step)
  })

  return displayed
}

const router = useRouter()
const userStore = useUserStore()
const queryClient = useQueryClient()

const meQuery = useQuery({
  queryKey: ['auth', 'me'],
  queryFn: async () => {
    const { data } = await authApi.me()
    userStore.setUser(data)
    return data
  },
})

const game = useGame()
const animatedScore = useAnimatedNumber(game.score)

const errorMsg = ref<string | null>(null)
const finishResult = ref<FinishAttemptResponse | null>(null)
const finishing = ref(false)

const startMutation = useMutation({
  mutationFn: () => gameApi.start().then((r) => r.data),
  onSuccess: (data) => {
    errorMsg.value = null
    finishResult.value = null
    game.reset()
    if (meQuery.data.value) {
      userStore.setUser({ ...meQuery.data.value, attempts_remaining: data.attempts_remaining })
      queryClient.setQueryData(['auth', 'me'], {
        ...meQuery.data.value,
        attempts_remaining: data.attempts_remaining,
      })
    }
  },
  onError: (err: unknown) => {
    const e = err as { response?: { status?: number; data?: { detail?: string } } }
    if (e.response?.status === 429) {
      errorMsg.value = 'На сегодня попыток больше нет. Возвращайся завтра!'
    } else {
      errorMsg.value = e.response?.data?.detail ?? 'Не удалось начать игру'
    }
  },
})

const finishMutation = useMutation({
  mutationFn: (body: { score: number; won: boolean }) =>
    gameApi.finish(body).then((r) => r.data),
  onSuccess: (data) => {
    finishResult.value = data
    if (meQuery.data.value) {
      const updated = {
        ...meQuery.data.value,
        bonus: data.bonus,
        attempts_remaining: data.attempts_remaining,
      }
      userStore.setUser(updated)
      queryClient.setQueryData(['auth', 'me'], updated)
    }
    queryClient.invalidateQueries({ queryKey: BATTLEPASS_QUERY_KEY })
    finishing.value = false
  },
  onError: () => {
    finishing.value = false
  },
})

watch(game.status, (s) => {
  if ((s === 'won' || s === 'lost') && !finishing.value) {
    finishing.value = true
    finishMutation.mutate({ score: game.score.value, won: s === 'won' })
  }
})

const canStart = computed(
  () => (meQuery.data.value?.attempts_remaining ?? 0) > 0 && game.status.value === 'idle',
)

function goHome() {
  router.push('/')
}

function retry() {
  startMutation.mutate()
}

const attemptsRemaining = computed(() => meQuery.data.value?.attempts_remaining ?? 0)
const bonus = computed(() => meQuery.data.value?.bonus ?? '0.00')
const showModal = computed(
  () => (game.status.value === 'won' || game.status.value === 'lost') && !!finishResult.value,
)
</script>

<template>
  <div class="min-h-[100dvh] bg-brand-gray flex flex-col items-center px-3 py-4">
    <header class="w-full max-w-md flex items-center justify-between mb-4">
      <button
        class="text-brand-dark/60 hover:text-brand-dark font-main text-sm transition"
        @click="goHome"
      >
        ← В меню
      </button>
      <div class="text-brand-dark/60 font-main text-sm">
        Бонусы: <span class="text-brand-secondary font-semibold">{{ bonus }}</span>
      </div>
    </header>

    <div class="w-full max-w-md mb-2 flex items-center justify-between text-brand-dark/60 font-main text-sm">
      <span>Попытки: <span class="text-brand-dark font-semibold">{{ attemptsRemaining }}/3</span></span>
      <span v-if="game.status.value !== 'idle'">Очки: <span class="text-brand-dark font-semibold">{{ animatedScore }}</span></span>
    </div>
    <div v-if="game.status.value !== 'idle'" class="w-full max-w-md mb-4 h-2 bg-brand-dark/10 rounded-full overflow-hidden">
      <div
        class="h-full bg-brand-primary transition-all duration-300"
        :style="{ width: `${game.progress.value}%` }"
      ></div>
    </div>
    <div v-else class="mb-4"></div>

    <div
      v-if="game.status.value === 'idle'"
      class="flex-1 flex flex-col justify-center w-full max-w-md py-4"
    >
      <div class="bg-brand-white rounded-2xl shadow p-6 flex flex-col items-center gap-4">
        <h1 class="text-brand-primary font-accent text-4xl">BlockBust</h1>
        <p class="text-brand-dark font-main text-center max-w-xs">
          Набери <span class="text-brand-dark font-semibold">1000 очков</span>, очищая ряды и
          столбцы. За победу — <span class="text-brand-secondary font-semibold">0.05 бонусов</span>.
        </p>
        <p v-if="errorMsg" class="text-brand-secondary font-main text-center text-sm">
          {{ errorMsg }}
        </p>
        <button
          class="bg-brand-primary hover:bg-brand-primary/90 disabled:bg-brand-gray/40 disabled:cursor-not-allowed text-brand-white font-main font-semibold px-8 py-3 rounded-xl transition w-full"
          :disabled="!canStart || startMutation.isPending.value"
          @click="startMutation.mutate()"
        >
          {{ startMutation.isPending.value ? 'Загрузка…' : 'Начать игру' }}
        </button>
        <p v-if="attemptsRemaining === 0" class="text-brand-dark/40 text-xs font-main">
          Попытки обновятся завтра.
        </p>
      </div>
    </div>

    <GameBoard v-else :game="game" class="flex-1 w-full max-w-md" />

    <Transition name="victory">
      <VictoryModal
        v-if="showModal && finishResult"
        :status="game.status.value === 'won' ? 'won' : 'lost'"
        :score="game.score.value"
        :awarded="finishResult.awarded"
        :can-retry="finishResult.attempts_remaining > 0"
        @retry="retry"
        @exit="goHome"
      />
    </Transition>
  </div>
</template>

<style scoped>
.victory-enter-active,
.victory-leave-active {
  transition: opacity 0.2s ease;
}
.victory-enter-from,
.victory-leave-to {
  opacity: 0;
}
</style>
