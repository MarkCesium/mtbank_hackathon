import type { Component } from 'vue'
import { ShoppingCart, Tv, Zap, Crown } from '@lucide/vue'
import type { RewardType } from './types'

export function rewardIcon(type: RewardType): Component {
  switch (type) {
    case 'promo_shop':
      return ShoppingCart
    case 'promo_sub':
      return Tv
    case 'cashback_boost':
      return Zap
    case 'package_month':
      return Crown
  }
}

export function rewardIconColor(type: RewardType): string {
  switch (type) {
    case 'promo_shop':
      return 'text-blue-600'
    case 'promo_sub':
      return 'text-violet-600'
    case 'cashback_boost':
      return 'text-emerald-600'
    case 'package_month':
      return 'text-amber-500'
  }
}

export function isMilestone(type: RewardType): boolean {
  return type === 'cashback_boost'
}

export function isGrandPrize(type: RewardType): boolean {
  return type === 'package_month'
}
