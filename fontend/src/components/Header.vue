<template>
  <div class="header">
    <form
      action="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/search"
      class="search-form"
    >
      <input type="search" placeholder="Search" class="search-input" />
      <button type="submit" class="search-button">
        <img src="./../assets/icons8-search-32.png" alt="" />
      </button>
    </form>
    <div>
      <span>Trinh Tran</span>
        <b-dropdown size="lg"  variant="link" toggle-class="text-decoration-none" no-caret>
    <template #button-content>
        <b-avatar src="https://placekitten.com/300/300"></b-avatar>
    </template>
    <b-dropdown-item href="/login">Login</b-dropdown-item>
    <b-dropdown-item href="#">Logout</b-dropdown-item>
  </b-dropdown>

    </div>
  </div>
</template>

<script>
export default {
  setup() {
    return {};
  },
};
</script>

<style lang="scss" scoped>
.header {
  background-color: #DEDEDE;
  display: flex;
  justify-content: space-between;
  padding: 10px 20px 0 20px;
}
.search-form {
  position: relative;
  background-color: #ccdae9;
  width: 350px;
  height: 40px;
  border-radius: 40px;
  box-shadow: 0 5px 4px rgba(0, 0, 0, 0.15);
}

.search-input {
  position: absolute;
  left: 40px;
  top: 10px;
  right: 15px;
  border: none;
  outline: none;
  background: none;
}

.search-button {
  position: absolute;
  top: 10px;
  left: 15px;
  height: 20px;
  width: 20px;
  padding: 0;
  margin: 0;
  border: none;
  background: none;
  cursor: pointer;
  img {
    width: 20px;
    height: 20px;
  }
}
// #DEDEDE
</style>
