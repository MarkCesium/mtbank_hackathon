<script setup lang="ts">
import { AppHeader } from '@/widgets/app-header'
</script>

<template>
  <div class="min-h-[100dvh] bg-brand-gray flex flex-col items-center p-6 pb-[88px]">
    <header class="w-full max-w-md flex flex-col gap-4">
      <AppHeader />
    </header>

    <main class="flex-1 w-full max-w-md flex flex-col items-center justify-center gap-4 text-center">
      <p class="text-brand-dark/50 font-main text-sm">Скоро здесь появятся товары</p>
    </main>
  </div>
</template>
