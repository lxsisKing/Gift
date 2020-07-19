<template>
  <div class="page">
    <div>
      <a class="back" href="/home">返回</a>
    </div>
    <div class="QandA">
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
    [Dialog.name]: Dialog
  },
  data() {
    return {
      score: 0,
      allQuestions: [],
      question: "",
      answer: "",
      num: -1
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
      let l = this.allQuestions.length;
      if (e.keyCode == 13) {
        if (answer.value === this.allQuestions[this.num]["answers"]) {
          question.style.transition = "";
          question.style.opacity = 0;
          this.num += 1;
          let url = this.serviceUrl;
          this.score = this.num;
          httpaxios.post(
            this,
            url + "/change-score/",
            { score: this.score },
            response => {
              console.log(response);
            }
          );
          if (this.num >= l) {
            this.$router.push("/home");
          } else {
            this.question = this.allQuestions[this.num]["questions_text"];
            answer.value = "";
            answer.style.height = "50px";
            answer.blur();
          }
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
    const getScore = () => {
      let url = this.serviceUrl;
      httpaxios.get(this, url + "/get-score/", response => {
        if (response.data.data !== "Unauthorized") {
          this.score = response.data.data;
          this.num = this.score;
        } else {
          localStorage.removeItem("Authorization");
          this.$router.push("/login");
        }
      });
    };
    getScore();

    const getQuestions = () => {
      let url = this.serviceUrl;
      httpaxios.get(this, url + "/show-questions/", response => {
        if (response.data.data !== "Unauthorized") {
          this.allQuestions = response.data.data;
          let l = this.allQuestions.length;
          if (this.num >= l) {
            Dialog.alert({
              message: "你已经答完全部题目了哦"
            }).then(() => {
              this.$router.push("/home");
            });
          } else {
            this.question = this.allQuestions[this.num]["questions_text"];
          }
        } else {
          localStorage.removeItem("Authorization");
          this.$router.push("/login");
        }
      });
    };
    if (this.num === -1) {
      setTimeout(getQuestions(), 1000);
    } else {
      getQuestions();
    }
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
.QandA {
  position: absolute;
  margin-top: -100px;
}
.answer_input {
  min-width: 200px;
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
  font-size: 40px;
  opacity: 0;
  margin-bottom: 5px;
}
@media (max-width: 500px) {
  .answer_input {
    font-size: 15px;
    min-width: 50;
    width: 50px;
    height: 30px;
  }
  .question {
    font-size: 15px;
  }
}
/* .questions:hover {
  opacity: 1;
  transform: translateY(-50px);
  transition: 2s ease;
  pointer-events: none;
} */
.back {
  position: absolute;
  right: 15px;
  top: 10px;
  font-size: 20px;
  font-weight: 700;
  color: #999;
}
.back:link {
  color: #999;
}
.back:visited {
  color: #999;
}
.back:active {
  color: #999;
}
.back:hover {
  color: gray;
}
</style>