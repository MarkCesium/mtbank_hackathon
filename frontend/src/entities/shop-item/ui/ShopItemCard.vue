<script setup lang="ts">
import type { ShopItem } from '../model/types'

defineProps<{ item: ShopItem }>()
defineEmits<{ click: [] }>()

const CATEGORY_GRADIENTS: Record<string, string> = {
  promo_code: 'from-[#1a1a2e] to-[#16213e]',
  subscription: 'from-[#6a0dad] to-[#9b59b6]',
  bank_perk: 'from-[#0021f3] to-[#071d49]',
}
</script>

<template>
  <button
    class="flex-shrink-0 w-44 rounded-2xl p-4 flex flex-col justify-between text-left shadow-md hover:shadow-lg transition bg-gradient-to-br"
    :class="CATEGORY_GRADIENTS[item.category] ?? 'from-brand-primary to-brand-dark'"
    @click="$emit('click')"
  >
    <div>
      <p class="font-accent font-bold text-white text-lg leading-tight">{{ item.title }}</p>
      <p class="font-main text-white/70 text-xs mt-1 line-clamp-2">{{ item.description }}</p>
    </div>
    <div class="mt-4 flex items-center gap-1">
      <span class="text-white/80 font-main text-xs">Б</span>
      <span class="font-digital text-white font-bold text-sm">{{ item.price }}</span>
      <span class="font-main text-white/60 text-[10px]">баллов</span>
    </div>
  </button>
</template>
