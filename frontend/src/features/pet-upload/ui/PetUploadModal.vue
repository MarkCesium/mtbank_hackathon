<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { ImagePlus, X } from '@lucide/vue'

const emit = defineEmits<{ close: [] }>()

const visible = ref(false)
onMounted(() => { visible.value = true })

async function handleClose() {
  visible.value = false
  await new Promise(r => setTimeout(r, 280))
  emit('close')
}
</script>

<template>
  <Teleport to="body">
    <Transition name="backdrop">
      <div
        v-show="visible"
        class="fixed inset-0 z-50 bg-brand-black/50 backdrop-blur-sm"
        @click="handleClose"
      />
    </Transition>

    <Transition name="sheet">
      <div
        v-show="visible"
        class="fixed inset-x-0 bottom-0 z-50 flex justify-center pointer-events-none"
      >
        <div class="w-full max-w-md bg-brand-white rounded-t-3xl p-6 pb-10 shadow-2xl pointer-events-auto">
          <div class="flex items-center justify-between mb-5">
            <h2 class="font-main font-bold text-brand-dark text-lg">Загрузи своего питомца</h2>
            <button class="text-brand-dark/40 hover:text-brand-dark transition" @click="handleClose">
              <X class="w-5 h-5" />
            </button>
          </div>

          <p class="font-main text-sm text-brand-dark/60 leading-relaxed mb-5">
            ИИ обработает фото и создаст уникального питомца в стиле MTBank.
          </p>

          <div class="border-2 border-dashed border-brand-dark/20 rounded-xl p-8 flex flex-col items-center gap-3 opacity-50 cursor-not-allowed select-none mb-4">
            <ImagePlus class="w-8 h-8 text-brand-dark/40" />
            <span class="font-main text-sm text-brand-dark/50">Выбрать фото</span>
          </div>

          <p class="text-center text-xs font-main text-brand-dark/40 mb-5">
            ✨ Функция скоро появится
          </p>

          <button
            class="w-full bg-brand-primary text-brand-white font-main font-semibold py-3 rounded-xl transition hover:bg-brand-primary/90"
            @click="handleClose"
          >
            Понятно
          </button>
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
