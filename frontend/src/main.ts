import { createApp } from 'vue'
import App from './App.vue'

import './app/styles/tailwind.css'
import { store } from './app/providers/store'
import { queryPlugin, queryClientOptions } from './app/providers/query'
import router from './app/router'

const app = createApp(App)

app.use(store)
app.use(queryPlugin, queryClientOptions)
app.use(router)

app.mount('#app')
