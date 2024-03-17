<template>
    <main class="navbar">
        <div class="centered-text">The last statistics crawl occured on {{ data }}.</div>
    </main>
</template>
<script lang="ts">
import { ref, defineComponent } from 'vue'

export default defineComponent({
    setup() {
        const loaded = ref(false);
        const data = ref('');
        fetch('/api/lastcrawl')
        .then( ( res ) => res.json() )
        .then( ( d ) => data.value = d[0]);
        return {
            loaded,
            data
        }
    },
})
</script>

<style lang="less" scoped>
@import '@wikimedia/codex-design-tokens/theme-wikimedia-ui.less';
.navbar {
    background: @background-color-interactive;
    font-family: @font-family-monospace;
    padding: @size-50;
    font-size: @size-75;
    display: flex;
    justify-content: center;
}

</style>