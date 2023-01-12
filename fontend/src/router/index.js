import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
// localStorage
const ifAuthenticated = (to, from, next) => {
  console.log(to, from)
  if (true) {
    next();
  }
  next({ name: "login" });
};

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
      beforeEnter: ifAuthenticated,
    },
    {
      path: "/login",
      name: "login",
      component: () => import("../views/Login.vue"),
    },
    {
      path: "/signup",
      name: "signup",
      component: () => import("../views/SignUp.vue"),
    },
    {
      path: "/board",
      name: "board",
      component: () => import("../views/Board.vue"),
    },
    {
      path: "/setting",
      name: "setting",
      component: () => import("../views/Test.vue"),
    },
  ],
});

export default router;
