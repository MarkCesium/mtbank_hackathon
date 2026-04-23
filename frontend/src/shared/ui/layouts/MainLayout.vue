<script setup lang="ts">
import { BottomNavBar } from '@/widgets/bottom-nav'
import { AppHeader } from '@/widgets/app-header'
</script>

<template>
  <div class="min-h-[100dvh] bg-brand-gray flex flex-col items-center p-6 pb-[88px]">
    <div class="w-full max-w-md flex flex-col gap-4 flex-1">
      <AppHeader />
      <RouterView v-slot="{ Component }">
        <Transition name="page" mode="out-in">
          <component :is="Component" />
        </Transition>
      </RouterView>
    </div>
    <BottomNavBar />
  </div>
</template>

<style scoped>
.page-enter-active,
.page-leave-active {
  transition: opacity 0.15s ease, transform 0.15s ease;
}
.page-enter-from {
  opacity: 0;
  transform: translateY(6px);
}
.page-leave-to {
  opacity: 0;
  transform: translateY(-4px);
}
</style>
