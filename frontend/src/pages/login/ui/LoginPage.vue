<script setup lang="ts">
import { LoginForm } from '@/features/auth/login'
import { AuthLayout } from '@/shared/ui/layouts'
</script>

<template>
  <AuthLayout footer-link-to="/register" footer-link-text="Зарегистрироваться">
    <template #header>
      <h2 class="font-accent text-xl sm:text-2xl font-semibold text-brand-black">Вход в аккаунт</h2>
      <p class="text-brand-black text-xs sm:text-sm mt-1">Введите данные для входа</p>
    </template>

    <template #form>
      <LoginForm />
    </template>

    <template #footer-link-prefix>
      Нет аккаунта?
    </template>
  </AuthLayout>
</template>
