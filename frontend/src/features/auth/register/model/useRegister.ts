import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { useMutation } from '@tanstack/vue-query'
import type { AxiosError } from 'axios'
import { authApi, type RegisterRequest } from '@/shared/api/auth'

interface ErrorResponse {
  detail: string
}

export function useRegister() {
  const router = useRouter()

  const { mutate, isPending, error } = useMutation({
    mutationFn: (data: RegisterRequest) => authApi.register(data).then((r) => r.data),
    onSuccess: () => {
      router.push('/login')
    },
  })

  const errorMessage = computed(() => {
    if (!error.value) return null
    const axiosError = error.value as AxiosError<ErrorResponse>
    return axiosError.response?.data?.detail ?? 'Ошибка регистрации. Попробуйте снова.'
  })

  return { register: mutate, isLoading: isPending, errorMessage }
}
