<script setup lang="ts">
import { nextTick, onMounted, ref, watch } from 'vue'
import type { BattlePassDay } from '@/entities/battlepass'
import { useBattlePass } from '../model/useBattlePass'
import BattlePassDayCard from './BattlePassDayCard.vue'
import BattlePassDayDetail from './BattlePassDayDetail.vue'

const { state, isLoading, isError } = useBattlePass()

const carouselRef = ref<HTMLElement | null>(null)
const selectedDay = ref<BattlePassDay | null>(null)

function scrollToToday() {
  const container = carouselRef.value
  if (!container) return
  const el = container.querySelector<HTMLElement>('[data-today="true"]')
  if (!el) return
  const target = el.offsetLeft - (container.clientWidth - el.clientWidth) / 2
  container.scrollLeft = Math.max(0, target)
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
  <section class="w-full">
    <header class="flex items-center justify-between px-1 mb-2">
      <h3 class="text-brand-white font-accent text-lg">Батлпасс</h3>
      <span
        v-if="state?.is_frozen"
        class="text-[10px] uppercase tracking-wide px-2 py-0.5 rounded-full bg-brand-gray/20 text-brand-gray font-main"
      >
        Заморожен
      </span>
    </header>

    <div v-if="isLoading" class="text-brand-gray font-main text-xs px-1">
      Загружается...
    </div>

    <div v-else-if="isError" class="text-brand-secondary font-main text-xs px-1">
      Не удалось загрузить батлпасс
    </div>

    <div
      v-else-if="state"
      ref="carouselRef"
      class="flex gap-2 overflow-x-auto overscroll-x-contain snap-x snap-proximity py-2 -mx-1 px-1 scrollbar-none touch-pan-x"
      @wheel="onWheel"
    >
      <BattlePassDayCard
        v-for="d in state.days"
        :key="d.day"
        :day="d"
        :is-today="d.day === state.today_day"
        @click="selectedDay = d"
      />
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
