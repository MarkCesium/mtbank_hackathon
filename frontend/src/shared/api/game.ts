import { apiClient } from './client'

export interface StartAttemptResponse {
  attempts_remaining: number
}

export interface FinishAttemptRequest {
  score: number
  won: boolean
}

export interface FinishAttemptResponse {
  bonus: string
  attempts_remaining: number
  awarded: string
}

export const gameApi = {
  start: () => apiClient.post<StartAttemptResponse>('/game/start'),
  finish: (data: FinishAttemptRequest) =>
    apiClient.post<FinishAttemptResponse>('/game/finish', data),
}
