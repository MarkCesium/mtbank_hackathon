import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { useMutation } from '@tanstack/vue-query'
import type { AxiosError } from 'axios'
import { authApi } from '@/shared/api/auth'
import { useUserStore } from '@/entities/user'

interface ErrorResponse {
  detail: string
}

export function useLogin() {
  const router = useRouter()
  const userStore = useUserStore()

  const { mutate, isPending, error } = useMutation({
    mutationFn: ({ username, password }: { username: string; password: string }) =>
      authApi.login(username, password).then((r) => r.data),
    onSuccess: (data) => {
      userStore.setTokens(data.access_token, data.refresh_token)
      router.push('/')
    },
  })

  const errorMessage = computed(() => {
    if (!error.value) return null
    const axiosError = error.value as AxiosError<ErrorResponse>
    return axiosError.response?.data?.detail ?? 'Ошибка входа. Проверьте данные.'
  })

  return { login: mutate, isLoading: isPending, errorMessage }
}
