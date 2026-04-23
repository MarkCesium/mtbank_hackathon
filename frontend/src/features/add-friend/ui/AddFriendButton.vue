<script setup lang="ts">
import { Link, Check } from '@lucide/vue'
import { useInviteLink } from '../composables/useInviteLink'

const { copied, copyInviteLink } = useInviteLink()
</script>

<template>
  <button
    class="flex items-center justify-center gap-2 w-full bg-brand-primary hover:bg-brand-primary/90 text-brand-white font-main font-semibold px-4 py-3 rounded-xl transition"
    @click="copyInviteLink"
  >
    <Check v-if="copied" :size="18" />
    <Link v-else :size="18" />
    <span>{{ copied ? 'Приглашение скопировано!' : 'Добавить друга' }}</span>
  </button>
</template>
