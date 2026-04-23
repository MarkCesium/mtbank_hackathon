import { computed, ref } from 'vue'
import {
  ANIM_APPEAR_MS,
  ANIM_CLEAR_MS,
  ANIM_POPUP_MS,
  BOARD_SIZE,
  LINE_SCORE,
  WIN_SCORE,
  type Board,
  type FloatingScore,
  type GameStatus,
  type Hand,
  type PieceDef,
} from '@/entities/game'
import {
  applyClears,
  canPlace,
  collectClearedKeys,
  createEmptyBoard,
  detectLines,
  isGameOver,
  placeShape,
} from './scoring'
import { generateHand } from './pieces'

const wait = (ms: number) => new Promise<void>((resolve) => setTimeout(resolve, ms))

let floatingIdCounter = 0

export function useGame() {
  const board = ref<Board>(createEmptyBoard())
  const hand = ref<Hand>(generateHand())
  const score = ref(0)
  const status = ref<GameStatus>('idle')
  const isAnimating = ref(false)

  const newCells = ref<Set<string>>(new Set())
  const clearingCells = ref<Set<string>>(new Set())
  const floaters = ref<FloatingScore[]>([])

  const progress = computed(() => Math.min(100, Math.round((score.value / WIN_SCORE) * 100)))

  function reset() {
    board.value = createEmptyBoard()
    hand.value = generateHand()
    score.value = 0
    status.value = 'playing'
    newCells.value = new Set()
    clearingCells.value = new Set()
    floaters.value = []
    isAnimating.value = false
  }

  function spawnFloater(row: number, col: number, value: number) {
    const id = ++floatingIdCounter
    floaters.value = [...floaters.value, { id, row, col, value }]
    setTimeout(() => {
      floaters.value = floaters.value.filter((f) => f.id !== id)
    }, ANIM_POPUP_MS)
  }

  async function tryPlace(slotIndex: number, row: number, col: number): Promise<boolean> {
    if (isAnimating.value || status.value !== 'playing') return false
    const piece = hand.value[slotIndex]
    if (!piece) return false
    if (!canPlace(board.value, piece.shape, row, col)) return false

    isAnimating.value = true

    const placedKeys = new Set<string>()
    for (let r = 0; r < piece.shape.length; r += 1) {
      for (let c = 0; c < piece.shape[r].length; c += 1) {
        if (piece.shape[r][c]) placedKeys.add(`${row + r}:${col + c}`)
      }
    }
    board.value = placeShape(board.value, piece.shape, row, col)
    newCells.value = placedKeys

    const nextHand = [...hand.value] as Hand
    nextHand[slotIndex] = null
    hand.value = nextHand

    await wait(ANIM_APPEAR_MS)
    newCells.value = new Set()

    const detected = detectLines(board.value)
    const totalLines = detected.clearedRows.length + detected.clearedCols.length

    if (totalLines > 0) {
      const clearingKeys = collectClearedKeys(detected)
      clearingCells.value = clearingKeys

      for (const r of detected.clearedRows) {
        spawnFloater(r, Math.floor(BOARD_SIZE / 2), LINE_SCORE)
      }
      for (const c of detected.clearedCols) {
        spawnFloater(Math.floor(BOARD_SIZE / 2), c, LINE_SCORE)
      }

      score.value += totalLines * LINE_SCORE

      await wait(ANIM_CLEAR_MS)
      board.value = applyClears(board.value, clearingKeys)
      clearingCells.value = new Set()
    }

    if (hand.value.every((p) => p === null)) {
      hand.value = generateHand()
    }

    if (score.value >= WIN_SCORE) {
      status.value = 'won'
    } else if (
      isGameOver(
        board.value,
        hand.value.map((p) => (p ? p.shape : null)),
      )
    ) {
      status.value = 'lost'
    }

    isAnimating.value = false
    return true
  }

  function canPlacePiece(piece: PieceDef, row: number, col: number): boolean {
    return canPlace(board.value, piece.shape, row, col)
  }

  return {
    board,
    hand,
    score,
    status,
    progress,
    isAnimating,
    newCells,
    clearingCells,
    floaters,
    reset,
    tryPlace,
    canPlacePiece,
    BOARD_SIZE,
  }
}

export type GameState = ReturnType<typeof useGame>
