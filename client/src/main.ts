import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import SmartTable from 'vuejs-smart-table'

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(SmartTable)


app.mount('#app')
