<template>
  <div class="container">
    <template v-if="menuItems.length > 0">
      <cdx-field>
        <cdx-select 
        :menu-items="menuItems"
        v-model:selected="selectedLang"
        @update:selected="onSelect"
        default-label="Choose a language">
        </cdx-select>
        <template #label>
          Select a language
        </template>
      </cdx-field>
      <cdx-field>
        <cdx-toggle-button-group :buttons="buttonGroup" v-model:model-value="selectedTime"></cdx-toggle-button-group>
        <template #label>
          Time period
        </template>
      </cdx-field>
      <template v-if="selectedTime === 'custom'">
        <cdx-field>
        <cdx-text-input
        input-type="date"
        ></cdx-text-input>
        <template #label>
          Start date
        </template>
      </cdx-field>
      <cdx-field>
        <cdx-text-input
        input-type="date"
        ></cdx-text-input>
        <template #label>
          End date
        </template>
      </cdx-field>
      </template>
      <br>
      <cdx-button action="progressive" weight="primary" @click="onClick">Show statistics</cdx-button>
    </template>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import { CdxTextInput, CdxSelect, CdxField, type MenuItemData, CdxToggleButtonGroup, CdxButton } from '@wikimedia/codex';
import clone from '../components/util';

export default defineComponent({
  name: 'HomeView',
  components: { CdxSelect, CdxTextInput, CdxField, CdxToggleButtonGroup, CdxButton },
  setup() {
    const menuItems = ref<MenuItemData[]>([]);
    let defaultButtons = [
      {
        label: 'Yesterday',
        value: 'yesterday',
        disabled: false,
      },
      {
        label: 'Last 7 days',
        value: 'lastweek',
        disabled: false,
      },
      {
        label: 'Last 30 days',
        value: 'lastmonth',
        disabled: false,
      },
      {
        label: 'Last 365 days',
        value: 'lastyear',
        disabled: false,
      },
      {
        label: 'All time',
        value: 'alltime',
        disabled: false,
      }
    ];
    const buttonGroup = ref(defaultButtons);
    const selectedLang = ref<string|number|null>(null);
    const selectedTime = ref<string|number|null>('yesterday');
    fetch( '/api/all_langs' )
      .then( ( resp ) => resp.json() )
      .then( ( val ) => {
        const menuList: any[] = [];
        for ( let i = 0; i < val.length; i++ ) {
          menuList.push( {
            value: val[i],
            label: val[i]
          } );
        }
        menuItems.value = menuList;
      } )

      function onSelect(val: string) {
        if ( val === 'all' ) {
          const disabledYesterday = clone( defaultButtons );
          disabledYesterday[0].disabled = true;
          if ( selectedTime.value === 'yesterday' ) {
            selectedTime.value = 'lastweek';
          }
          buttonGroup.value = disabledYesterday;
        } else {
          buttonGroup.value = defaultButtons;
        }
      }

      function onClick() {
        window.location.href = `stats/${ selectedLang.value }/${ selectedTime.value }`
      }

      return {
        selectedTime,
        buttonGroup,
        menuItems,
        onSelect,
        menuConfig: {
          visibleItemLimit: 6
        },
        onClick,
        selectedLang
      }
  },
})
</script>

<style lang="less" scoped>
@import '@wikimedia/codex-design-tokens/theme-wikimedia-ui.less';
.container {
  width: 75%;
  margin: auto;
  padding: @spacing-125;
  background: @color-inverted;
  height: @size-full;
}
</style>


