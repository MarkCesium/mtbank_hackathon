<script setup lang="ts">
import { BottomNavBar } from '@/widgets/bottom-nav'
import { AppHeader } from '@/widgets/app-header'
</script>

<template>
  <div class="min-h-[100dvh] bg-brand-gray flex flex-col items-center p-6 pb-[88px]">
    <div class="w-full max-w-md flex flex-col gap-4 flex-1">
      <AppHeader />
      <RouterView />
    </div>
    <BottomNavBar />
  </div>
</template>
