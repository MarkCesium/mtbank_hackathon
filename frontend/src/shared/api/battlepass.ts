import { apiClient } from './client'

export type DayState = 'completed' | 'active' | 'available' | 'missed' | 'locked'
export type RewardType = 'promo_shop' | 'promo_sub' | 'cashback_boost' | 'package_month'

export interface BattlePassDay {
  day: number
  state: DayState
  reward_type: RewardType
  reward_title: string
  reward_description: string
}

export interface BattlePassStateResponse {
  year: number
  month: number
  month_days_count: number
  today_day: number
  is_frozen: boolean
  days: BattlePassDay[]
}

export const battlepassApi = {
  current: () => apiClient.get<BattlePassStateResponse>('/battlepass/current'),
}
