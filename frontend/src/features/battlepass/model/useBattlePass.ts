import { useQuery } from '@tanstack/vue-query'
import { battlepassApi } from '@/shared/api/battlepass'

export const BATTLEPASS_QUERY_KEY = ['battlepass', 'current'] as const

export function useBattlePass() {
  const query = useQuery({
    queryKey: BATTLEPASS_QUERY_KEY,
    queryFn: async () => {
      const { data } = await battlepassApi.current()
      return data
    },
    staleTime: 60_000,
  })

  return {
    state: query.data,
    isLoading: query.isPending,
    isError: query.isError,
    refetch: query.refetch,
  }
}
