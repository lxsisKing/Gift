
<template>
  <div>
      <van-button loading type="primary" loading-type="spinner"/>
  </div>
</template>


<script>
import { Button } from 'vant';
export default {
    components: {
        [Button.name]: Button
    }
}
</script>

<style>

</style>