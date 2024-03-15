<template>
    <div v-for="l of allLangs" v-if="loaded">
        <div class="heading-for-each-wikisource">
            <h2 v-if="l === 'old'">wikisource.org</h2>
            <h2 v-else>{{ l }}.wikisource.org</h2>
        </div>
        <intial-stat-view :lang="l" :start="start" :end="end" :showChange="showChange" :showCharts="true" :filtering="filtering" :short="short"></intial-stat-view>
    </div>
</template>

<script lang="ts">
import { ref, type Ref, defineComponent } from 'vue'
import IntialStatView from '../components/IntialStatView.vue';

export default defineComponent({
    name: 'StatsAllAllTime',
    components: {IntialStatView},
    setup() {
        const allLangs: Ref<Array<string>> = ref([]);
        const loaded = ref(false);
        fetch( '/api/all_langs' )
        .then( ( resp ) => resp.json() )
        .then( ( val ) => {
            allLangs.value = val;
            loaded.value = true;
        });
        const tmEnd = new Date();
        tmEnd.setHours(0);
        tmEnd.setMinutes(0);
        tmEnd.setSeconds(0);
        return {
            allLangs,
            loaded,
            start: '0',
            end: String( Math.floor( tmEnd.getTime() / 1000 ) ),
            showChange: false,
            showCharts: true,
            filtering: 'year',
            short: true
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