import Vue from "vue";
import VueRouter from "vue-router"
import Login from "../views/Login.vue"
import About from "../views/About.vue"
import Home from "../views/Home.vue"
import Questions from "../views/Questions.vue"
import Letter from "../views/Letter.vue"
import Voice from "../views/Voice.vue"

Vue.use(VueRouter);


const routes = [
    {
        path: '/login',
        name: 'login',
        component: Login
    },
    {
        path: '/about',
        name: 'about',
        component: About
    },
    {
        path: '/home',
        name: 'home',
        component: Home
    },
    {
        path: '/questions',
        name: 'questions',
        component: Questions
    },
    {
        path: '/letter',
        name: 'letter',
        component: Letter
    },
    {
        path: '/voice',
        name: 'voice',
        component: Voice,
    },
];

const router = new VueRouter({
    mode: "history",
    routes
});

router.beforeEach((to, from, next) => {
    // ${//to and from are Route Object,next() must be called to resolve the hook}
    if (to.path === '/login'){
        let token = localStorage.getItem('Authorization');
        if (token === null || token === '') {
            next()
        } else {
            next({path: '/home'})
        }
    } else {
        let token = localStorage.getItem('Authorization');
        if (token === null || token === '') {
            next({path: '/login'});
        } else {
            next();
        }
    }
})

export default router;

