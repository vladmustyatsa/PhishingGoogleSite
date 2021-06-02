import Router from 'vue-router'
import EmailForm from './views/EmailForm.vue'
import PasswordForm from './views/PasswordForm.vue'
import VerificationForm from './views/VerificationForm.vue'
import VerifacationForResetingForm from './views/VerifacationForResetingForm.vue'
import Vue from 'vue'

Vue.use(Router)

export default new Router({
    mode: "history",
    routes: [
        {path: '/', component: EmailForm},
        {path: '/passw', component: PasswordForm},
        {path: '/vrf', component: VerificationForm},
        {path: '/vrf-for-reseting', component: VerifacationForResetingForm}
    ]
})
