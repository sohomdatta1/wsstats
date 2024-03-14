import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import StatsYesterdayView from '../views/StatsYesterdayView.vue'
import StatsYearView from '@/views/StatsYearView.vue'
import StatsLastMonth from '@/views/StatsLastMonth.vue'
import StatsLastWeek from '@/views/StatsLastWeek.vue'
import StatsAllTime from '@/views/StatsAllTime.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/stats/:lang/yesterday',
      name: 'yesterday-stats',
      component: StatsYesterdayView
    },
    {
      path: '/stats/:lang/lastyear',
      name: 'lastyear-stats',
      component: StatsYearView
    },
    {
      path: '/stats/:lang/lastmonth',
      name: 'lastmonth-stats',
      component: StatsLastMonth
    },
    {
      path: '/stats/:lang/lastweek',
      name: 'lastweek-stats',
      component: StatsLastWeek
    },
    {
      path: '/stats/:lang/alltime',
      name: 'all-time',
      component: StatsAllTime
    }
  ]
})

export default router
