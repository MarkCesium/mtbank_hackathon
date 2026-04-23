<script setup lang="ts">
import { computed, ref } from 'vue'
import {
  ANIM_APPEAR_MS,
  ANIM_CLEAR_MS,
  ANIM_POPUP_MS,
  BOARD_SIZE,
  type Board,
  type FloatingScore,
  type PieceDef,
} from '@/entities/game'
import type { PreviewInfo } from '../model/useDragPiece'

interface Props {
  board: Board
  preview: PreviewInfo | null
  previewPiece: PieceDef | null
  newCells: Set<string>
  clearingCells: Set<string>
  floaters: FloatingScore[]
}

const props = defineProps<Props>()
const rootEl = ref<HTMLElement | null>(null)

defineExpose({ rootEl })

const previewCells = computed<Map<string, { valid: boolean; color: string }>>(() => {
  const cells = new Map<string, { valid: boolean; color: string }>()
  if (!props.preview || !props.previewPiece) return cells
  const { row, col, valid } = props.preview
  for (let r = 0; r < props.previewPiece.shape.length; r += 1) {
    for (let c = 0; c < props.previewPiece.shape[r].length; c += 1) {
      if (!props.previewPiece.shape[r][c]) continue
      const key = `${row + r}:${col + c}`
      cells.set(key, { valid, color: props.previewPiece.color })
    }
  }
  return cells
})

type CellKind = 'empty' | 'filled' | 'new' | 'clearing' | 'preview-valid' | 'preview-invalid'

function cellKind(r: number, c: number): CellKind {
  const key = `${r}:${c}`
  if (props.clearingCells.has(key)) return 'clearing'
  const preview = previewCells.value.get(key)
  if (preview) return preview.valid ? 'preview-valid' : 'preview-invalid'
  if (props.board[r][c] === 1) return props.newCells.has(key) ? 'new' : 'filled'
  return 'empty'
}

function cellStyle(r: number, c: number): Record<string, string> {
  const kind = cellKind(r, c)
  const preview = previewCells.value.get(`${r}:${c}`)
  const base: Record<string, string> = {}
  if (kind === 'new') base.animationDuration = `${ANIM_APPEAR_MS}ms`
  if (kind === 'clearing') base.animationDuration = `${ANIM_CLEAR_MS}ms`

  if (kind === 'preview-valid' && preview) {
    return {
      ...base,
      backgroundColor: preview.color,
      opacity: '0.65',
      boxShadow: 'inset 0 0 0 1px rgba(255,255,255,0.3)',
    }
  }
  if (kind === 'preview-invalid') {
    return {
      ...base,
      backgroundColor: '#ef4444',
      opacity: '0.45',
      boxShadow: 'inset 0 0 0 1px rgba(255,255,255,0.3)',
    }
  }
  if (kind === 'filled' || kind === 'new' || kind === 'clearing') {
    return {
      ...base,
      backgroundColor: '#0021f3',
      boxShadow: 'inset 0 0 0 1px rgba(255,255,255,0.25)',
    }
  }
  return {
    backgroundColor: 'rgba(255,255,255,0.04)',
    boxShadow: 'inset 0 0 0 1px rgba(255,255,255,0.06)',
  }
}

function floaterStyle(f: FloatingScore): Record<string, string> {
  return {
    left: `${((f.col + 0.5) / BOARD_SIZE) * 100}%`,
    top: `${((f.row + 0.5) / BOARD_SIZE) * 100}%`,
    animationDuration: `${ANIM_POPUP_MS}ms`,
  }
}
</script>

<template>
  <div
    ref="rootEl"
    class="relative grid gap-[2px] p-[6px] bg-brand-dark/60 rounded-xl touch-none select-none w-full"
    :style="{
      gridTemplateColumns: `repeat(${BOARD_SIZE}, 1fr)`,
      gridTemplateRows: `repeat(${BOARD_SIZE}, 1fr)`,
      aspectRatio: '1 / 1',
    }"
  >
    <template v-for="(row, r) in props.board" :key="r">
      <div
        v-for="(_cell, c) in row"
        :key="`${r}-${c}`"
        class="cell"
        :class="`cell-${cellKind(r, c)}`"
        :style="cellStyle(r, c)"
      ></div>
    </template>

    <div
      v-for="f in props.floaters"
      :key="f.id"
      class="floater font-digital text-brand-white"
      :style="floaterStyle(f)"
    >
      +{{ f.value }}
    </div>
  </div>
</template>

<style scoped>
.cell {
  border-radius: 4px;
  will-change: transform, opacity;
}

.cell-new {
  animation-name: cell-appear;
  animation-timing-function: ease-out;
}

.cell-clearing {
  animation-name: cell-clear;
  animation-timing-function: ease-in;
  animation-fill-mode: forwards;
  z-index: 1;
}

.floater {
  position: absolute;
  transform: translate(-50%, -50%);
  pointer-events: none;
  font-size: 1.5rem;
  font-weight: 700;
  text-shadow: 0 2px 6px rgba(0, 0, 0, 0.55);
  animation-name: floater-up;
  animation-timing-function: ease-out;
  animation-fill-mode: forwards;
  z-index: 2;
}

@keyframes cell-appear {
  0% {
    transform: scale(0.6);
    opacity: 0;
  }
  100% {
    transform: scale(1);
    opacity: 1;
  }
}

@keyframes cell-clear {
  0% {
    transform: scale(1);
    filter: brightness(1);
    opacity: 1;
  }
  45% {
    transform: scale(1.12);
    filter: brightness(2.2);
    opacity: 1;
  }
  100% {
    transform: scale(0.3);
    filter: brightness(2.2);
    opacity: 0;
  }
}

@keyframes floater-up {
  0% {
    transform: translate(-50%, -50%) scale(0.7);
    opacity: 0;
  }
  20% {
    transform: translate(-50%, -70%) scale(1.1);
    opacity: 1;
  }
  100% {
    transform: translate(-50%, -160%) scale(1);
    opacity: 0;
  }
}
</style>
