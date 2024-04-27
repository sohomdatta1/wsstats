import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import StatsView from '../views/StatsNormalView.vue'
import StatsAllView from '@/views/StatsAllView.vue'

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
      component: StatsView
    },
    {
      path: '/stats/:lang/lastyear',
      name: 'lastyear-stats',
      component: StatsView
    },
    {
      path: '/stats/:lang/lastmonth',
      name: 'lastmonth-stats',
      component: StatsView
    },
    {
      path: '/stats/:lang/lastweek',
      name: 'lastweek-stats',
      component: StatsView
    },
    {
      path: '/stats/:lang/alltime',
      name: 'all-time',
      component: StatsView
    },
    {
      path: '/stats/all/alltime',
      name: 'all-all-time',
      component: StatsAllView
    },
    {
      path: '/stats/all/yesterday',
      name: 'all-yesterday',
      component: StatsAllView
    },
    {
      path: '/stats/all/lastweek',
      name: 'all-lastweek',
      component: StatsAllView
    },
    {
      path: '/stats/all/lastyear',
      name: 'all-lastyear',
      component: StatsAllView
    },

    {
      path: '/stats/all/lastmonth',
      name: 'all-lastmonth',
      component: StatsAllView
    },
    {
      path: '/stats/all/yesterday',
      name: 'yesterday-all-stats',
      component: StatsAllView
    }
  ]
})

export default router
