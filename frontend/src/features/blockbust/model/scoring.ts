import { BOARD_SIZE, type Board, type PieceShape } from '@/entities/game'

export function createEmptyBoard(): Board {
  return Array.from({ length: BOARD_SIZE }, () =>
    Array.from({ length: BOARD_SIZE }, () => 0 as const),
  )
}

export function cloneBoard(board: Board): Board {
  return board.map((row) => [...row])
}

export function canPlace(board: Board, shape: PieceShape, row: number, col: number): boolean {
  for (let r = 0; r < shape.length; r += 1) {
    for (let c = 0; c < shape[r].length; c += 1) {
      if (!shape[r][c]) continue
      const br = row + r
      const bc = col + c
      if (br < 0 || br >= BOARD_SIZE || bc < 0 || bc >= BOARD_SIZE) return false
      if (board[br][bc]) return false
    }
  }
  return true
}

export function placeShape(board: Board, shape: PieceShape, row: number, col: number): Board {
  const next = cloneBoard(board)
  for (let r = 0; r < shape.length; r += 1) {
    for (let c = 0; c < shape[r].length; c += 1) {
      if (shape[r][c]) next[row + r][col + c] = 1
    }
  }
  return next
}

export interface DetectResult {
  clearedRows: number[]
  clearedCols: number[]
}

export function detectLines(board: Board): DetectResult {
  const clearedRows: number[] = []
  const clearedCols: number[] = []

  for (let r = 0; r < BOARD_SIZE; r += 1) {
    if (board[r].every((cell) => cell === 1)) clearedRows.push(r)
  }
  for (let c = 0; c < BOARD_SIZE; c += 1) {
    let full = true
    for (let r = 0; r < BOARD_SIZE; r += 1) {
      if (!board[r][c]) {
        full = false
        break
      }
    }
    if (full) clearedCols.push(c)
  }
  return { clearedRows, clearedCols }
}

export function collectClearedKeys(result: DetectResult): Set<string> {
  const keys = new Set<string>()
  for (const r of result.clearedRows) {
    for (let c = 0; c < BOARD_SIZE; c += 1) keys.add(`${r}:${c}`)
  }
  for (const c of result.clearedCols) {
    for (let r = 0; r < BOARD_SIZE; r += 1) keys.add(`${r}:${c}`)
  }
  return keys
}

export function applyClears(board: Board, keys: Set<string>): Board {
  if (keys.size === 0) return board
  const next = cloneBoard(board)
  for (const key of keys) {
    const [r, c] = key.split(':').map(Number)
    next[r][c] = 0
  }
  return next
}

export function hasAnyPlacement(board: Board, shape: PieceShape): boolean {
  for (let r = 0; r < BOARD_SIZE; r += 1) {
    for (let c = 0; c < BOARD_SIZE; c += 1) {
      if (canPlace(board, shape, r, c)) return true
    }
  }
  return false
}

export function isGameOver(board: Board, shapes: (PieceShape | null)[]): boolean {
  const remaining = shapes.filter((s): s is PieceShape => s !== null)
  if (remaining.length === 0) return false
  return remaining.every((shape) => !hasAnyPlacement(board, shape))
}
