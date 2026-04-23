<script setup lang="ts">
import { ChevronRight } from '@lucide/vue'
import type { ShopItem } from '../model/types'

defineProps<{ item: ShopItem }>()
defineEmits<{ click: [] }>()
</script>

<template>
  <button
    class="w-full flex items-center gap-3 bg-brand-white rounded-2xl p-4 shadow-sm hover:shadow-md transition text-left"
    @click="$emit('click')"
  >
    <div
      class="w-12 h-12 rounded-xl bg-brand-gray flex items-center justify-center flex-shrink-0 overflow-hidden"
    >
      <img v-if="item.image_url" :src="item.image_url" :alt="item.brand_name ?? item.title" class="w-full h-full object-cover" />
      <span v-else class="text-brand-primary font-accent font-bold text-lg">
        {{ (item.brand_name ?? item.title).charAt(0) }}
      </span>
    </div>

    <div class="flex-1 min-w-0">
      <p class="font-main font-semibold text-brand-dark text-sm leading-tight truncate">
        {{ item.title }}
      </p>
      <p class="font-main text-brand-dark/50 text-xs mt-0.5 truncate">{{ item.description }}</p>
    </div>

    <div class="flex items-center gap-1 flex-shrink-0">
      <div class="flex flex-col items-end">
        <span class="font-digital text-brand-dark text-sm font-semibold">{{ item.price }}</span>
        <span class="font-main text-brand-dark/50 text-[10px]">баллов</span>
      </div>
      <ChevronRight class="w-4 h-4 text-brand-dark/30" />
    </div>
  </button>
</template>
