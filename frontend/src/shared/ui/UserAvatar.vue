<script setup lang="ts">
import { computed } from 'vue'
import { getAvatarColor } from '@/shared/lib/avatar'

const props = withDefaults(
  defineProps<{
    userId: string
    username: string
    size?: 'sm' | 'md'
  }>(),
  { size: 'md' },
)

const letter = computed(() => props.username.charAt(0).toUpperCase())
const bgColor = computed(() => getAvatarColor(props.userId))
const sizeClass = computed(() =>
  props.size === 'sm' ? 'w-8 h-8 text-sm' : 'w-10 h-10 text-base',
)
</script>

<template>
  <div
    class="rounded-full flex items-center justify-center font-main font-semibold text-white shrink-0"
    :class="sizeClass"
    :style="{ backgroundColor: bgColor }"
  >
    {{ letter }}
  </div>
</template>
