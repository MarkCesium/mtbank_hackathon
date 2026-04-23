<script setup lang="ts">
import { computed } from 'vue'
import type { BattlePassDay } from '@/entities/battlepass'
import { rewardIcon, rewardIconColor } from '@/entities/battlepass'

interface Props {
  day: BattlePassDay
}

const props = defineProps<Props>()

defineEmits<{
  close: []
}>()

const stateLabel = computed(() => {
  switch (props.day.state) {
    case 'completed':
      return 'Получено'
    case 'active':
      return 'Доступно сегодня — выиграй в игре'
    case 'available':
      return 'Откроется в свой день'
    case 'missed':
      return 'Пропущено'
    case 'locked':
      return 'Заморожено до конца месяца'
  }
})

const stateColor = computed(() => {
  switch (props.day.state) {
    case 'completed':
      return 'text-brand-primary'
    case 'active':
      return 'text-brand-secondary'
    case 'missed':
    case 'locked':
      return 'text-brand-gray'
    default:
      return 'text-brand-black/70'
  }
})
</script>

<template>
  <div
    class="fixed inset-0 z-40 bg-black/70 flex items-center justify-center p-4"
    @click.self="$emit('close')"
  >
    <div
      class="bg-brand-white rounded-2xl max-w-sm w-full p-6 flex flex-col items-center gap-4 shadow-2xl"
    >
      <div class="flex items-center gap-2 text-brand-gray font-main text-sm">
        <span class="font-main text-brand-black text-xl">День</span>
        <span class="font-digital text-brand-black text-xl">{{ day.day }}</span>
      </div>

      <component
        :is="rewardIcon(day.reward_type)"
        class="w-16 h-16"
        :class="rewardIconColor(day.reward_type)"
      />

      <h3 class="text-2xl font-accent text-brand-black text-center">
        {{ day.reward_title }}
      </h3>

      <p class="text-brand-black/80 font-main text-center text-sm">
        {{ day.reward_description }}
      </p>

      <div
        class="font-main text-sm font-semibold mt-1"
        :class="stateColor"
      >
        {{ stateLabel }}
      </div>

      <button
        class="w-full mt-2 bg-brand-primary hover:bg-brand-primary/90 text-brand-white font-main font-semibold py-2 rounded-lg transition"
        @click="$emit('close')"
      >
        Закрыть
      </button>
    </div>
  </div>
</template>
