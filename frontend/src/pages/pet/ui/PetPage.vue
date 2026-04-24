<script setup lang="ts">
import { ref } from 'vue'
import { PetUploadModal } from '@/features/pet-upload'
import maskot from '@/assets/maskot.png'

const showUploadModal = ref(false)
</script>

<template>
  <div class="flex-1 w-full flex flex-col gap-4 pb-8">
    <div class="bg-brand-primary rounded-2xl p-6 flex flex-col items-center gap-3 shadow-sm">
      <div class="w-48 h-48 overflow-hidden flex items-center justify-center">
        <img
          :src="maskot"
          alt="МТКотик"
          class="w-full h-full object-contain scale-[1.5] drop-shadow-lg"
        />
      </div>
      <div class="flex flex-col items-center gap-1.5">
        <span class="font-digital text-2xl text-brand-white leading-tight">МТКотик</span>
        <div class="bg-brand-dark/20 px-2.5 py-0.5 rounded-full text-[10px] font-main text-brand-white/80">
          Котость + Пиратость :>
        </div>
      </div>
    </div>

    <div class="bg-brand-white rounded-2xl p-5 flex flex-col gap-4 shadow-sm mb-12">
      <p class="font-main font-semibold text-brand-dark/60 text-xs uppercase tracking-wide">
        О питомцах
      </p>
      <p class="font-main text-sm text-brand-dark/70 leading-relaxed">
        Питомец сопровождает тебя в MTBank Rewards. Загрузи фото своего питомца — ИИ превратит его в уникального персонажа в нашем стиле.
      </p>
      <p class="font-main text-sm text-brand-dark/70 leading-relaxed">
        За первое прохождение MTPass банк подарит вам наклейку с изображением вашего питомца.
      </p>
      <span class="self-start bg-brand-secondary/10 text-brand-secondary rounded-full text-xs font-main font-medium px-3 py-1">
        ✦ AI-обработка
      </span>
      <button
        class="bg-brand-primary text-brand-white font-main font-semibold py-3 rounded-xl w-full transition hover:bg-brand-primary/90 active:scale-[0.98]"
        @click="showUploadModal = true"
      >
        Загрузить своего питомца
      </button>
    </div>

    <PetUploadModal v-if="showUploadModal" @close="showUploadModal = false" />
  </div>
</template>
