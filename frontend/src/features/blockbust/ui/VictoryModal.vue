<script setup lang="ts">
interface Props {
  status: 'won' | 'lost'
  score: number
  awarded: string | null
  canRetry: boolean
}

defineProps<Props>()

const emit = defineEmits<{
  retry: []
  exit: []
}>()
</script>

<template>
  <div class="fixed inset-0 z-40 bg-black/70 flex items-center justify-center p-4">
    <div
      class="bg-brand-white rounded-2xl max-w-sm w-full p-6 flex flex-col items-center gap-4 shadow-2xl"
    >
      <h2
        v-if="status === 'won'"
        class="text-3xl font-accent text-brand-primary text-center"
      >
        Победа!
      </h2>
      <h2 v-else class="text-3xl font-accent text-brand-dark text-center">Игра окончена</h2>

      <p class="text-brand-black font-main text-center">
        Ваш счёт: <span class="font-bold">{{ score }}</span>
      </p>

      <div
        v-if="awarded && Number(awarded) > 0"
        class="bg-brand-primary/10 border border-brand-primary text-brand-primary rounded-lg px-4 py-2 font-main text-center"
      >
        Начислено бонусов: <span class="font-bold">+{{ awarded }}</span>
      </div>

      <div class="flex gap-3 w-full mt-2">
        <button
          v-if="canRetry"
          class="flex-1 bg-brand-primary hover:bg-brand-primary/90 text-brand-white font-main font-semibold py-2 rounded-lg transition"
          @click="emit('retry')"
        >
          Ещё раз
        </button>
        <button
          class="flex-1 bg-brand-gray/30 hover:bg-brand-gray/50 text-brand-black font-main font-semibold py-2 rounded-lg transition"
          @click="emit('exit')"
        >
          В меню
        </button>
      </div>
    </div>
  </div>
</template>
