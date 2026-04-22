<script setup lang="ts">
import { computed, ref } from 'vue'

type AuthView = 'login' | 'register'

const activeView = ref<AuthView>('login')
const showDemoNotice = ref(false)
const isSubmitting = ref(false)
const title = computed(() =>
  activeView.value === 'login' ? 'Вход в аккаунт' : 'Создание аккаунта',
)

const handleSubmit = () => {
  isSubmitting.value = true
  showDemoNotice.value = true
  setTimeout(() => {
    isSubmitting.value = false
    showDemoNotice.value = false
  }, 3000)
}
</script>

<template>
  <main class="auth-bg min-h-screen px-4 py-8 sm:px-6">
    <div class="mx-auto w-full max-w-md rounded-2xl border border-brand-gray/30 bg-brand-white p-8 shadow-2xl">
      <header class="mb-7 text-center">
        <p class="font-digital text-xs uppercase tracking-[0.22em] text-brand-primary">MTBank</p>
        <h1 id="auth-title" class="mt-3 font-accent text-4xl leading-tight text-brand-black">{{ title }}</h1>
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

      <form class="space-y-4" aria-labelledby="auth-title" @submit.prevent="handleSubmit">
        <label for="email" class="block text-sm text-brand-dark">
          Email
          <input
            id="email"
            type="email"
            class="mt-1 w-full rounded-xl border border-brand-gray/60 px-4 py-3 outline-none transition focus:border-brand-primary focus:ring-2 focus:ring-brand-primary/20"
            placeholder="name@mail.com"
            autocomplete="email"
            required
          />
        </label>

        <label for="password" class="block text-sm text-brand-dark">
          Пароль
          <input
            id="password"
            type="password"
            class="mt-1 w-full rounded-xl border border-brand-gray/60 px-4 py-3 outline-none transition focus:border-brand-primary focus:ring-2 focus:ring-brand-primary/20"
            placeholder="••••••••"
            :autocomplete="activeView === 'login' ? 'current-password' : 'new-password'"
            :aria-describedby="activeView === 'register' ? 'password-hint' : undefined"
            required
          />
        </label>
        <p v-if="activeView === 'register'" id="password-hint" class="text-xs text-brand-dark/70">
          Используйте минимум 8 символов, включая буквы и цифры.
        </p>

        <label v-if="activeView === 'register'" for="confirm-password" class="block text-sm text-brand-dark">
          Подтвердите пароль
          <input
            id="confirm-password"
            type="password"
            class="mt-1 w-full rounded-xl border border-brand-gray/60 px-4 py-3 outline-none transition focus:border-brand-secondary focus:ring-2 focus:ring-brand-secondary/20"
            placeholder="••••••••"
            autocomplete="new-password"
            aria-describedby="password-hint"
            required
          />
        </label>

        <button
          type="submit"
          class="mt-1 w-full rounded-xl px-4 py-3 font-main font-semibold text-brand-white transition-opacity hover:opacity-90 disabled:cursor-not-allowed disabled:opacity-70"
          :class="activeView === 'login' ? 'bg-brand-primary' : 'bg-brand-secondary'"
          :aria-busy="isSubmitting"
          :disabled="isSubmitting"
        >
          {{ isSubmitting ? 'Отправка...' : activeView === 'login' ? 'Войти' : 'Зарегистрироваться' }}
        </button>
        <p v-if="showDemoNotice" class="text-center text-xs text-brand-dark/70">
          Демо-экран: интеграция формы будет подключена на следующем этапе.
        </p>
      </form>
    </div>
  </main>
</template>
