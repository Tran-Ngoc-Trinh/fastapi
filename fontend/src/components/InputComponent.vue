<template>
  <div class="input">
    <img :src="img" alt="" />
    <input
      :type="type"
      :placeholder="placeholder"
      v-model="password"
      :id="placeholder == 'Password' ? 'password' : ''"
    />
    <span class="focus_input"></span>
    <img
      v-if="placeholder === 'Password'"
      src="./../assets/icon_eye_input_off.png"
      alt=""
      @click="showPassWord"
      id="eye"
    />
    <span class="errors">{{ errors_password }}</span>
  </div>
</template>

<script>
export default {
  data() {
    return {
        username: "",
    password: "",
    };
  },
  props: {
    img: String,
    type: String,
    placeholder: String,
  },
  methods: {
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
.input {
  position: relative;
  background-color: #e6e6e6;
  display: flex;
  align-items: center;
  border-radius: 3px;
  margin-bottom: 16px;
  font-family: Ubuntu-Bold;
  height: 62px;
  width: 100%;
}
input {
  border: none;
  outline: none;
  background: 0 0;
  font-weight: bold;
  width: 100%;
  height: 100%;
}
input:focus + .focus_input {
  visibility: inherit;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  transform: scaleX(1) scaleY(1);
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
