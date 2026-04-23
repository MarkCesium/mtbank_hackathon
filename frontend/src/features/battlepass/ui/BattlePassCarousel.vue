<script setup lang="ts">
import { computed, nextTick, onMounted, ref, watch } from 'vue'
import type { BattlePassDay } from '@/entities/battlepass'
import { useBattlePass } from '../model/useBattlePass'
import BattlePassDayCard from './BattlePassDayCard.vue'
import BattlePassDayDetail from './BattlePassDayDetail.vue'

const { state, isLoading, isError } = useBattlePass()

const carouselRef = ref<HTMLElement | null>(null)
const selectedDay = ref<BattlePassDay | null>(null)

const completedCount = computed(() =>
  state.value?.days.filter(d => d.state === 'completed').length ?? 0,
)

const progressPct = computed(() => {
  if (!state.value) return 0
  return (completedCount.value / state.value.month_days_count) * 100
})

function scrollToToday() {
  const container = carouselRef.value
  if (!container) return
  const el = container.querySelector<HTMLElement>('[data-today="true"]')
  if (!el) return
  const target = el.offsetLeft - (container.clientWidth - el.clientWidth) / 2
  container.scrollTo({ left: Math.max(0, target), behavior: 'smooth' })
}

function onWheel(e: WheelEvent) {
  const container = carouselRef.value
  if (!container) return
  if (e.deltaY === 0 || e.deltaX !== 0) return
  if (container.scrollWidth <= container.clientWidth) return
  e.preventDefault()
  container.scrollLeft += e.deltaY
}

onMounted(() => {
  nextTick(() => scrollToToday())
})

watch(
  () => state.value?.today_day,
  () => {
    nextTick(() => scrollToToday())
  },
)
</script>

<template>
  <section class="w-full bg-brand-white rounded-2xl p-4 shadow-sm">
    <div class="flex items-start justify-between gap-3 mb-3">
      <div class="min-w-0">
        <h3 class="text-brand-dark font-accent font-bold text-sm uppercase tracking-wide leading-tight">
          Программа бонусов на месяц
        </h3>
        <p class="text-brand-dark/55 font-main text-[11px] mt-1 leading-snug">
          Проходи игру каждый день и получай награды!<br>
          Пропустишь день — бонусы сгорают до конца месяца.
        </p>
      </div>
    </div>

    <div v-if="isLoading" class="text-brand-dark/50 font-main text-xs py-2">
      Загружается...
    </div>

    <div v-else-if="isError" class="text-brand-secondary font-main text-xs py-2">
      Не удалось загрузить MTPass
    </div>

    <div
      v-else-if="state"
      ref="carouselRef"
      class="flex items-center overflow-x-auto overscroll-x-contain snap-x snap-proximity py-2 -mx-4 px-4 scrollbar-none touch-[pan-x_pan-y]"
      @wheel="onWheel"
    >
      <template v-for="(d, i) in state.days" :key="d.day">
        <BattlePassDayCard
          :day="d"
          :is-today="d.day === state.today_day"
          @click="selectedDay = d"
        />
        <span
          v-if="i < state.days.length - 1"
          class="flex-shrink-0 text-brand-gray/40 text-sm select-none leading-none mx-0.5"
        >〜</span>
      </template>
    </div>

    <div v-if="state" class="mt-3">
      <div class="text-brand-dark/50 font-main text-[11px] mb-1.5">
        {{ completedCount }}&thinsp;/&thinsp;{{ state.month_days_count }} дней пройдено
      </div>
      <div class="w-full h-1.5 rounded-full bg-brand-gray/25 overflow-hidden">
        <div
          class="h-full rounded-full bg-brand-primary transition-all duration-700"
          :style="{ width: `${progressPct}%` }"
        />
      </div>
    </div>

    <BattlePassDayDetail
      v-if="selectedDay"
      :day="selectedDay"
      @close="selectedDay = null"
    />
  </section>
</template>

<style scoped>
.scrollbar-none {
  scrollbar-width: none;
}
.scrollbar-none::-webkit-scrollbar {
  display: none;
}
</style>
