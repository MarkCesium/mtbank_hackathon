<script setup lang="ts">
import { computed, useTemplateRef } from 'vue'
import {
  BoardGrid,
  DragGhost,
  PieceTray,
  useDragPiece,
  type GameState,
} from '@/features/blockbust'
import type { PieceDef } from '@/entities/game'

interface Props {
  game: GameState
}

const props = defineProps<Props>()

const boardComp = useTemplateRef<{ rootEl: HTMLElement | null }>('boardComp')
const boardEl = computed(() => boardComp.value?.rootEl ?? null)

const drag = useDragPiece(props.game, boardEl)

const draggingSlot = computed(() => drag.dragging.value?.slotIndex ?? null)
const previewPiece = computed(() => drag.dragging.value?.piece ?? null)

function onPickup(e: PointerEvent, slot: number, piece: PieceDef) {
  drag.startDrag(e, slot, piece)
}
</script>

<template>
  <div class="w-full max-w-md mx-auto flex flex-col flex-1">
    <div class="flex-1"></div>
    <BoardGrid
      ref="boardComp"
      :board="props.game.board.value"
      :preview="drag.preview.value"
      :preview-piece="previewPiece"
      :new-cells="props.game.newCells.value"
      :clearing-cells="props.game.clearingCells.value"
      :floaters="props.game.floaters.value"
    />
    <div class="flex-1"></div>
    <div class="bg-brand-white/80 rounded-xl py-2">
      <PieceTray
        :hand="props.game.hand.value"
        :dragging-slot="draggingSlot"
        @pickup="onPickup"
      />
    </div>
    <DragGhost v-if="drag.dragging.value" :drag="drag.dragging.value" />
  </div>
</template>
