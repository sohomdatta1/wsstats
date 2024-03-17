<template>
    <intial-stat-view :lang="lang" :start="start" :end="end" :showChange="showChange"></intial-stat-view>
</template>
<script lang="ts">
import { ref, type Ref, defineComponent } from 'vue'
import { useRoute } from 'vue-router';
import IntialStatView from '../components/IntialStatView.vue';

export default defineComponent({
    name: 'StatsView',
    components: {
        IntialStatView
    },
    setup() { 
        const route = useRoute();
        const lang: Ref<string> = ref('en');
        lang.value = String(route.params.lang);
        const filtering = ref('day');
        const showCharts = ref(true);
        const serializeTm  = ( tm: Date ) => String( Math.floor( tm.getTime() / 1000 ) );
        const path = new URL( location.href ).pathname;
        const tmEnd = new Date();
        tmEnd.setHours(0);
        tmEnd.setMinutes(0);
        tmEnd.setSeconds(0);
        let tmStart = new Date();
        if ( path.endsWith( 'yesterday' ) ) {
            tmStart.setTime( tmEnd.getTime() - (86400000 - 1) * 2 );
            showCharts.value = false;
        } else if ( path.endsWith( 'lastweek' ) ) {
            tmStart.setDate( tmEnd.getDate() - 7 );
        } else if ( path.endsWith( 'lastyear' ) ) {
            let tmStart = new Date();
            tmStart.setDate( tmEnd.getDate() - 365 );
            filtering.value = 'month';
        } else if ( path.endsWith( 'lastmonth' ) ) {
            tmStart.setDate( tmEnd.getDate() - 30 );
            filtering.value = 'month';
        } else if ( path.endsWith( 'alltime' ) ) {
            tmStart = new Date(0);
            filtering.value = 'year';
        }
        return {
            lang,
            start: serializeTm( tmStart ),
            end: serializeTm( tmEnd ),
            showChange: true
        }
    },
})
</script>