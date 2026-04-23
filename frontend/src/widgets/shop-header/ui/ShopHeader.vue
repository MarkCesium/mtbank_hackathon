<script setup lang="ts">
import { LayoutGrid, Tag, Play, Gift } from '@lucide/vue'
import { useUserStore } from '@/entities/user'
import { SHOP_CATEGORIES } from '@/entities/shop-item'

type CategoryKey = 'all' | 'promo_code' | 'subscription' | 'bank_perk'

const model = defineModel<CategoryKey>({ default: 'all' })

const userStore = useUserStore()

const ICONS = {
  all: LayoutGrid,
  promo_code: Tag,
  subscription: Play,
  bank_perk: Gift,
}
</script>

<template>
  <div class="flex flex-col gap-0">
    <!-- Синяя шапка с балансом -->
    <div class="bg-brand-primary rounded-2xl p-4 flex items-center justify-between">
      <div>
        <h1 class="font-accent font-bold text-brand-white text-2xl tracking-wide leading-none">
          МАГАЗИН
        </h1>
        <p class="font-main text-brand-white/60 text-xs mt-1">1 балл = 1 BYN</p>
      </div>
      <div class="text-right">
        <p class="font-main text-brand-white/60 text-xs uppercase tracking-wide">Мой баланс</p>
        <p class="font-digital text-brand-white font-bold text-2xl leading-tight">
          {{ userStore.user?.bonus ?? '0.00' }}
        </p>
        <p class="font-main text-brand-white/60 text-[10px]">баллов</p>
      </div>
    </div>

    <!-- Табы фильтрации -->
    <div class="bg-brand-white rounded-2xl shadow-sm mt-3 flex">
      <button
        v-for="cat in SHOP_CATEGORIES"
        :key="cat.key"
        class="flex-1 flex flex-col items-center gap-1 py-3 px-1 transition rounded-2xl"
        :class="
          model === cat.key
            ? 'text-brand-primary'
            : 'text-brand-dark/40 hover:text-brand-dark/60'
        "
        @click="model = cat.key as CategoryKey"
      >
        <component :is="ICONS[cat.key as keyof typeof ICONS]" class="w-5 h-5" />
        <span class="font-main text-[10px] font-medium leading-none text-center">{{ cat.label }}</span>
        <div
          class="h-0.5 w-5 rounded-full transition-all"
          :class="model === cat.key ? 'bg-brand-primary' : 'bg-transparent'"
        />
      </button>
    </div>
  </div>
</template>
