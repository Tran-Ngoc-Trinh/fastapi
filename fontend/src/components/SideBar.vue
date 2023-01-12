<template>
  <div class="main">
    <div class="main_avt">
      <b-avatar src="https://placekitten.com/300/300"></b-avatar>
      <span class="title">Trinh Tran</span>
    </div>
    <div class="main_menu">
      <router-link to="/">
        <div tabIndex="1" :style="$route.name == 'home' ? cssFocusBg : ''">
          <img src="./../assets/icons8-person-30.png" alt="" />
          <span>Profile</span>
          <div
            class="boder"
            :style="$route.name == 'home' ? cssFocusBoder : ''"
          ></div>
        </div>
      </router-link>
      <router-link to="/">
        <div tabIndex="2" :style="$route.name == '' ? cssFocusBg : ''">
          <img src="./../assets/icons8-power-bi-30.png" alt="" />
          <span>Boards</span>
          <div
            class="boder"
            :style="$route.name == '' ? cssFocusBoder : ''"
          ></div>
        </div>
      </router-link>
      <router-link to="/board">
        <div tabIndex="3" :style="$route.name == 'board' ? cssFocusBg : ''">
          <img src="./../assets/icons8-calendar-30.png" alt="" />
          <span>Boards</span>
          <div
            class="boder"
            :style="$route.name == 'board' ? cssFocusBoder : ''"
          ></div>
        </div>
      </router-link>
      <router-link to="/setting" :style="$route.name == '' ? cssFocusBg : ''">
        <div tabIndex="4">
          <img src="./../assets/icons8-settings-30.png" alt="" />
          <span>Setting</span>
          <div
            class="boder"
            :style="$route.name == '' ? cssFocusBoder : ''"
          ></div>
        </div>
      </router-link>
      <router-link to="/login" class="logout">
        <div tabIndex="5">
          <img src="./../assets/icons8-logout-rounded-30.png" alt="" />
          <span>Logout</span>
          <div class="boder"></div>
        </div>
      </router-link>
    </div>
    <div class="silebar_footer">T.N.T</div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      cssFocusBg: {
        backgroundColor: "white",
      },
      cssFocusBoder: {
        visibility: "inherit",
      },
    };
  },
  methods: {},
};
</script>

<style lang="scss" scoped>
.main {
  position: relative;
  height: 100%;
  background-color: var(--bg-sildebar);
}
.main_avt {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1.2rem 0;
  span {
    font-family: Ubuntu-Regular;
    font-weight: bold;
  }
}

.main_menu {
  padding: 0 10px;
  a {
    text-decoration: none;
    border-radius: 5px;
    > div {
      margin-bottom: 5px;
      background-color: var(--color-menu-sidebar);
      display: flex;
      align-items: center;
      border-radius: 5px;
      position: relative;
      &:hover {
        background-color: var(--bg-sildebar);
        .boder {
          visibility: inherit;
        }
      }
      // &:focus {
      //   background-color: var(--bg-sildebar);
      //   .boder {
      //     visibility: inherit;
      //   }
      // }
      img {
        width: 25px;
        height: 25px;
        margin: 0 10px;
        user-select: none;
      }
      span {
        color: var(--color-text-sidebar);
        line-height: 3;
        user-select: none;
        font-family: Ubuntu-Regular;
      }
      .boder {
        position: absolute;
        pointer-events: none;
        visibility: hidden;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        border-radius: 5px;
        border: 1px solid var(--color-text-sidebar);
      }
    }
  }
  .logout div {
    span {
      color: #f50e02;
    }
    &:hover {
      background-color: var(--bg-sildebar);
      .boder {
        visibility: inherit;
        border: 1px solid #f50e02;
      }
    }
    &:focus {
      background-color: var(--bg-sildebar);
      .boder {
        visibility: inherit;
        border: 1px solid #f50e02;
      }
    }
  }
}
.silebar_footer {
  color: #c0c0c0;
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
}
</style>
