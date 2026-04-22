<script setup lang="ts">
import { RegisterForm } from '@/features/auth/register'
import { AuthLayout } from '@/shared/ui/layouts'
</script>

<template>
  <AuthLayout footer-link-to="/login" footer-link-text="Войти">
    <template #header>
      <h2 class="font-accent text-xl sm:text-2xl font-semibold text-brand-black">Регистрация</h2>
      <p class="text-brand-gray text-xs sm:text-sm mt-1">Создайте аккаунт для доступа</p>
    </template>

    <template #form>
      <RegisterForm />
    </template>

    <template #footer-link-prefix>
      Уже есть аккаунт?
    </template>
  </AuthLayout>
</template>
