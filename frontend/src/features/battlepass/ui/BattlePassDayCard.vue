<script setup lang="ts">
import { computed } from 'vue'
import type { BattlePassDay } from '@/entities/battlepass'
import { rewardIcon, isMilestone, isGrandPrize } from '@/entities/battlepass'

interface Props {
  day: BattlePassDay
  isToday: boolean
}

const props = defineProps<Props>()

defineEmits<{
  click: [day: BattlePassDay]
}>()

const stateClasses = computed(() => {
  switch (props.day.state) {
    case 'completed':
      return 'bg-brand-primary/25 border-brand-primary text-brand-white'
    case 'active':
      return 'bg-brand-secondary/25 border-brand-secondary text-brand-white animate-pulse-slow'
    case 'available':
      return 'bg-brand-white/5 border-brand-white/15 text-brand-white'
    case 'missed':
      return 'bg-brand-gray/10 border-brand-gray/30 text-brand-gray opacity-60'
    case 'locked':
      return 'bg-brand-dark/70 border-brand-gray/20 text-brand-gray/70 opacity-50'
  }
})

const ringClass = computed(() => {
  if (isGrandPrize(props.day.reward_type)) return 'ring-2 ring-inset ring-yellow-400/80'
  if (isMilestone(props.day.reward_type)) return 'ring-2 ring-inset ring-brand-secondary/50'
  return ''
})

const widthClass = computed(() =>
  isGrandPrize(props.day.reward_type) ? 'w-24' : 'w-20',
)

const overlayIcon = computed(() => {
  switch (props.day.state) {
    case 'completed':
      return '✓'
    case 'missed':
      return '✕'
    case 'locked':
      return '🔒'
    default:
      return null
  }
})
</script>

<template>
  <button
    type="button"
    :data-today="isToday"
    :class="[
      'flex-shrink-0 h-28 snap-center rounded-xl border',
      'flex flex-col items-center justify-between py-2 px-2',
      'transition-transform duration-150 active:scale-95',
      'cursor-pointer focus:outline-none focus:ring-2 focus:ring-brand-white/40',
      stateClasses,
      ringClass,
      widthClass,
    ]"
    @click="$emit('click', day)"
  >
    <div class="flex items-center justify-between w-full">
      <span class="font-digital text-xl leading-none">{{ day.day }}</span>
      <span
        v-if="overlayIcon"
        class="text-xs leading-none"
        :class="{
          'text-brand-primary': day.state === 'completed',
          'text-brand-gray': day.state !== 'completed',
        }"
      >
        {{ overlayIcon }}
      </span>
    </div>

    <div class="text-2xl leading-none select-none">{{ rewardIcon(day.reward_type) }}</div>

    <div class="text-[10px] font-main text-center leading-tight line-clamp-2 w-full">
      {{ day.reward_title }}
    </div>
  </button>
</template>

<style scoped>
@keyframes pulseSoft {
  0%,
  100% {
    box-shadow: 0 0 0 0 rgba(248, 75, 54, 0.6);
  }
  50% {
    box-shadow: 0 0 0 6px rgba(248, 75, 54, 0);
  }
}
.animate-pulse-slow {
  animation: pulseSoft 1.8s ease-in-out infinite;
}
</style>
