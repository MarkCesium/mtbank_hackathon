const AVATAR_COLORS = [
  '#4A90D9',
  '#E86060',
  '#5BAD72',
  '#D4A843',
  '#9B6DD4',
  '#E87B3A',
  '#48AAAD',
  '#C76FAA',
]

export function getAvatarColor(userId: string): string {
  let hash = 0
  for (const char of userId) hash = ((hash * 31) + char.charCodeAt(0)) >>> 0
  return AVATAR_COLORS[hash % AVATAR_COLORS.length]
}
