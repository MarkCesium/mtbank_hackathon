<script setup lang="ts">
import type { Hand, PieceDef } from '@/entities/game'
import PieceView from './PieceView.vue'

interface Props {
  hand: Hand
  draggingSlot: number | null
  cellSize?: number
}

const props = withDefaults(defineProps<Props>(), { cellSize: 24 })

const emit = defineEmits<{
  pickup: [event: PointerEvent, slot: number, piece: PieceDef]
}>()

function onPointerDown(e: PointerEvent, slot: number) {
  const piece = props.hand[slot]
  if (!piece) return
  emit('pickup', e, slot, piece)
}
</script>

<template>
  <div class="flex justify-around items-end w-full py-3 px-2">
    <div
      v-for="(piece, slot) in props.hand"
      :key="slot"
      class="flex items-center justify-center min-h-[90px] min-w-[90px]"
    >
      <div
        v-if="piece"
        class="cursor-grab active:cursor-grabbing touch-none"
        @pointerdown="(e) => onPointerDown(e, slot)"
      >
        <PieceView :piece="piece" :cell-size="cellSize" :dim="draggingSlot === slot" />
      </div>
    </div>
  </div>
</template>
