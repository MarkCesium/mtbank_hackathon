import { apiClient } from './client'

export interface LeaderboardEntry {
  user_id: string
  username: string
  bonus: string
  rank: number
  is_current_user: boolean
}

export const friendsApi = {
  leaderboard: () =>
    apiClient.get<{ entries: LeaderboardEntry[] }>('/friends/leaderboard'),
  addFriend: (friend_id: string) =>
    apiClient.post('/friends/add', { friend_id }),
}
