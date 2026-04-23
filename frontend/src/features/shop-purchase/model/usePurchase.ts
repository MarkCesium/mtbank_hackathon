import { useMutation, useQueryClient } from '@tanstack/vue-query'
import { shopApi } from '@/shared/api/shop'

export function usePurchase() {
  const queryClient = useQueryClient()

  const mutation = useMutation({
    mutationFn: (shopItemId: string) => shopApi.purchase(shopItemId).then((r) => r.data),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['auth', 'me'] })
    },
  })

  return mutation
}
