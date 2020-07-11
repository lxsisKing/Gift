<template>
  <div>
    <h1>about</h1>
    <p>{{aboutMsg}}</p>
    <div>
        <layout />
    </div>
  </div>
</template>
<script>
import Layout from "../components/Layout.vue";
export default {
  components: {
    Layout
  },
  data() {
    return {
      aboutMsg: "我是about组件"
    };
  }
};
</script>