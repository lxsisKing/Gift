import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import axios from 'axios';

// 允许跨域时携带cookie
axios.defaults.withCredentials = true;
// 阻止启动生产消息
Vue.config.productionTip = false;
Vue.prototype.$axios = axios;

new Vue({
  store,
  router,
  render: h => h(App),
}).$mount('#app')
