import type { RewardType } from './types'

export function rewardIcon(type: RewardType): string {
  switch (type) {
    case 'promo_shop':
      return '🛒'
    case 'promo_sub':
      return '🎬'
    case 'cashback_boost':
      return '💰'
    case 'package_month':
      return '👑'
  }
}

export function isMilestone(type: RewardType): boolean {
  return type === 'cashback_boost'
}

export function isGrandPrize(type: RewardType): boolean {
  return type === 'package_month'
}
