<template>
  <div class="main">
    <img src="./../assets/icons8-redux-100.png" alt="" />
    <div class="menu">
        <router-link to="/" >
        <div>
          <img src="./../assets/icons8-home-page-64.png" alt="" />
          <span>Home</span>
        </div>
          
        </router-link>
        <router-link to="/" >
      <div>
        <img src="./../assets/icons8-folder-50.png" alt="" />
        <span>Folder</span>
      </div>
      </router-link>
      <router-link to="/" >
      <div>
        <img src="./../assets/icons8-user-50.png" alt="" />
        <span>User</span>
      </div>
      </router-link>
    </div>
    <div class="silebar_footer">T.N.T</div>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.main {
  position: relative;
  height: 100%;
  background-color: #1b1737;
  display: flex;
  flex-direction: column;
  align-items: center;
  > img {
    margin: 1.2rem 0;
  }
}
.menu {
  a {
    text-decoration: none;
  }
  a > div {
    display: flex;
    align-items: center;
    padding: 0 25px;
    img {
      width: 25px;
      height: 25px;
    }
    span {
      color: #c0c0c0;
      margin: 0 10px;
      line-height: 3;
    }
  }
  a > div:hover {
    background-color: #49475f;
    border-radius: 5px;
    span {
        color: white;
    }
    img {
        filter: opacity(0.5) drop-shadow(0 0 0 blue);
    }
  }
}
.silebar_footer {
  color: #c0c0c0;
  position: absolute;
  bottom: 20px;
}
</style>
