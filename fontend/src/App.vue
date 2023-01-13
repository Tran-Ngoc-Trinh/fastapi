<script setup>
import Header from "./components/Header.vue";
import SideBar from "./components/SideBar.vue";
</script>

<template>
  <div class="wrapper">
    <div class="sidebar" v-if="$route.name!='login' & $route.name!='signup'">
      <SideBar />
    </div>
    <div class="content">
      <!-- <header v-if="$route.name!='login' & $route.name!='signup'">
        <Header />
      </header> -->
      <router-view />
    </div>
  </div>
</template>

<style scoped lang="scss">
.wrapper {
  // height: 100vh;
  display: flex;
  // width: 100vw;
  .sidebar {
    width: 200px;
  }
  .content {
    width: 100%;
  }
}
</style>
