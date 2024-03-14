<template>
    <intial-stat-view :lang="lang" :start="start" :end="end" :showChange="showChange"></intial-stat-view>
</template>
<script lang="ts">
import { ref, type Ref, defineComponent } from 'vue'
import { useRoute } from 'vue-router';
import IntialStatView from '../components/IntialStatView.vue';

export default defineComponent({
    name: 'StatsYesterdayView',
    components: {
        IntialStatView
    },
    setup() { 
        const route = useRoute();
        const lang: Ref<string> = ref('en');
        lang.value = String(route.params.lang);
        const tmEnd = new Date();
        tmEnd.setHours(0);
        tmEnd.setMinutes(0);
        tmEnd.setSeconds(0);
        let tmStart = new Date();
        tmStart.setTime( tmEnd.getTime() - (86400000 - 1) * 2 );
        return {
            lang,
            start: String( Math.floor( tmStart.getTime() / 1000 ) ),
            end: String( Math.floor( tmEnd.getTime() / 1000 ) ),
            showChange: true
        }
    },
})
</script>
