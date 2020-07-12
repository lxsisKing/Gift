import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        serviceUrl: 'http://127.0.0.1:8000',
        Authorization: localStorage.getItem('Authorization') ? localStorage.getItem('Authorization') : '',
    },
    mutations: {
        // 修改token值，并将token存入localStorage
        changeLogin(state, token) {
            state.Authorization = token;
            localStorage.setItem('Authorization', token);
        }
    },
    getters: {

    },
    actions: {

    },
    modules: {

    },
});