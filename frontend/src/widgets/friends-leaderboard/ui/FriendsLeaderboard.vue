<script setup lang="ts">
import { useQuery } from '@tanstack/vue-query'
import { friendsApi, type LeaderboardEntry } from '@/shared/api/friends'
import { UserAvatar } from '@/shared/ui'

defineExpose({ queryKey: ['friends', 'leaderboard'] })

const { data, isPending } = useQuery({
  queryKey: ['friends', 'leaderboard'],
  queryFn: async () => {
    const { data } = await friendsApi.leaderboard()
    return data
  },
})

const hasOnlyCurrentUser = (entries: LeaderboardEntry[]) =>
  entries.every((e) => e.is_current_user)
</script>

<template>
  <div class="w-full flex flex-col gap-2">
    <h2 class="text-brand-dark font-main font-semibold text-base px-1">Лидерборд</h2>

    <div v-if="isPending" class="flex flex-col gap-2">
      <div
        v-for="i in 3"
        :key="i"
        class="bg-brand-white rounded-2xl h-14 animate-pulse"
      />
    </div>

    <template v-else-if="data?.entries">
      <p
        v-if="hasOnlyCurrentUser(data.entries)"
        class="text-brand-dark/50 font-main text-sm text-center py-6"
      >
        Добавьте своего первого друга!
      </p>

      <div
        v-for="(entry, index) in data.entries"
        :key="entry.user_id"
        class="flex items-center bg-brand-white gap-3 px-4 py-3 rounded-2xl transition stagger-item"
        :style="{ animationDelay: `${index * 50}ms` }"
      >
        <span class="text-brand-dark/40 font-main text-sm w-5 text-center shrink-0">
          {{ entry.rank }}
        </span>

        <UserAvatar :user-id="entry.user_id" :username="entry.username" size="sm" />

        <span
          class="flex-1 font-main text-sm truncate"
          :class="entry.is_current_user ? 'text-brand-primary font-semibold' : 'text-brand-dark'"
        >
          {{ entry.username }}
          <span v-if="entry.is_current_user" class="text-xs font-normal"> (вы)</span>
        </span>

        <span class="font-digital text-brand-dark text-base shrink-0">
          {{ Number(entry.bonus).toFixed(2) }}
        </span>
      </div>
    </template>
  </div>
</template>

<style scoped>
.stagger-item {
  animation: stagger-in 0.2s ease-out both;
}

@keyframes stagger-in {
  from {
    opacity: 0;
    transform: translateY(6px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
