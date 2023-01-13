<template>
  <div class="board">
    <div class="board_header">
      <span>Board</span>
      <div>
        <div class="board_header_search">
          <form
            action="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/search"
            class="search-form"
          >
            <input type="search" placeholder="Search" class="search-input" />
            <button type="submit" class="search-button">
              <img src="./../assets/icons8-search-32.png" alt="" />
            </button>
          </form>
        </div>
        <div class="board_addtask">
          <img src="./../assets/icons8-plus-math-24.png" alt="" />
          <span>&nbsp; Add task</span>
        </div>
      </div>
    </div>

    <div class="board_content">
      <div class="board_content_block color_todo">
        <div class="board_content_block_header">
          <div class="block_color color_text_todo"></div>
          <span>To do</span>
        </div>
        <div class="scroll">
          <draggable v-model="ToDo" transition="100" class="drop-zone">
            <template v-slot:item="{ item }">
              <div class="board_content_block_body">
                <div class="board_background"></div>
                <div class="board_content_title">
                  <h3>{{ item.title }}</h3>
                  <img :src="item.image" alt="" />
                </div>
                <span>{{ item.content }}</span>
                <div class="board_date">
                  <img src="./../assets/icons8-calendar-25.png" alt="" />
                  <span>{{ item.date }}</span>
                </div>
              </div>
            </template>
          </draggable>
        </div>
      </div>

      <div class="board_content_block color_doing">
        <div class="board_content_block_header">
          <div class="block_color color_text_doing"></div>
          <span>Doing</span>
        </div>
        <div class="scroll">
          <draggable v-model="Doing" transition="100" class="drop-zone">
            <template v-slot:item="{ item }">
              <div class="board_content_block_body">
                <div class="board_background"></div>
                <div class="board_content_title">
                  <h3>{{ item.title }}</h3>
                  <img :src="item.image" alt="" />
                </div>
                <span>{{ item.content }}</span>
                <div class="board_date">
                  <img src="./../assets/icons8-calendar-25.png" alt="" />
                  <span>{{ item.date }}</span>
                </div>
              </div>
            </template>
          </draggable>
        </div>
      </div>
      <div class="board_content_block color_done">
        <div class="board_content_block_header">
          <div class="block_color color_text_done"></div>
          <span>Done</span>
        </div>
        <div class="scroll">
          <draggable v-model="Done" transition="100" class="drop-zone">
            <template v-slot:item="{ item }">
              <div class="board_content_block_body">
                <div class="board_background"></div>
                <div class="board_content_title">
                  <h3>{{ item.title }}</h3>
                  <img :src="item.image" alt="" />
                </div>
                <span>{{ item.content }}</span>
                <div class="board_date">
                  <img src="./../assets/icons8-calendar-25.png" alt="" />
                  <span>{{ item.date }}</span>
                </div>
              </div>
            </template>
          </draggable>
        </div>
      </div>
      <div class="board_content_block color_trash">
        <div class="board_content_block_header">
          <div class="block_color color_text_trash"></div>
          <span>Trash</span>
        </div>
        <div class="scroll">
          <draggable v-model="Trash" transition="100" class="drop-zone">
            <template v-slot:item="{ item }">
              <div class="board_content_block_body">
                <div class="board_background"></div>
                <div class="board_content_title">
                  <h3>{{ item.title }}</h3>
                  <img :src="item.image" alt="" />
                </div>
                <span>{{ item.content }}</span>
                <div class="board_date">
                  <img src="./../assets/icons8-calendar-25.png" alt="" />
                  <span>{{ item.date }}</span>
                </div>
              </div>
            </template>
          </draggable>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Draggable from "vue3-draggable";
export default {
  data() {
    return {
      ToDo: [
        {
          image:
            "./../assets/icons8-vertical-ellipsis-menu-with-three-dots-expansion-24.png",
          title: "To do 1",
          content:
            "Task manager app is a type of software used by many industries for project management",
          date: "12/12/2022",
        },
        {
          image:
            "./../assets/icons8-vertical-ellipsis-menu-with-three-dots-expansion-24.png",
          title: "To do 2",
          content:
            "Task manager app is a type of software used by many industries for project management",
          date: "12/12/2022",
        },
      ],
      Doing: [
        {
          image:
            "./../assets/icons8-vertical-ellipsis-menu-with-three-dots-expansion-24.png",
          title: "Doing",
          content:
            "Task manager app is a type of software used by many industries for project management",
          date: "12/12/2022",
        },
      ],
      Done: [],
      Trash: [
        {
          image:
            "./../assets/icons8-vertical-ellipsis-menu-with-three-dots-expansion-24.png",
          title: "Trash",
          content:
            "Task manager app is a type of software used by many industries for project management",
          date: "12/12/2022",
        },
      ],
    };
  },
  components: {
    Draggable,
  },
};
</script>

<style lang="scss" scoped>
.board {
  background-color: var(--bg-content);
  height: 100vh;
  display: flex;
  flex-direction: column;
}
.board_header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 29px 20px;
  > div {
    display: flex;
    align-items: center;
  }
}
.board_header_search {
  margin-right: 30px;
  position: relative;
}
.search-form {
  position: relative;
  background-color: #e3ecf9;
  width: 350px;
  height: 40px;
  border-radius: 40px;
  //   box-shadow: 0 5px 4px rgba(0, 0, 0, 0.15);
}
.search-input {
  position: absolute;
  left: 40px;
  top: 50%;
  transform: translateY(-50%);
  right: 15px;
  border: none;
  outline: none;
  background: none;
  height: 100%;
}

.search-button {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  left: 15px;
  height: 20px;
  width: 20px;
  padding: 0;
  margin: 0;
  border: none;
  background: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  img {
    width: 20px;
    height: 20px;
  }
}
.board_addtask {
  color: var(--color-text-sidebar);
  background-color: #e3ecf9;
  border-radius: 10px;
  padding: 10px;
  display: flex;
  align-items: center;
  &:hover {
    background-color: white;
  }
  img {
    width: 20px;
  }
}
.board_content {
  display: flex;
  justify-content: space-between;
  padding: 0 20px;
  height: 85%;
  .board_content_block {
    width: 100%;
    display: flex;
    flex-direction: column;
    margin-right: 20px;
    border-radius: 20px;
    &:last-child {
      margin-right: inherit;
    }
    .board_content_block_header {
      display: flex;
      padding: 20px;
      .block_color {
        width: 15px;
        height: 15px;
        border-radius: 5px;
        margin: 5px 5px 0 0;
      }
    }
    .scroll {
      overflow: auto;
      padding: 0 20px 0 20px;
      height: 100%;
      margin-bottom: 20px;
    }
    .board_content_block_body {
      background-color: #fff;
      border-radius: 30px;
      padding: 20px;
      margin: 0 0 20px 0;
      .board_background {
        height: 130px;
        border-radius: 20px;
        background: url("https://c.pxhere.com/photos/6a/97/mountain_fog_peak_landscape_nature-99408.jpg!d");
        background-position: center;
        background-size: cover;
      }
      .board_content_title {
        display: flex;
        justify-content: space-between;
        // align-items: center;
        margin-top: 10px;
        h3 {
          font-size: 18px;
          font-family: var(--font-family);
          font-weight: bold;
        }
        img {
          height: 20px;
        }
      }
      > span {
        font-size: 14px;
      }
      .board_date {
        font-size: 12px;
        img {
          width: 15px;
          margin-right: 10px;
        }
      }
    }
  }
}
.drop-zone {
  height: 100%;
}
.color_text_todo {
  background-color: #eddeb2;
}
.color_todo {
  background-color: #fdf8ea;
}
.color_text_doing {
  background-color: #b5b0eb;
}
.color_doing {
  background-color: #d6d4f2;
}
.color_text_done {
  background-color: #9cf5ac;
}
.color_done {
  background-color: #d6f6dc;
}
.color_text_trash {
  background-color: #eeb1df;
}
.color_trash {
  background-color: #f5e1f0;
}
</style>
