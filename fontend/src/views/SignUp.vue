<template>
  <div class="login">
    <div class="login_content">
      <div class="login_title">SIGNUP</div>
      <form action="" @submit="checkForm" class="login_form">
        <input-component
          img="./src/assets/icons8-mail-30.png"
          placeholder="Email"
        />
        <input-component
          img="./src/assets/icons8-user-50.png"
          placeholder="Username"
        />
        <input-component
          img="./src/assets/icons8-lock-30.png"
          placeholder="Password"
        />
        <input-component
          img="./src/assets/icons8-lock-30.png"
          placeholder="Password"
        />
        <div class="login_btn">
          <button>SIGNUP</button>
        </div>
        <div class="login_create">
          <router-link to="/login">
            <span>login</span>
            <div></div>
          </router-link>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import InputComponent from "./../components/InputComponent.vue";
export default {
  components: { InputComponent },
  data: () => ({
    errors_username: "",
    errors_password: "",
  }),
  methods: {
    checkForm(e) {
      if (!this.errors_username) {
        this.errors_username = "Name required.";
      }
      e.preventDefault();
    },
  },
};
</script>

<style lang="scss" scoped>
.login {
  background-image: url("./../assets/black-and-white-architecture-white-building-skyscraper-pattern-1115046-pxhere.com.jpg");
  width: 100vw;
  height: 100vh;
  background-position: center;
  background-size: cover;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  z-index: 1;
}
.login::before {
  content: "";
  display: block;
  position: absolute;
  z-index: -1;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.65);
}
.login_title {
  line-height: 1.2;
  font-size: 30px;
  font-family: Ubuntu-Bold;
  color: #403866;
  padding-bottom: 40px;
  font-weight: bold;
}
.login_content {
  background-color: #fff;
  padding: 40px;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 500px;
  border-radius: 3px;
}
.login_form {
  width: 100%;
  > div {
    border-radius: 3px;
    margin-bottom: 16px;
  }
}
.label_checkbox {
  color: #999;
  line-height: 1.2;
  font-size: 16px;
  font-family: Ubuntu-Regular;
}
.login_btn {
  display: flex;
  justify-content: center;
  background-color: #827ffe;
  border-radius: 3px;
  &:hover {
    background-color: #2c2a74;
  }
  button {
    border: none;
    background: 0 0;
    font-size: 16px;
    line-height: 1.2;
    height: 62px;
    color: #fff;
    font-family: Ubuntu-Bold;
    font-weight: bold;
    width: 100%;
  }
}
img {
  width: 30px;
  height: 30px;
  margin: 0 10px;
}
.focus_input {
  position: absolute;
  border: 1px solid #827ffe;
  left: -1px;
  top: -1px;
  visibility: hidden;
  width: calc(100% + 2px);
  height: calc(100% + 2px);
  pointer-events: none;
  border-radius: 3px;
  transform: scaleX(1.05) scaleY(1.1);
  transition: all 0.15s;
}
.errors {
  color: red;
  position: absolute;
  right: 0;
}
.login_create {
  display: flex;
  justify-content: end;
  div {
    background: url("./../assets/icons8-right-arrow-30.png") no-repeat;
    width: 40px;
    height: 25px;
    background-size: 25px 25px;
    background-position: center;
  }
  a {
    text-decoration: none;
    display: flex;
    align-items: center;
    color: #827ffe;
    &:hover {
      color: #212529;
      div {
        background: url("./../assets/icons8-right-arrow-30_black.png") no-repeat;
        background-position: center;
        background-size: 25px 25px;
      }
    }
  }
}
</style>
