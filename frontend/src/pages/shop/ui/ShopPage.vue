<script setup lang="ts">
import { ref, computed } from 'vue'
import { useQuery } from '@tanstack/vue-query'
import { authApi } from '@/shared/api/auth'
import { shopApi } from '@/shared/api/shop'
import { useUserStore } from '@/entities/user'
import { ShopHeader } from '@/widgets/shop-header'
import { ShopItemRow, ShopItemCard, type ShopItem, type ShopCategory } from '@/entities/shop-item'
import { PurchaseModal } from '@/features/shop-purchase'

type CategoryKey = 'all' | ShopCategory

const activeCategory = ref<CategoryKey>('all')
const selectedItem = ref<ShopItem | null>(null)
const userStore = useUserStore()

useQuery({
  queryKey: ['auth', 'me'],
  queryFn: async () => {
    const { data } = await authApi.me()
    userStore.setUser(data)
    return data
  },
})

const itemsQuery = useQuery({
  queryKey: ['shop', 'items'],
  queryFn: async () => (await shopApi.list()).data.items,
})

const recommended = computed(
  () => itemsQuery.data.value?.filter((i) => i.is_recommended) ?? [],
)

function byCategory(cat: ShopCategory) {
  return itemsQuery.data.value?.filter((i) => i.category === cat) ?? []
}

function visible(cat: ShopCategory) {
  return activeCategory.value === 'all' || activeCategory.value === cat
}
</script>

<template>
  <div class="flex-1 w-full flex flex-col gap-4 pb-8">
    <ShopHeader v-model="activeCategory" />

    <!-- Загрузка -->
    <div v-if="itemsQuery.isPending.value" class="flex-1 flex items-center justify-center">
      <p class="font-main text-brand-dark/40 text-sm">Загрузка товаров...</p>
    </div>

    <Transition v-else name="tab-switch" mode="out-in">
      <div :key="activeCategory" class="flex flex-col gap-4">
        <!-- Рекомендуем -->
        <section v-if="activeCategory === 'all' && recommended.length">
          <p class="font-main font-semibold text-brand-dark/60 text-xs uppercase tracking-wide mb-3">
            Рекомендуем
          </p>
          <div class="flex gap-3 overflow-x-auto pb-1 -mx-4 px-4">
            <ShopItemCard
              v-for="item in recommended"
              :key="item.id"
              :item="item"
              @click="selectedItem = item"
            />
          </div>
        </section>

        <!-- Промокоды -->
        <section v-if="visible('promo_code') && byCategory('promo_code').length">
          <div class="flex items-center justify-between mb-3">
            <p class="font-main font-semibold text-brand-dark/60 text-xs uppercase tracking-wide">
              Промокоды на товары и услуги
            </p>
          </div>
          <div class="flex flex-col gap-2">
            <ShopItemRow
              v-for="item in byCategory('promo_code')"
              :key="item.id"
              :item="item"
              @click="selectedItem = item"
            />
          </div>
        </section>

        <!-- Подписки -->
        <section v-if="visible('subscription') && byCategory('subscription').length">
          <div class="flex items-center justify-between mb-3">
            <p class="font-main font-semibold text-brand-dark/60 text-xs uppercase tracking-wide">
              Подписки и сервисы
            </p>
          </div>
          <div class="flex flex-col gap-2">
            <ShopItemRow
              v-for="item in byCategory('subscription')"
              :key="item.id"
              :item="item"
              @click="selectedItem = item"
            />
          </div>
        </section>

        <!-- Плюшки банка -->
        <section v-if="visible('bank_perk') && byCategory('bank_perk').length">
          <div class="flex items-center justify-between mb-3">
            <p class="font-main font-semibold text-brand-dark/60 text-xs uppercase tracking-wide">
              Плюшки банка
            </p>
          </div>
          <div class="flex flex-col gap-2">
            <ShopItemRow
              v-for="item in byCategory('bank_perk')"
              :key="item.id"
              :item="item"
              @click="selectedItem = item"
            />
          </div>
        </section>
      </div>
    </Transition>

    <PurchaseModal
      v-if="selectedItem"
      :item="selectedItem"
      @close="selectedItem = null"
    />
  </div>
</template>

<style scoped>
.tab-switch-enter-active {
  transition: opacity 0.15s ease, transform 0.15s ease;
}
.tab-switch-leave-active {
  transition: opacity 0.1s ease;
}
.tab-switch-enter-from {
  opacity: 0;
  transform: translateY(6px);
}
.tab-switch-leave-to {
  opacity: 0;
}
</style>
