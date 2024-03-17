<template>
    <div v-for="(shortData, l) in allData" v-if="loaded">
        <div class="heading-for-each-wikisource">
            <h2 v-if="l === 'old'">wikisource.org</h2>
            <h2 v-else>{{ l }}.wikisource.org</h2>
        </div>
        <intial-stat-view :lang="l" :start="start" :end="end" :showChange="showChange" :showCharts="true" :filtering="filtering" :short="short" :shortData="shortData"></intial-stat-view>
    </div>
    <cdx-progress-bar inline v-else></cdx-progress-bar>
</template>

<script lang="ts">
import { ref, type Ref, defineComponent } from 'vue'
import IntialStatView from '../components/IntialStatView.vue';
import { CdxProgressBar } from '@wikimedia/codex';

export default defineComponent({
    name: 'StatsAllView',
    components: {IntialStatView, CdxProgressBar},
    setup() {
        const allData: Ref<Object> = ref([]);
        const loaded = ref(false);
        const filtering = ref('day');
        const showCharts = ref(true);
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
        } else if ( path.endsWith( 'lastweek' ) ) {
            let tmStart = new Date();
            tmStart.setDate( tmEnd.getDate() - 7 );
            fetchurlend = `${ serializeTm( tmStart ) }/${ serializeTm( tmEnd ) }`
        } else if ( path.endsWith( 'lastyear' ) ) {
            let tmStart = new Date();
            tmStart.setDate( tmEnd.getDate() - 365 );
            fetchurlend = `${ serializeTm( tmStart ) }/${ serializeTm( tmEnd ) }`
            filtering.value = 'month';
        } else if ( path.endsWith( 'lastmonth' ) ) {
            let tmStart = new Date();
            tmStart.setDate( tmEnd.getDate() - 30 );
            fetchurlend = `${ serializeTm( tmStart ) }/${ serializeTm( tmEnd ) }`
            filtering.value = 'month';
        } else if ( path.endsWith( 'alltime' ) ) {
            fetchurlend = `0/${ serializeTm( tmEnd ) }`
            filtering.value = 'year';
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
            shortData: true
        }
    },
})
</script>
<style lang="less" scoped>
@import '@wikimedia/codex-design-tokens/theme-wikimedia-ui.less';
.heading-for-each-wikisource {
    width: 75%;
    margin: auto;
    padding: @spacing-100;
    position: sticky;
    top: 0;
    z-index: 100;
    background: @background-color-interactive;
    h2 {
        margin: 0;
    }
}

</style>