<script setup lang="ts">
import { RegisterForm } from '@/features/auth/register'
</script>

<template>
  <div class="min-h-[100dvh] bg-brand-dark flex flex-col items-center justify-center px-4 py-8 sm:px-6 lg:px-8">
    <div class="mb-8 sm:mb-10 text-center">
      <h1 class="font-accent text-3xl sm:text-4xl font-bold text-brand-white tracking-tight">
        MTBank
      </h1>
      <p class="text-brand-gray/70 text-xs sm:text-sm mt-2 font-main tracking-wider uppercase">
        Финансовые решения
      </p>
    </div>

    <div class="w-full max-w-sm sm:max-w-md bg-brand-white rounded-2xl shadow-2xl px-6 py-8 sm:px-8 sm:py-10">
      <div class="mb-6 sm:mb-8">
        <h2 class="font-accent text-xl sm:text-2xl font-semibold text-brand-black">Регистрация</h2>
        <p class="text-brand-gray text-xs sm:text-sm mt-1">Создайте аккаунт для доступа</p>
      </div>

      <RegisterForm />

      <p class="text-center text-xs sm:text-sm text-brand-gray mt-6 flex flex-col sm:block">
        Уже есть аккаунт?
        <RouterLink
          to="/login"
          class="text-brand-primary font-medium hover:underline sm:ml-1 mt-1 sm:mt-0 inline-block"
        >
          Войти
        </RouterLink>
      </p>
    </div>
  </div>
</template>
