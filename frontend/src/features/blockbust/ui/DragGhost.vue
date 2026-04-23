<script setup lang="ts">
import type { DragInfo } from '../model/useDragPiece'
import PieceView from './PieceView.vue'

interface Props {
  drag: DragInfo
}

const props = defineProps<Props>()
</script>

<template>
  <Teleport to="body">
    <div
      class="fixed z-50 pointer-events-none"
      :style="{
        left: `${props.drag.x - props.drag.offsetX}px`,
        top: `${props.drag.y - props.drag.offsetY}px`,
      }"
    >
      <PieceView :piece="props.drag.piece" :cell-size="props.drag.cellSize" />
    </div>
  </Teleport>
</template>
