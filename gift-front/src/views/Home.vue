<template>
  <div class="page">
    <div>
      <h3 class="score">积分：{{ this.score }}</h3>
    </div>
    <div class="allcards">
      <home-card
        :getUrl="imgOne"
        :textTitle="title.titleOne"
        :textContent="content.contentOne"
        :page="nextPage.pageOne"
      ></home-card>
      <home-card
        :getUrl="imgTwo"
        :textTitle="title.titleTwo"
        :textContent="content.contentTwo"
        :page="nextPage.pageTwo"
        :score="score"
      ></home-card>
      <home-card
        :getUrl="imgOne"
        :textTitle="title.titleThree"
        :textContent="content.contentThree"
        :page="nextPage.pageOne"
        :score="score"
      ></home-card>
      <home-card :getUrl="imgThree" :textTitle="title.titleFour" :textContent="content.contentFour"></home-card>
    </div>
  </div>
</template>

<script>
import httpaxios from "../unites/httpaxios";
import HomeCard from "../components/HomeCard.vue";
import { mapState } from "vuex";
export default {
  components: {
    HomeCard
  },
  data() {
    return {
      score: 0,
      imgOne: require("../assets/1.jpg"),
      imgTwo: require("../assets/2.jpg"),
      imgThree: require("../assets/3.jpg"),
      title: {
        titleOne: "问题",
        titleTwo: "书信",
        titleThree: "小惊喜",
        titleFour: "未完待续..."
      },
      content: {
        contentOne: "要在这里回答一些问题哦",
        contentTwo: "在这里是很多很多真心话哦",
        contentThree: "这里有一点小小的惊喜",
        contentFour: "还有更多等着宝贝哦"
      },
      nextPage: {
        pageOne: "/questions",
        pageTwo: "/letter"
      }
    };
  },
  computed: {
    ...mapState(["serviceUrl"])
  },

  mounted() {
    const getScore = () => {
      let url = this.serviceUrl;
      httpaxios.get(this, url + "/get-score/", response => {
        if (response.data.data !== "Unauthorized") {
          this.score = response.data.data;
        } else {
          localStorage.removeItem("Authorization");
          this.$router.push("/login");
        }
      });
    };
    getScore();
  }
};
</script>

<style scoped>
* {
  box-sizing: border-box;
}

.page {
  background: #e2e2e5;
  display: grid;
  /* font-family: var(--font-sans); */
  height: calc(100% - 40px);
  width: calc(100% - 40px);
  position: absolute;
}
.allcards {
  grid-gap: 1rem;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  place-items: center;
  max-width: 1024px;
  margin: 0 auto;
  padding: 1rem;
}
.score {
  position: absolute;
  right: 15px;
  margin-top: 10px;
  color: #999;
  font-size: 20px;
}

@media (max-width: 800px) {
  .allcards {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 500px) {
  .allcards {
    grid-template-columns: repeat(1, 1fr);
  }
}
</style>