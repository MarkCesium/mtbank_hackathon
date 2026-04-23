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

const borderClass = computed(() => {
  switch (props.day.state) {
    case 'completed': return 'border-brand-primary/40'
    case 'active': return 'border-brand-primary border-[2px]'
    case 'available': return 'border-brand-gray/35'
    case 'missed': return 'border-brand-gray/20'
    case 'locked': return 'border-brand-gray/15'
  }
})

const opacityClass = computed(() => {
  switch (props.day.state) {
    case 'missed': return 'opacity-50'
    case 'locked': return 'opacity-40'
    default: return ''
  }
})

const iconBgClass = computed(() => {
  switch (props.day.state) {
    case 'completed': return 'bg-brand-primary'
    case 'active': return 'bg-brand-primary/10 ring-2 ring-brand-primary'
    case 'available': return 'bg-brand-gray/15'
    case 'missed': return 'bg-brand-gray/15'
    case 'locked': return 'bg-brand-gray/10'
  }
})

const specialRingClass = computed(() => {
  if (isGrandPrize(props.day.reward_type)) return 'ring-2 ring-yellow-400/80'
  if (isMilestone(props.day.reward_type)) return 'ring-1 ring-brand-secondary/60'
  return ''
})

const widthClass = computed(() =>
  isGrandPrize(props.day.reward_type) ? 'w-20' : 'w-[72px]',
)
</script>

<template>
  <button
    type="button"
    :data-today="isToday"
    :class="[
      'flex-shrink-0 snap-center rounded-xl border bg-brand-white',
      'flex flex-col items-center justify-between pt-2.5 pb-2.5 px-1.5',
      'h-[108px]',
      'transition-all duration-150 active:scale-95 cursor-pointer focus:outline-none',
      borderClass,
      opacityClass,
      specialRingClass,
      widthClass,
      isToday ? 'animate-pulse-card' : '',
    ]"
    @click="$emit('click', day)"
  >
    <span
      class="font-main text-[9px] font-bold uppercase tracking-widest w-full text-center leading-none"
      :class="day.state === 'active' ? 'text-brand-primary' : 'text-brand-dark/45'"
    >
      День {{ day.day }}
    </span>

    <div
      class="w-10 h-10 rounded-full flex items-center justify-center flex-shrink-0"
      :class="iconBgClass"
    >
      <template v-if="day.state === 'completed'">
        <span class="text-brand-white font-bold text-lg leading-none">✓</span>
      </template>
      <template v-else-if="day.state === 'missed'">
        <span class="text-brand-dark/40 font-semibold text-base leading-none">✕</span>
      </template>
      <template v-else-if="day.state === 'locked'">
        <span class="text-base leading-none">🔒</span>
      </template>
      <template v-else>
        <span class="text-xl leading-none select-none">{{ rewardIcon(day.reward_type) }}</span>
      </template>
    </div>

    <span
      class="text-[9px] font-main text-center leading-tight line-clamp-2 w-full h-[1.5rem] flex items-start justify-center"
      :class="day.state === 'active' ? 'text-brand-dark font-medium' : 'text-brand-dark/50'"
    >
      {{ day.reward_title }}
    </span>
  </button>
</template>

<style scoped>
@keyframes pulseSoft {
  0%, 100% { box-shadow: 0 0 0 0 rgba(0, 33, 243, 0.3); }
  50% { box-shadow: 0 0 0 7px rgba(0, 33, 243, 0); }
}
.animate-pulse-card {
  animation: pulseSoft 2s ease-in-out infinite;
}
</style>
