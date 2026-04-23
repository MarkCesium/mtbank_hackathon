export type Cell = 0 | 1
export type Board = Cell[][]
export type PieceShape = Cell[][]

export interface PieceDef {
  id: string
  key: string
  shape: PieceShape
  color: string
}

export type HandSlot = PieceDef | null
export type Hand = [HandSlot, HandSlot, HandSlot]

export type GameStatus = 'idle' | 'playing' | 'won' | 'lost'

export const BOARD_SIZE = 10
export const WIN_SCORE = 1000
export const LINE_SCORE = 50

export const ANIM_APPEAR_MS = 100
export const ANIM_CLEAR_MS = 300
export const ANIM_POPUP_MS = 500

export interface FloatingScore {
  id: number
  row: number
  col: number
  value: number
}
