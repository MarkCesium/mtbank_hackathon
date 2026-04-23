import { apiClient } from './client'

export interface RegisterRequest {
  username: string
  email: string
  password: string
}

export interface RegisterResponse {
  user_id: string
}

export interface TokenResponse {
  access_token: string
  refresh_token: string
}

export interface UserResponse {
  user_id: string
  username: string
  email: string
  bonus: string
  attempts_remaining: number
}

export const authApi = {
  register: (data: RegisterRequest) => apiClient.post<RegisterResponse>('/auth/register', data),

  login: (username: string, password: string) => {
    const params = new URLSearchParams({ username, password })
    return apiClient.post<TokenResponse>('/auth/login', params, {
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    })
  },

  logout: (refreshToken: string) =>
    apiClient.post<{ success: boolean }>('/auth/logout', { refresh_token: refreshToken }),

  me: () => apiClient.get<UserResponse>('/auth/me'),
}
