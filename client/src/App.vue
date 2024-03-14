<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import HeaderComponent from './components/HeaderComponent.vue'
</script>

<template>
  <header>
    <HeaderComponent />
  </header>

    <div class="wrapper">
      <RouterView />
    </div>

</template>

<style lang="less" scoped>
@import '@wikimedia/codex-design-tokens/theme-wikimedia-ui.less';

.wrapper {
  background: @background-color-interactive;
  min-height: 100vh;
}
</style>
