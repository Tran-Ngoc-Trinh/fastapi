<script setup>
import Header from "./components/Header.vue";
import SideBar from "./components/SideBar.vue";
</script>

<template>
  <div class="wrapper">
    <div class="sidebar">
      <SideBar />
    </div>
    <div class="content">
      <header>
        <Header />
      </header>
    </div>
  </div>
</template>

<style scoped lang="scss">
.wrapper {
  min-height: 100vh;
  min-width: 100vw;
  display: flex;
  .sidebar {
    width: 200px;
  }
  .content {
    width: 100%;
  }
}
</style>
