<template>
  <div>
    <!-- <h1>home</h1>
    <p>{{msg}}</p>
    <router-link to="/about">About</router-link> -->
    <nice-login />
  </div>
</template>
<script>
import NiceLogin from "../components/NiceLogin.vue";
export default {
  components: {
    NiceLogin
  },
  data() {
    return {
      msg: "我是home 组件"
    };
  }
};
</script>