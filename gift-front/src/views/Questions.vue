<template>
  <div class="page">
    <div>
      <h1 class="questions">测试</h1>
      <input id="answer" class="answer_input" type="text" value="测试" />
    </div>
  </div>
</template>

<script>
export default {
};
</script>

<style scoped>
* {
  box-sizing: border-box;
}

.page {
  display: grid;
  position: absolute;
  background-color: #e2e2e5;
  height: calc(100% - 40px);
  width: calc(100% - 40px);
  text-align: center;
  place-items: center;
}
.answer_input {
  width: 150px;
  text-align: center;
  border-bottom-style: solid;
  border-top-style: solid;;
  border-left-style: none;
  border-right-style: none;
  border-width: 5px;
  border-color: #999;
  height: 50px;
  color: #999;
  background-color: rgba(0, 0, 0, 0);
  font-weight: 700;
  font-size: 40px;
}
.questions {
  position: relative;
  font-size: 40px;
  margin-bottom: -50px;
  
}
</style>