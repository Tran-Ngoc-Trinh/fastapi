<template>
  <div class="login">
    <div class="login_content">
      <div class="login_title">LOGIN</div>
      <form action="" @submit="checkForm" class="login_form">
        <div>
          <img src="./../assets/icons8-user-50.png" alt="" />
          <input type="text" placeholder="Username" v-model="username" required pattern="[a-z]{4,8}" size="45"/>
          <span class="focus_input"></span>
          <span class="errors">{{ errors_username }}</span>
        </div>
        <div>
          <img src="./../assets/icons8-lock-30.png" alt="" />
          <input
            type="password"
            placeholder="Password"
            v-model="password"
            id="password"
          />
          <span class="focus_input"></span>
          <img
            src="./../assets/icon_eye_input_off.png"
            alt=""
            @click="showPassWord"
            id="eye"
          />
          <span class="errors">{{ errors_password }}</span>
        </div>
        <div>
          <input type="checkbox" id="login_checkbox" />
          <label for="login_checkbox" class="label_checkbox"
            >&nbsp;Remember me</label
          >
        </div>
        <div class="login_btn">
          <button>LOGIN</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data: () => ({
    username: "",
    password: "",
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
    showPassWord() {
      var input_password = document.getElementById("password");
      var eye = document.getElementById("eye");
      if (input_password.type === "password") {
        input_password.type = "text";
        eye.src = "./src/assets/icon_eye_input_black.png";
      } else {
        input_password.type = "password";
        eye.src = "./src/assets/icon_eye_input_off.png";
      }
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
  > div:nth-child(1),
  > div:nth-child(2) {
    position: relative;
    background-color: #e6e6e6;
    display: flex;
    align-items: center;
  }
  > div {
    border-radius: 3px;
    margin-bottom: 16px;
  }
}
input {
  border: none;
  outline: none;
  background: 0 0;
  font-weight: bold;
}
input[type="text"],
input[type="password"] {
  font-family: Ubuntu-Bold;
  height: 62px;
  padding: 0 20px 0 0;
  width: 100%;
}
input[type="text"]:focus + .focus_input,
input[type="password"]:focus + .focus_input {
  visibility: inherit;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  transform: scaleX(1) scaleY(1);
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
</style>
