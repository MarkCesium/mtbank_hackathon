<script setup lang="ts">
import { computed, ref } from 'vue'

type AuthView = 'login' | 'register'

const activeView = ref<AuthView>('login')
const title = computed(() =>
  activeView.value === 'login' ? 'Вход в аккаунт' : 'Создание аккаунта',
)
</script>

<template>
  <main
    class="min-h-screen bg-[radial-gradient(circle_at_top,_#0d2f7f_0%,_#071d49_42%,_#010615_100%)] px-4 py-8 sm:px-6"
  >
    <div class="mx-auto w-full max-w-md rounded-2xl border border-brand-gray/30 bg-brand-white p-8 shadow-2xl">
      <header class="mb-7 text-center">
        <p class="font-digital text-xs uppercase tracking-[0.22em] text-brand-primary">MTBank</p>
        <h1 class="mt-3 font-accent text-4xl leading-tight text-brand-black">{{ title }}</h1>
        <p class="mt-2 text-sm text-brand-dark/80">Безопасный доступ к вашему банковскому кабинету</p>
      </header>

      <div class="mb-6 grid grid-cols-2 rounded-xl bg-brand-dark/6 p-1 text-sm font-main">
        <button
          type="button"
          class="rounded-lg px-3 py-2 font-semibold transition-colors"
          :class="
            activeView === 'login'
              ? 'bg-brand-primary text-brand-white shadow-sm'
              : 'text-brand-dark hover:bg-brand-white/80'
          "
          @click="activeView = 'login'"
        >
          Логин
        </button>
        <button
          type="button"
          class="rounded-lg px-3 py-2 font-semibold transition-colors"
          :class="
            activeView === 'register'
              ? 'bg-brand-secondary text-brand-white shadow-sm'
              : 'text-brand-dark hover:bg-brand-white/80'
          "
          @click="activeView = 'register'"
        >
          Регистрация
        </button>
      </div>

      <form class="space-y-4" @submit.prevent>
        <label class="block text-sm text-brand-dark">
          Email
          <input
            type="email"
            class="mt-1 w-full rounded-xl border border-brand-gray/60 px-4 py-3 outline-none transition focus:border-brand-primary focus:ring-2 focus:ring-brand-primary/20"
            placeholder="name@mail.com"
            autocomplete="email"
          />
        </label>

        <label class="block text-sm text-brand-dark">
          Пароль
          <input
            type="password"
            class="mt-1 w-full rounded-xl border border-brand-gray/60 px-4 py-3 outline-none transition focus:border-brand-primary focus:ring-2 focus:ring-brand-primary/20"
            placeholder="••••••••"
            autocomplete="current-password"
          />
        </label>

        <label v-if="activeView === 'register'" class="block text-sm text-brand-dark">
          Подтвердите пароль
          <input
            type="password"
            class="mt-1 w-full rounded-xl border border-brand-gray/60 px-4 py-3 outline-none transition focus:border-brand-secondary focus:ring-2 focus:ring-brand-secondary/20"
            placeholder="••••••••"
            autocomplete="new-password"
          />
        </label>

        <button
          type="submit"
          class="mt-1 w-full rounded-xl px-4 py-3 font-main font-semibold text-brand-white transition-opacity hover:opacity-90"
          :class="activeView === 'login' ? 'bg-brand-primary' : 'bg-brand-secondary'"
        >
          {{ activeView === 'login' ? 'Войти' : 'Зарегистрироваться' }}
        </button>
      </form>
    </div>
  </main>
</template>
