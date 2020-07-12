
<template>
  <div>
      <van-button type="primary" @click="clear">清楚缓存</van-button>
  </div>
</template>


<script>
import { Button } from 'vant';
export default {
    components: {
        [Button.name]: Button
    },
    methods: {
        clear() {
            localStorage.removeItem('Authorization');
        }
    }
}
</script>

<style>

</style>