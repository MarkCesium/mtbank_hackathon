import { computed, ref, type Ref } from 'vue'
import { BOARD_SIZE, type PieceDef } from '@/entities/game'
import type { GameState } from './useGame'

export interface DragInfo {
  slotIndex: number
  piece: PieceDef
  pointerId: number
  offsetX: number
  offsetY: number
  x: number
  y: number
  cellSize: number
}

export interface PreviewInfo {
  row: number
  col: number
  valid: boolean
}

export function useDragPiece(game: GameState, boardEl: Ref<HTMLElement | null>) {
  const dragging = ref<DragInfo | null>(null)

  const preview = computed<PreviewInfo | null>(() => {
    if (!dragging.value || !boardEl.value) return null
    const rect = boardEl.value.getBoundingClientRect()
    const cellSize = rect.width / BOARD_SIZE
    const pieceLeft = dragging.value.x - dragging.value.offsetX
    const pieceTop = dragging.value.y - dragging.value.offsetY
    const col = Math.round((pieceLeft - rect.left) / cellSize)
    const row = Math.round((pieceTop - rect.top) / cellSize)
    const valid = game.canPlacePiece(dragging.value.piece, row, col)
    return { row, col, valid }
  })

  function onMove(e: PointerEvent) {
    if (!dragging.value || e.pointerId !== dragging.value.pointerId) return
    dragging.value = { ...dragging.value, x: e.clientX, y: e.clientY }
  }

  function cleanup() {
    window.removeEventListener('pointermove', onMove)
    window.removeEventListener('pointerup', onEnd)
    window.removeEventListener('pointercancel', onEnd)
    dragging.value = null
  }

  function onEnd(e: PointerEvent) {
    if (!dragging.value || e.pointerId !== dragging.value.pointerId) return
    const p = preview.value
    const slot = dragging.value.slotIndex
    if (p && p.valid) {
      game.tryPlace(slot, p.row, p.col)
    }
    cleanup()
  }

  function startDrag(event: PointerEvent, slotIndex: number, piece: PieceDef) {
    if (game.status.value !== 'playing' || game.isAnimating.value) return
    event.preventDefault()
    const target = event.currentTarget as HTMLElement
    const rect = target.getBoundingClientRect()
    const offsetX = event.clientX - rect.left
    const offsetY = event.clientY - rect.top
    const boardRect = boardEl.value?.getBoundingClientRect()
    const cellSize = boardRect ? boardRect.width / BOARD_SIZE : 36
    dragging.value = {
      slotIndex,
      piece,
      pointerId: event.pointerId,
      offsetX,
      offsetY,
      x: event.clientX,
      y: event.clientY,
      cellSize,
    }
    window.addEventListener('pointermove', onMove)
    window.addEventListener('pointerup', onEnd)
    window.addEventListener('pointercancel', onEnd)
  }

  return { dragging, preview, startDrag, cleanup }
}

export type DragState = ReturnType<typeof useDragPiece>
