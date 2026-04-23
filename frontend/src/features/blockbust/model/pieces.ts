import type { PieceDef, PieceShape } from '@/entities/game'

interface PieceBlueprint {
  id: string
  shape: PieceShape
  color: string
}

const PIECES: PieceBlueprint[] = [
  { id: 'dot', color: '#0021f3', shape: [[1]] },
  {
    id: 'h2',
    color: '#0021f3',
    shape: [[1, 1]],
  },
  {
    id: 'v2',
    color: '#0021f3',
    shape: [[1], [1]],
  },
  {
    id: 'h3',
    color: '#14b8a6',
    shape: [[1, 1, 1]],
  },
  {
    id: 'v3',
    color: '#14b8a6',
    shape: [[1], [1], [1]],
  },
  {
    id: 'h4',
    color: '#f59e0b',
    shape: [[1, 1, 1, 1]],
  },
  {
    id: 'v4',
    color: '#f59e0b',
    shape: [[1], [1], [1], [1]],
  },
  {
    id: 'h5',
    color: '#f84b36',
    shape: [[1, 1, 1, 1, 1]],
  },
  {
    id: 'v5',
    color: '#f84b36',
    shape: [[1], [1], [1], [1], [1]],
  },
  {
    id: 'sq2',
    color: '#a855f7',
    shape: [
      [1, 1],
      [1, 1],
    ],
  },
  {
    id: 'sq3',
    color: '#ec4899',
    shape: [
      [1, 1, 1],
      [1, 1, 1],
      [1, 1, 1],
    ],
  },
  {
    id: 'l-tl',
    color: '#22c55e',
    shape: [
      [1, 0],
      [1, 0],
      [1, 1],
    ],
  },
  {
    id: 'l-tr',
    color: '#22c55e',
    shape: [
      [0, 1],
      [0, 1],
      [1, 1],
    ],
  },
  {
    id: 'l-bl',
    color: '#22c55e',
    shape: [
      [1, 1],
      [1, 0],
      [1, 0],
    ],
  },
  {
    id: 'l-br',
    color: '#22c55e',
    shape: [
      [1, 1],
      [0, 1],
      [0, 1],
    ],
  },
  {
    id: 'corner-tl',
    color: '#3b82f6',
    shape: [
      [1, 0],
      [1, 1],
    ],
  },
  {
    id: 'corner-tr',
    color: '#3b82f6',
    shape: [
      [0, 1],
      [1, 1],
    ],
  },
  {
    id: 'corner-bl',
    color: '#3b82f6',
    shape: [
      [1, 1],
      [1, 0],
    ],
  },
  {
    id: 'corner-br',
    color: '#3b82f6',
    shape: [
      [1, 1],
      [0, 1],
    ],
  },
  {
    id: 't-up',
    color: '#e11d48',
    shape: [
      [1, 1, 1],
      [0, 1, 0],
    ],
  },
  {
    id: 't-down',
    color: '#e11d48',
    shape: [
      [0, 1, 0],
      [1, 1, 1],
    ],
  },
  {
    id: 's',
    color: '#eab308',
    shape: [
      [0, 1, 1],
      [1, 1, 0],
    ],
  },
  {
    id: 'z',
    color: '#eab308',
    shape: [
      [1, 1, 0],
      [0, 1, 1],
    ],
  },
]

let pieceCounter = 0

function instantiate(blueprint: PieceBlueprint): PieceDef {
  pieceCounter += 1
  return {
    id: blueprint.id,
    key: `${blueprint.id}-${pieceCounter}`,
    shape: blueprint.shape,
    color: blueprint.color,
  }
}

export function randomPiece(): PieceDef {
  const blueprint = PIECES[Math.floor(Math.random() * PIECES.length)]
  return instantiate(blueprint)
}

export function generateHand(): [PieceDef, PieceDef, PieceDef] {
  return [randomPiece(), randomPiece(), randomPiece()]
}
