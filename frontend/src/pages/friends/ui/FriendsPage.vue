<script setup lang="ts">
import { onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useQuery, useQueryClient } from '@tanstack/vue-query'
import { authApi } from '@/shared/api/auth'
import { useUserStore } from '@/entities/user'
import { friendsApi } from '@/shared/api/friends'
import { AddFriendButton } from '@/features/add-friend'
import { FriendsLeaderboard } from '@/widgets/friends-leaderboard'

const route = useRoute()
const router = useRouter()
const queryClient = useQueryClient()
const userStore = useUserStore()

useQuery({
  queryKey: ['auth', 'me'],
  queryFn: async () => {
    const { data } = await authApi.me()
    userStore.setUser(data)
    return data
  },
})

onMounted(async () => {
  const inviteId = route.query.invite as string | undefined
  if (!inviteId) return

  await router.replace({ query: {} })

  try {
    await friendsApi.addFriend(inviteId)
    await queryClient.invalidateQueries({ queryKey: ['friends', 'leaderboard'] })
  } catch {
    // already friends or invalid id — silently ignore
  }
})
</script>

<template>
  <main class="flex-1 w-full flex flex-col gap-4">
    <AddFriendButton />
    <FriendsLeaderboard />
  </main>
</template>
