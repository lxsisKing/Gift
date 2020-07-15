<template>
  <div class="page">
    <div>
      <h1 id="question" class="question">{{ question }}</h1>
      <input
        id="answer"
        class="answer_input"
        type="text"
        :placeholder="question"
        @keydown="changeWidth"
      />
    </div>
  </div>
</template>

<script>
import httpaxios from "../unites/httpaxios";
import { mapState } from "vuex";
import { Dialog, Notify } from "vant";
export default {
  components: {
    [Notify.name]: Notify,
    [Dialog.name]: Dialog,
  },
  data() {
    return {
      allQuestions: {},
      question: "",
      answer: ""
    };
  },
  computed: {
    ...mapState(["serviceUrl"])
  },
  methods: {
    moveQuestion() {
      let answer = document.getElementById("answer");
      answer.placeholder = "";
      answer.style.height = "60px";
      answer.style.transition = "1s ease";

      let question = document.getElementById("question");
      question.style.opacity = 1;
      question.style.transition = "2s ease";
    },
    changeWidth(e) {
      let answer = document.getElementById("answer");
      let question = document.getElementById("question");
      answer.style.width = answer.value.length * 40 + "px";
      if (e.keyCode == 13) {
        if (answer.value === this.allQuestions[1][1]["answer"]) {
          question.style.transition = "";
          question.style.opacity = 0;
          this.question = this.allQuestions[2][0]["question"];
          answer.value = "";
          answer.style.height = "50px";
          answer.blur();
        } else {
          // Dialog.alert({
          //   message: '回答错误哦',
          // }).then(() => {});
          Notify({ type: "warning", message: "回答错误哦！" });
        }
      }
    }
  },
  beforeMount() {
    const getQuestions = () => {
      let url = this.serviceUrl;
      httpaxios.get(this, url + "/show-questions/", response => {
        this.allQuestions = response.data;
        this.question = response.data[1][0]["question"];
      });
    };
    getQuestions();
  },

  mounted() {
    document
      .querySelector("#answer")
      .addEventListener("focus", this.moveQuestion, true);
  },
  updated() {
    const initialWidth = () => {
      let answer = document.getElementById("answer");
      answer.style.width = answer.placeholder.length * 40 + "px";
    };

    initialWidth();
  }
};
</script>

<style scoped>
* {
  box-sizing: border-box;
}

.page {
  display: grid;
  position: absolute;
  background-color: #e2e2e5;
  height: calc(100% - 40px);
  width: calc(100% - 40px);
  text-align: center;
  place-items: center;
}
.answer_input {
  min-width: 80px;
  text-align: center;
  border-bottom-style: solid;
  border-top-style: solid;
  border-left-style: none;
  border-right-style: none;
  border-width: 5px;
  border-color: #999;
  height: 50px;
  color: #999;
  background-color: rgba(0, 0, 0, 0);
  font-weight: 700;
  font-size: 40px;
}
.question {
  position: relative;
  font-size: 40px;
  opacity: 0;
  margin-bottom: 5px;
}
/* .questions:hover {
  opacity: 1;
  transform: translateY(-50px);
  transition: 2s ease;
  pointer-events: none;
} */
</style>