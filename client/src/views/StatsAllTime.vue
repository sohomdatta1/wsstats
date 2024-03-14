<template>
    <intial-stat-view :lang="lang" :start="start" :end="end" :showChange="showChange" :showCharts="true" :filtering="filtering"></intial-stat-view>
</template>
<script lang="ts">
import { ref, type Ref, defineComponent } from 'vue'
import { useRoute } from 'vue-router';
import IntialStatView from '../components/IntialStatView.vue';

export default defineComponent({
    name: 'StatsMonthView',
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
        return {
            lang,
            start: '0',
            end: String( Math.floor( tmEnd.getTime() / 1000 ) ),
            showChange: false,
            showCharts: true,
            filtering: 'year'
        }
    },
})
</script>
