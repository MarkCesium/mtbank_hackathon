<script setup lang="ts">
import type { PieceDef } from '@/entities/game'

interface Props {
  piece: PieceDef
  cellSize?: number
  dim?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  cellSize: 28,
  dim: false,
})
</script>

<template>
  <div
    class="grid gap-[2px] touch-none select-none"
    :style="{
      gridTemplateColumns: `repeat(${props.piece.shape[0].length}, ${props.cellSize}px)`,
      gridTemplateRows: `repeat(${props.piece.shape.length}, ${props.cellSize}px)`,
      opacity: props.dim ? 0.3 : 1,
    }"
  >
    <template v-for="(row, r) in props.piece.shape" :key="r">
      <div
        v-for="(cell, c) in row"
        :key="`${r}-${c}`"
        :style="{
          backgroundColor: cell ? props.piece.color : 'transparent',
          borderRadius: '4px',
          boxShadow: cell ? 'inset 0 0 0 1px rgba(255,255,255,0.25)' : undefined,
        }"
      ></div>
    </template>
  </div>
</template>
