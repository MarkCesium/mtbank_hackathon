import { ref } from 'vue'
import { useUserStore } from '@/entities/user'

export function useInviteLink() {
  const userStore = useUserStore()
  const copied = ref(false)

  async function copyInviteLink() {
    const userId = userStore.user?.user_id
    if (!userId) return

    const link = `${window.location.origin}/friends?invite=${userId}`

    try {
      await navigator.clipboard.writeText(link)
    } catch {
      const el = document.createElement('textarea')
      el.value = link
      el.style.position = 'fixed'
      el.style.opacity = '0'
      document.body.appendChild(el)
      el.focus()
      el.select()
      document.execCommand('copy')
      document.body.removeChild(el)
    }

    copied.value = true
    setTimeout(() => {
      copied.value = false
    }, 2000)
  }

  return { copied, copyInviteLink }
}
