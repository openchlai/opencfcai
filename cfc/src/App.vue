<script>
import { RouterLink, RouterView } from 'vue-router'
import LayoutFile from './components/LayoutFile.vue';

export default {
  name: 'App',
  components: {
    LayoutFile,
  },
  setup() {
    return {}
  }
}
</script>

<template>
  
  <LayoutFile />
</template>

<style scoped>

</style>
