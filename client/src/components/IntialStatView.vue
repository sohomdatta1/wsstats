<template>
    <div class="initial-stats-container">
        <cdx-card
            :class="changeAll > 0 ? 'up' : changeAll == 0 ? 'pause' : 'down'"
            :icon="changeAll > 0 ? cdxIconCollapse : changeAll == 0 ? cdxIconPause : cdxIconExpand">
            <template #title>
                Total number of pages
            </template>
            <template #description>
                {{ totalAll }} <span class="change-num" v-if="$props.showChange">({{ changeAll }})</span>
                <div class="pr-percentage-wrapper">
                    <div class="pr-percentage-bar">
                        <div class="pr-percentage-bar-inner" :style="{ width: `${percentagePr}%` }"></div>
                    </div>
                    {{ isNaN(percentagePr) ? 0 : percentagePr }}% of the pages are proofread
                </div>

                <line-chart-vue v-if="loaded && $props.showCharts" :chartData="chartAll" :chartOptions="chartOptions"></line-chart-vue>
            </template>
        </cdx-card>
        <cdx-card 
            :class="changeValidated > 0 ? 'up' : changeValidated == 0 ? 'pause' : 'down'"
            :icon="changeProofread > 0 ? cdxIconCollapse : changeProofread == 0 ? cdxIconPause : cdxIconExpand">
            <template #title>
                Number of texts
            </template>
            <template #description>
                {{ totalTexts }} <span class="change-num" v-if="$props.showChange">({{ changeTexts }})</span>
                <line-chart-vue v-if="loaded && $props.showCharts" :chartData="chartText" :chartOptions="chartOptions"></line-chart-vue>
            </template>
        </cdx-card>
        <cdx-card
            :class="changeTrans > 0 ? 'up' : changeTrans == 0 ? 'pause' : 'down'"
            v-if="!$props.short"
            :icon="changeTrans > 0 ? cdxIconCollapse : changeTrans == 0 ? cdxIconPause : cdxIconExpand">
            <template #title>
                Number of transclusions
            </template>
            <template #description>
                {{ totalTrans }} <span class="change-num" v-if="$props.showChange">({{ changeTrans }})</span>
                <line-chart-vue v-if="loaded && $props.showCharts" :chartData="chartTrans" :chartOptions="chartOptions"></line-chart-vue>
            </template>
        </cdx-card>
        <cdx-card
            :class="changeWithoutText > 0 ? 'up' : changeWithoutText == 0 ? 'pause' : 'down'"
            v-if="!$props.short"
            :icon="changeWithoutText > 0 ? cdxIconCollapse : changeWithoutText == 0 ? cdxIconPause : cdxIconExpand">
            <template #title>
                Number of pages without text
            </template>
            <template #description>
                {{ totalWithoutText }} <span class="change-num" v-if="$props.showChange">({{ changeWithoutText }})</span>
                <line-chart-vue v-if="loaded && $props.showCharts" :chartData="chartWithoutText" :chartOptions="chartOptions"></line-chart-vue>
            </template>
        </cdx-card>
        <cdx-card
            :class="changeUnproofread > 0 ? 'down' : changeUnproofread == 0 ? 'pause' : 'up'"
            v-if="!$props.short"
            :icon="changeUnproofread > 0 ? cdxIconCollapse : changeUnproofread == 0 ? cdxIconPause : cdxIconExpand">
            <template #title>
                Number of unproofread pages 
            </template>
            <template #description>
                {{ totalUnproofread }} <span class="change-num" v-if="$props.showChange">({{ changeUnproofread }})</span>
                <line-chart-vue v-if="loaded && $props.showCharts" :chartData="chartUnproofread" :chartOptions="chartOptions"></line-chart-vue>
            </template>
        </cdx-card>
        <cdx-card
            :class="changeProblematic > 0 ? 'down' : changeProblematic == 0 ? 'pause' : 'up'"
            v-if="!$props.short"
            :icon="changeProblematic > 0 ? cdxIconCollapse : changeProblematic == 0 ? cdxIconPause : cdxIconExpand">
            <template #title>
                Number of problematic pages 
            </template>
            <template #description>
                {{  totalProblematic }} <span class="change-num" v-if="$props.showChange">({{ changeProblematic }})</span>
                <line-chart-vue v-if="loaded && $props.showCharts" :chartData="chartProblematic" :chartOptions="chartOptions"></line-chart-vue>
            </template>
        </cdx-card>
        <cdx-card 
            :class="[changeProofread > 0 ? 'up' : changeProofread == 0 ? 'pause' : 'down']"
            v-if="!$props.short"
            :icon="changeProofread > 0 ? cdxIconCollapse : changeProofread == 0 ? cdxIconPause : cdxIconExpand">
            <template #title>
                Number of proofread pages
            </template>
            <template #description>
                {{  totalProofread }} <span class="change-num" v-if="$props.showChange">({{ changeProofread }})</span>
                <line-chart-vue v-if="loaded && $props.showCharts" :chartData="chartProofread" :chartOptions="chartOptions"></line-chart-vue>
            </template>
        </cdx-card>
        <cdx-card 
            :class="changeValidated > 0 ? 'up' : changeValidated == 0 ? 'pause' : 'down'"
            v-if="!$props.short"
            :icon="changeValidated > 0 ? cdxIconCollapse : changeValidated == 0 ? cdxIconPause : cdxIconExpand">
            <template #title>
                Number of validated pages 
            </template>
            <template #description>
                {{ totalValidated }} <span class="change-num" v-if="$props.showChange">({{ changeValidated }})</span>
                <line-chart-vue v-if="loaded && $props.showCharts" :chartData="chartValidated" :chartOptions="chartOptions"></line-chart-vue>
            </template>
        </cdx-card>
        <cdx-card 
            :class="changeValidated > 0 ? 'up' : changeValidated == 0 ? 'pause' : 'down'"
            v-if="!$props.short"
            :icon="changeProofread > 0 ? cdxIconCollapse : changeProofread == 0 ? cdxIconPause : cdxIconExpand">
            <template #title>
                Number of disambiguated pages
            </template>
            <template #description>
                {{ totalDab }} <span class="change-num" v-if="$props.showChange">({{ changeDab }})</span>
                <line-chart-vue v-if="loaded && $props.showCharts" :chartData="chartDab" :chartOptions="chartOptions"></line-chart-vue>
            </template>
        </cdx-card>
    </div>
</template>

<script lang="ts">
import { ref, defineComponent } from 'vue'
import { CdxCard } from '@wikimedia/codex';
import { cdxIconCollapse, cdxIconExpand, cdxIconPause } from '@wikimedia/codex-icons';
import LineChartVue from './LineChart.vue';
import clone from './util'

export default defineComponent({
    name: 'InitialStatView',
    props: {
        "lang": String,
        "start": String,
        "end": String,
        "showChange": Boolean,
        "showCharts": Boolean,
        "filtering": String,
        "pageType": String,
        "short": Boolean
    },
    components: {
        CdxCard,
        LineChartVue
    },
    data: () => ({
        cdxIconExpand,
        cdxIconCollapse,
        cdxIconPause,
        chartOptions: {
            responsive: true,
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero:false
                        }
                    }],
                    xAxes: [{
                        ticks: {
                            padding: 100,
                            autoSkip: true
                        }
                    }]
                }
            }
        }
    } ),
    setup( props ) {
        const totalAll = ref(0);
        const loaded = ref(false);
        const totalTrans = ref(0);
        const totalUnproofread = ref(0);
        const totalProblematic = ref(0);
        const totalProofread = ref(0);
        const totalValidated = ref(0);
        const totalWithoutText = ref(0);
        const totalTexts =  ref(0);
        const totalDab = ref(0);
        const percentagePr = ref(0);
        const changeAll = ref(0);
        const changeTrans = ref(0);
        const changeUnproofread = ref(0);
        const changeProblematic = ref(0);
        const changeProofread = ref(0);
        const changeWithoutText = ref(0);
        const changeValidated = ref(0);
        const changeTexts = ref(0);
        const changeDab = ref(0);
        const chartAll = ref({});
        const chartTrans = ref({});
        const chartUnproofread = ref({});
        const chartProblematic = ref({});
        const chartProofread = ref({});
        const chartValidated = ref({});
        const chartWithoutText = ref({});
        const chartText = ref({});
        const chartDab = ref({});
        const lang = props.lang;
        fetch( `/api/stats/${ lang }/${ props.start }/${ props.end }` ).then( 
            ( r ) => {
                return r.json();
            }
        ).then(
            ( data ) => {
                console.log( props )
                const currentData = data['data'][data['data']['length'] - 1];
                const dataBefore = data['data'][0];
                totalAll.value = currentData[1];
                totalWithoutText.value = currentData[2];
                totalProblematic.value = currentData[3];
                totalUnproofread.value = currentData[1] - ( currentData[2] + currentData[3] + currentData[4] + currentData[5] );
                // round to two places after decimal point
                percentagePr.value =  Math.round((( currentData[4] + currentData[5] ) / currentData[1]) * 10000) / 100;
                totalProofread.value = currentData[4];
                totalValidated.value = currentData[5];
                totalTrans.value = currentData[6];
                totalTexts.value = currentData[7]
                totalDab.value = currentData[8];
                changeAll.value = currentData[1] - dataBefore[1];
                changeWithoutText.value = currentData[2] - dataBefore[2];
                changeProblematic.value = currentData[3] - dataBefore[3];
                changeUnproofread.value = totalUnproofread.value - (dataBefore[1] - ( dataBefore[2] + dataBefore[3] + dataBefore[4] + dataBefore[5] ) );
                changeProofread.value = currentData[4] - dataBefore[4];
                changeValidated.value = currentData[5] - dataBefore[5];
                changeTrans.value = currentData[6] - dataBefore[6];
                changeTexts.value = currentData[7] - dataBefore[7];
                changeDab.value = currentData[8] - dataBefore[8];
                let serializedData: Array<Array<number>> = [[], [], [], [], [], [], [], [], []];
                let serializedLabels = [];
                let actualLabels = [];
                let mnth = 0;
                for(let i = 0; i < data['data'].length; i++) {
                    serializedLabels.push( new Date( data['data'][i][0] ).toISOString().split('T')[0] );
                    if ( props.filtering === 'day' ) {
                            actualLabels.push( serializedLabels[i] );
                        } else if (props.filtering === 'month' ) {
                            if ( i % 30 === 0 ) {
                                actualLabels.push( serializedLabels[i].slice(0, -3) );
                                mnth++;
                            }
                        } else if ( props.filtering === 'year' ) {
                            if ( serializedLabels[i].slice(-5) === '12-31' ) {
                                actualLabels.push( serializedLabels[i].slice(0, -6) );
                            }
                        }
                }
                for(let i = 0; i < data['data'].length; i++) {
                    for(let  j = 0; j < data['data'][i].length; j++) {
                        if ( props.filtering === 'day' ) {
                            serializedData[j].push( data['data'][i][j] );
                        } else if (props.filtering === 'month' ) {
                            if ( i % 30 === 0 ) {
                                serializedData[j].push( data['data'][i][j] );
                                mnth++;
                            }
                        } else if ( props.filtering === 'year' ) {
                            if ( serializedLabels[i].slice(-5) === '12-31' ) {
                                serializedData[j].push( data['data'][i][j] );
                            }
                        }
                    }
                }
                const generalDataStructure = {
                        labels: actualLabels,
                        datasets: [
                            {
                                label: 'All pages',
                                backgroundColor: '#191919',
                                data: Array<number>(),
                                spanGaps: true
                            }
                        ]
                };
                const unProofreadPagesData = serializedData[1].map((val, idx) => val - (
                    serializedData[2][idx] + serializedData[3][idx] + serializedData[3][idx] + serializedData[4][idx] + serializedData[5][idx]
                ));
                generalDataStructure.datasets[0].label = 'All pages without text'
                generalDataStructure.datasets[0].data = serializedData[2];
                chartWithoutText.value = clone( generalDataStructure );
                generalDataStructure.datasets[0].label = 'All pages tagged problematic'
                generalDataStructure.datasets[0].data = serializedData[3];
                chartProblematic.value = clone( generalDataStructure );
                generalDataStructure.datasets[0].label = 'All pages that have not been proofread'
                generalDataStructure.datasets[0].data = unProofreadPagesData;
                chartUnproofread.value = clone( generalDataStructure );
                generalDataStructure.datasets[0].label = 'All proofread pages'
                generalDataStructure.datasets[0].data = serializedData[4];
                chartProofread.value = clone( generalDataStructure );
                generalDataStructure.datasets[0].label = 'All validated pages'
                generalDataStructure.datasets[0].data = serializedData[5];
                chartValidated.value = clone( generalDataStructure );
                generalDataStructure.datasets[0].label = 'All transcluded pages'
                generalDataStructure.datasets[0].data = serializedData[6];
                chartTrans.value = clone( generalDataStructure );
                const nakedTexts = serializedData[7].map((val, idx) => val - serializedData[6][idx] - serializedData[8][idx])
                chartText.value = {
                    labels: actualLabels,
                    datasets: [
                        {
                            label: 'Naked texts',
                            backgroundColor: '#d73333',
                            borderColor: '#d73333',
                            data: nakedTexts,
                            spanGaps: true,
                            fill: 'start'
                        },
                        {
                            label: 'All texts',
                            backgroundColor: '#447ff5',
                            borderColor: '#447ff5',
                            data: serializedData[7],
                            spanGaps: true,
                            fill: 'start'
                        }

                    ]
                };
                generalDataStructure.datasets[0].label = 'Disambiguation pages'
                generalDataStructure.datasets[0].data = serializedData[8];
                chartDab.value = generalDataStructure;
                chartAll.value = {
                        labels: actualLabels,
                        datasets: [
                            {
                                label: 'Pages without text',
                                backgroundColor: '#ddd',
                                borderColor: '#ddd',
                                data: serializedData[2],
                                spanGaps: true,
                                fill: 'start'
                            },
                            {
                                label: 'Problematic pages',
                                backgroundColor: '#b0b0ff',
                                borderColor: '#b0b0ff',
                                data: serializedData[3].map((val, idx) => val + serializedData[2][idx]),
                                spanGaps: true,
                                fill: 'start'
                            },
                            {
                                label: 'Unproofread pages',
                                backgroundColor: '#ffa0a0',
                                borderColor: '#ffa0a0',
                                data: unProofreadPagesData.map((val, idx) => val + serializedData[3][idx] + serializedData[2][idx]),
                                spanGaps: true,
                                fill: 'start'
                            },
                            {
                                label: 'Proofread pages',
                                backgroundColor: '#ffe867',
                                borderColor: '#ffe867',
                                data: serializedData[4].map((val, idx) => val + serializedData[3][idx] + serializedData[2][idx] + unProofreadPagesData[idx]),
                                spanGaps: true,
                                fill: 'start'
                            },
                            {
                                label: 'Validated pages',
                                backgroundColor: '#90ff90',
                                borderColor: '#90ff90',
                                data: serializedData[5].map((val, idx) => val + serializedData[3][idx] + serializedData[2][idx] + serializedData[4][idx] + unProofreadPagesData[idx]),
                                spanGaps: true,
                                fill: 'start'
                            }
                        ]
                };
                
                loaded.value = true;
            }
        )

        return {
            totalAll,
            totalTrans,
            totalUnproofread,
            totalProblematic,
            totalProofread,
            totalValidated,
            totalWithoutText,
            totalTexts,
            totalDab,
            percentagePr,
            changeAll,
            changeProblematic,
            changeUnproofread,
            changeProofread,
            changeValidated,
            changeTrans,
            changeWithoutText,
            changeTexts,
            chartAll,
            chartTrans,
            chartWithoutText,
            chartValidated,
            chartProofread,
            chartUnproofread,
            chartProblematic,
            chartText,
            chartDab,
            loaded,
            changeDab
        }
    },
})
</script>

<style lang="less">
@import '@wikimedia/codex-design-tokens/theme-wikimedia-ui.less';

.initial-stats-container {
    padding-top: @spacing-75;
    width: 75%;
    margin: auto;
    display: grid;
    grid-template-rows: auto auto;
    box-sizing: border-box;
}
.pr-percentage-wrapper {
    padding: @spacing-50;
    padding-left: 0;
}

.pr-percentage-bar {
    height: 1em;
    width: 100%;
    border-radius: @border-radius-pill;
    border: @border-base;
    box-sizing: border-box;
}
.pr-percentage-bar-inner {
    height: 0.95em;
    background: @color-progressive;
    border-radius: @border-radius-pill;
}
.cdx-card {
    margin: @spacing-75;
}
.cdx-card .cdx-card__text{
    width: 100%;
}
.up .cdx-icon,
.up .change-num {
    color: @color-success;
}
.down .cdx-icon,
.down .change-num {
    color: @color-destructive;
}

.pause .cdx-icon,
.pause .change-num {
    color: @color-warning;
}
</style>
