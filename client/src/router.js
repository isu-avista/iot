/* eslint-disable */
import Vue from 'vue';
import Router from 'vue-router';
import Monitor from '@/views/Monitor.vue';
import Config from '@/views/Config.vue';
import Login from '@/views/Login.vue';
import About from '@/views/About.vue';
import Profile from '@/views/Profile';
import isValidJwt from '@/utils';

Vue.use(Router);

export const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Monitor,
    },
    {
      path: '/monitor',
      name: 'Monitor',
      component: Monitor,
    },
    {
      path: '/about',
      name: 'About',
      component: About,
    },
    {
      path: '/config',
      name: 'Config',
      component: Config,
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
    },
    {
      path: '/profile',
      name: 'Profile',
      component: Profile,
    },
  ],
});

router.beforeEach((to, from, next) => {
  const publicPages = ['/login', '/about'];
  const adminPages = ['/config']
  const authRequired = !publicPages.includes(to.path);
  const loggedIn = localStorage.getItem('user');

  // trying to access a restricted page + not logged in
  // redirect to login page
  if (authRequired && !loggedIn) {
    next('/login');
  } else {
    const user = JSON.parse(localStorage.getItem('user'));
    if (user && user.token && !isValidJwt(user.token)) {
      next('/login')
    } else {
      if (adminPages.includes(to.path) && user.role === "ADMIN") {
        next();
      } else if (adminPages.includes(to.path) && user.role !== "ADMIN") {
        next(from);
      } else {
        next();
      }
    }
  }
});
