import Router from 'vue-router'
import EmailForm from './views/EmailForm.vue'
import Test from './views/Test.vue'

import Vue from 'vue'

Vue.use(Router)

const router = new Router({
    mode: "history",
    routes: [
        {path: '/', component: EmailForm},
        {path: '/asd', component: Test}
    ]
})



export default router;
