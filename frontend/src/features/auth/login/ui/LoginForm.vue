<script setup lang="ts">
import { ref } from 'vue'
import { useLogin } from '../model/useLogin'

const { login, isLoading, errorMessage } = useLogin()

const username = ref('')
const password = ref('')

function handleSubmit() {
  login({ username: username.value, password: password.value })
}
</script>

<template>
  <form class="flex flex-col gap-4 sm:gap-5" @submit.prevent="handleSubmit">
    <div class="flex flex-col gap-1.5">
      <label class="text-xs sm:text-sm font-medium text-brand-black/60 tracking-wide uppercase">Email</label>
      <input
        v-model="username"
        type="email"
        autocomplete="email"
        required
        placeholder="example@mail.com"
        class="border border-brand-gray/60 rounded-xl px-3 py-2.5 sm:px-4 sm:py-3 text-sm sm:text-base text-brand-black placeholder:text-brand-black/40 focus:outline-none focus:border-brand-primary focus:ring-1 focus:ring-brand-primary transition-colors"
      />
    </div>

    <div class="flex flex-col gap-1.5">
      <label class="text-xs sm:text-sm font-medium text-brand-black/60 tracking-wide uppercase">Пароль</label>
      <input
        v-model="password"
        type="password"
        autocomplete="current-password"
        required
        placeholder="Введите пароль"
        class="border border-brand-gray/60 rounded-xl px-3 py-2.5 sm:px-4 sm:py-3 text-sm sm:text-base text-brand-black placeholder:text-brand-black/40 focus:outline-none focus:border-brand-primary focus:ring-1 focus:ring-brand-primary transition-colors"
      />
    </div>

    <Transition name="fade">
      <div
        v-if="errorMessage"
        class="flex items-center gap-2 bg-brand-secondary/10 border border-brand-secondary/20 text-brand-secondary text-xs sm:text-sm rounded-xl px-3 py-2 sm:px-4 sm:py-3"
      >
        <span>{{ errorMessage }}</span>
      </div>
    </Transition>

    <button
      type="submit"
      :disabled="isLoading"
      class="w-full bg-brand-primary text-brand-white font-medium py-3 sm:py-3.5 rounded-xl hover:opacity-90 active:opacity-80 disabled:opacity-50 transition-opacity mt-1 text-sm sm:text-base"
    >
      <span v-if="isLoading" class="inline-flex items-center gap-2">
        <svg
          class="animate-spin h-4 w-4"
          fill="none"
          viewBox="0 0 24 24"
          xmlns="http://www.w3.org/2000/svg"
        >
          <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" />
          <path
            class="opacity-75"
            fill="currentColor"
            d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"
          />
        </svg>
        Входим...
      </span>
      <span v-else>Войти</span>
    </button>
  </form>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition:
    opacity 0.2s ease,
    transform 0.2s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(-4px);
}
</style>
