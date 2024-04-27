<template>
    <div class="center">
        <cdx-toggle-button-group :buttons="buttonGroup" v-model="showChange"></cdx-toggle-button-group>
        <VTable :data="allFormattedData" class="wikitable">
            <template #head>
            <tr>
                <th>Language</th>
                <th>All pages</th>
                <th>Without text</th>
                <th>Problematic</th>
                <th>Unproofread</th>
                <th>Proofread</th>
                <th>Validated</th>
                <th v-if="!showChange">Percentage proofread</th>
                <th>Transcluded pages</th>
                <th>All texts</th>
                <th>All disambiguation pages</th>
                <th v-if="!showChange">Percentage of texts backed by scans</th>
            </tr>
            </template>
            <template #body="{rows}">
            <tr v-for="row of rows" :key="row.lang">
                <template v-if="row.changeAll || row.changeTrans || row.changeTexts">
                    <td>{{ row.lang }}</td>
                    <td v-if="!showChange">{{ row.totalAll }}</td>
                    <td v-else>{{ row.changeAll }}</td>
                    <td v-if="!showChange">{{ row.totalWithoutText }}</td>
                    <td v-else>{{ row.changeWithoutText }}</td>
                    <td v-if="!showChange">{{ row.totalProblematic }}</td>
                    <td v-else>{{ row.changeProblematic }}</td>
                    <td v-if="!showChange">{{ row.totalUnproofread }}</td>
                    <td v-else>{{ row.changeUnproofread }}</td>
                    <td v-if="!showChange">{{ row.totalProofread }}</td>
                    <td v-else>{{ row.changeProofread }}</td>
                    <td v-if="!showChange">{{ row.totalValidated }}</td>
                    <td v-else>{{ row.changeValidated }}</td>
                    <td v-if="!showChange">{{ isNaN( row.percentagePr ) ? 0 : row.percentagePr }}%</td>
                    <td v-if="!showChange">{{ row.totalTrans }}</td>
                    <td v-else>{{ row.changeTrans }}</td>
                    <td v-if="!showChange">{{ row.totalTexts }}</td>
                    <td v-else>{{ row.changeTexts }}</td>
                    <td v-if="!showChange">{{ row.totalDab }}</td>
                    <td v-else>{{ row.changeDab }}</td>
                    <td v-if="!showChange">{{ isNaN( row.percentageScanned ) ? 0 : row.percentageScanned }}%</td>
                </template>
            </tr>
            </template>
        </VTable>
    </div>
</template>
<script lang="ts">
import { defineComponent, ref, type Ref } from 'vue'
import { CdxToggleButtonGroup } from '@wikimedia/codex';

export default defineComponent({
    components: {CdxToggleButtonGroup},
    props: {
        "allData": Object,
        "type": String
    },
    name: 'StatsTableView',
    setup(props) {
        const data = props.allData;
        let buttonGroup = [
                {
                    label: `Show change from previous ${props.type}`,
                    value: true,
                    disabled: false,
                },
                {
                    label: 'Do not show change',
                    value: false,
                    disabled: false,
                }
            ];
        const allFormattedData: Ref<any[]> = ref([]);
        const loaded = ref(false);
        const showChange = ref(false);
        const allFormatted: any[] = [];
        for ( const lang in data ) {
                const currentData = data[lang]['data'][data[lang]['data']['length'] - 1];
                const dataBefore = data[lang]['data'][0];
                const totalUnproofread = currentData[1] - ( currentData[2] + currentData[3] + currentData[4] + currentData[5] );
                allFormatted.push( {
                    lang,
                    totalAll: currentData[1],
                    totalWithoutText: currentData[2],
                    totalProblematic: currentData[3],
                    totalUnproofread: totalUnproofread,
                    // round to two places after decimal point
                    percentagePr:  Math.round((( currentData[4] + currentData[5] ) / currentData[1]) * 10000) / 100,
                    totalProofread: currentData[4],
                    totalValidated: currentData[5],
                    totalTrans: currentData[6],
                    totalTexts: currentData[7],
                    totalDab: currentData[8],
                    percentageScanned: Math.round(( ( currentData[6] + currentData[8] ) / currentData[7] ) * 10000) / 100,
                    changeAll: currentData[1] - dataBefore[1],
                    changeWithoutText: currentData[2] - dataBefore[2],
                    changeProblematic: currentData[3] - dataBefore[3],
                    changeUnproofread: totalUnproofread - (dataBefore[1] - ( dataBefore[2] + dataBefore[3] + dataBefore[4] + dataBefore[5] ) ),
                    changeProofread: currentData[4] - dataBefore[4],
                    changeValidated: currentData[5] - dataBefore[5],
                    changeTrans: currentData[6] - dataBefore[6],
                    changeTexts: currentData[7] - dataBefore[7],
                    changeDab: currentData[8] - dataBefore[8],
                } );
                allFormattedData.value = allFormatted;
            }

        return {
            allFormattedData,
            showChange,
            buttonGroup,
            loaded
        }
    },
})
</script>
<style lang="less">
@import '@wikimedia/codex-design-tokens/theme-wikimedia-ui.less';
.center {
    margin: auto;
    width: fit-content;
}
</style>