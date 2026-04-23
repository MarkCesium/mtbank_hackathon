<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { X } from '@lucide/vue'
import type { ShopItem } from '@/entities/shop-item'
import { usePurchase } from '../model/usePurchase'

const props = defineProps<{ item: ShopItem }>()
const emit = defineEmits<{ close: [] }>()

const { mutate, isPending, isSuccess, data, error, reset } = usePurchase()

const visible = ref(false)
onMounted(() => { visible.value = true })

const errorMessage = computed(() => {
  if (!error.value) return null
  const resp = (error.value as any)?.response?.data?.detail
  return resp ?? 'Ошибка при покупке'
})

function handlePurchase() {
  mutate(props.item.id)
}

async function handleClose() {
  visible.value = false
  await new Promise(r => setTimeout(r, 280))
  reset()
  emit('close')
}
</script>

<template>
  <Teleport to="body">
    <!-- Backdrop -->
    <Transition name="backdrop">
      <div
        v-show="visible"
        class="fixed inset-0 z-50 bg-brand-black/50 backdrop-blur-sm"
        @click="handleClose"
      />
    </Transition>

    <!-- Sheet -->
    <Transition name="sheet">
      <div
        v-show="visible"
        class="fixed inset-x-0 bottom-0 z-50 flex justify-center pointer-events-none"
      >
        <div class="w-full max-w-md bg-brand-white rounded-t-3xl p-6 pb-10 shadow-2xl pointer-events-auto">
          <div class="flex items-center justify-between mb-5">
            <h2 class="font-main font-bold text-brand-dark text-lg">
              {{ isSuccess ? 'Покупка совершена!' : 'Подтвердите покупку' }}
            </h2>
            <button class="text-brand-dark/40 hover:text-brand-dark transition" @click="handleClose">
              <X class="w-5 h-5" />
            </button>
          </div>

          <!-- Результат покупки -->
          <template v-if="isSuccess && data">
            <div class="bg-brand-gray rounded-2xl p-4 mb-5">
              <p class="font-main text-brand-dark/60 text-xs mb-1">Ваш промокод / активация:</p>
              <p class="font-digital text-brand-dark font-bold text-base break-all">
                {{ data.payload }}
              </p>
            </div>
            <div class="flex items-center justify-between mb-5">
              <span class="font-main text-brand-dark/60 text-sm">Новый баланс</span>
              <span class="font-digital text-brand-primary font-bold text-xl">
                {{ data.new_balance }} <span class="text-sm font-main font-normal">бонусов</span>
              </span>
            </div>
            <button
              class="w-full bg-brand-primary text-brand-white font-main font-semibold py-3 rounded-xl transition hover:bg-brand-primary/90"
              @click="handleClose"
            >
              Закрыть
            </button>
          </template>

          <!-- Форма подтверждения -->
          <template v-else>
            <div class="flex items-start gap-3 mb-5">
              <div class="w-12 h-12 rounded-xl bg-brand-gray flex items-center justify-center flex-shrink-0">
                <span class="text-brand-primary font-accent font-bold text-lg">
                  {{ (item.brand_name ?? item.title).charAt(0) }}
                </span>
              </div>
              <div>
                <p class="font-main font-semibold text-brand-dark">{{ item.title }}</p>
                <p class="font-main text-brand-dark/50 text-sm mt-0.5">{{ item.description }}</p>
              </div>
            </div>

            <div class="flex items-center justify-between bg-brand-gray rounded-2xl p-4 mb-5">
              <span class="font-main text-brand-dark/60 text-sm">Стоимость</span>
              <span class="font-digital text-brand-dark font-bold text-xl">
                {{ item.price }} <span class="text-sm font-main font-normal">бонусов</span>
              </span>
            </div>

            <p v-if="errorMessage" class="text-brand-secondary text-sm font-main text-center mb-4">
              {{ errorMessage }}
            </p>

            <div class="flex gap-3">
              <button
                class="flex-1 border border-brand-gray text-brand-dark/60 font-main font-semibold py-3 rounded-xl transition hover:border-brand-dark/20"
                :disabled="isPending"
                @click="handleClose"
              >
                Отмена
              </button>
              <button
                class="flex-1 bg-brand-primary text-brand-white font-main font-semibold py-3 rounded-xl transition hover:bg-brand-primary/90 disabled:bg-brand-gray/60 disabled:cursor-not-allowed"
                :disabled="isPending"
                @click="handlePurchase"
              >
                {{ isPending ? 'Загрузка...' : 'Купить' }}
              </button>
            </div>
          </template>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<style scoped>
.backdrop-enter-active,
.backdrop-leave-active {
  transition: opacity 0.25s ease;
}
.backdrop-enter-from,
.backdrop-leave-to {
  opacity: 0;
}

.sheet-enter-active,
.sheet-leave-active {
  transition: transform 0.3s cubic-bezier(0.32, 0.72, 0, 1);
}
.sheet-enter-from,
.sheet-leave-to {
  transform: translateY(100%);
}
</style>
