<template>
    <div>
        <cdx-progress-bar inline v-if="!loaded"></cdx-progress-bar>
        <stats-table-view :allData="allData" :type="type" v-if="loaded && !pathname.endsWith( 'alltime' )"></stats-table-view>
        <template v-if="loaded && !pathname.endsWith( 'yesterday' )">
            <div v-for="(shortData, l) in allData" v-bind:key="l">
            <intial-stat-view :lang="l" :start="start" :end="end" :showChange="showChange" :showCharts="true" :filtering="filtering" :short="short" :shortData="shortData"></intial-stat-view>
        </div>
        </template>
    </div>
</template>

<script lang="ts">
import { ref, type Ref, defineComponent } from 'vue'
import IntialStatView from '../components/IntialStatView.vue';
import { CdxProgressBar } from '@wikimedia/codex';
import StatsTableView from '../components/StatsTableView.vue';

export default defineComponent({
    name: 'StatsAllView',
    components: {IntialStatView, CdxProgressBar, StatsTableView},
    setup() {
        const allData: Ref<Object> = ref({});
        const pathname = ref( new URL( location.href ).pathname );
        const loaded = ref(false);
        const filtering = ref('day');
        const showCharts = ref(true);
        const type = ref('day');
        const serializeTm  = ( tm: Date ) => Math.floor( tm.getTime() / 1000 );
        const path = new URL( location.href ).pathname;
        let fetchurlend = 'alltime';
        const tmEnd = new Date();
        tmEnd.setHours(0);
        tmEnd.setMinutes(0);
        tmEnd.setSeconds(0);
        if ( path.endsWith( 'yesterday' ) ) {
            let tmStart = new Date();
            tmStart.setTime( tmEnd.getTime() - (86400000 - 1) * 2 );
            fetchurlend = `${ serializeTm( tmStart ) }/${ serializeTm( tmEnd ) }`
            showCharts.value = false;
            type.value = 'day';
        } else if ( path.endsWith( 'lastweek' ) ) {
            let tmStart = new Date();
            tmStart.setDate( tmEnd.getDate() - 7 );
            fetchurlend = `${ serializeTm( tmStart ) }/${ serializeTm( tmEnd ) }`
            type.value = 'week';
        } else if ( path.endsWith( 'lastyear' ) ) {
            let tmStart = new Date();
            tmStart.setDate( tmEnd.getDate() - 365 );
            fetchurlend = `${ serializeTm( tmStart ) }/${ serializeTm( tmEnd ) }`
            type.value = 'year';
        } else if ( path.endsWith( 'lastmonth' ) ) {
            let tmStart = new Date();
            tmStart.setDate( tmEnd.getDate() - 30 );
            fetchurlend = `${ serializeTm( tmStart ) }/${ serializeTm( tmEnd ) }`
            filtering.value = 'day';
            type.value = 'month';
        } else if ( path.endsWith( 'alltime' ) ) {
            fetchurlend = `0/${ serializeTm( tmEnd ) }`
            filtering.value = 'month';
            type.value = 'year';
        }
        fetch( `/api/all/${ fetchurlend }` )
        .then( ( resp ) => resp.json() )
        .then( ( val ) => {
            allData.value = val;
            loaded.value = true;
        });
        return {
            allData,
            loaded,
            start: '0',
            end: String( Math.floor( tmEnd.getTime() / 1000 ) ),
            showChange: false,
            showCharts: showCharts,
            filtering: filtering,
            short: true,
            shortData: true,
            pathname,
            type,
        }
    },
})
</script>