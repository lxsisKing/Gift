<template>
  <div class="page">
    <div>
      <a class="back" href="/home">返回</a>
    </div>
    <div class="letter">
      <div class="letterContent" :class="{hidden: score < 5}">
        <span class="paragraph">
          <span style="font-size: 40px">宝贝💕</span>
          ，今天是我们在一起的第1096天了。从那时的青涩初吻，到现在的初入社会，三年的时间，我们改变了很多。
          三年来，从两千两百公里到九百公里。我们走过的是别人没有走过的路，是他们无法体会到的感受。
        </span>
        <br />
        <span class="paragraph">
          我们有过180天没见面后再见的紧张，兴奋，开心。也有过在难过时无以言表的无助。可能在接下来的这段时间里，
          我们依旧要经历着我们这三年来所经历过的日子，但是，已经在慢慢变好了不是吗。
          至少现在，我可以在想你的时候，跨越这九百公里的距离🛫去抱抱你了。
          相信在你完成你的学业之后，我们可以在同一座城市，同一间房子，去慢慢地体验属于我们的生活。
        </span>
        <br />
        <span class="paragraph">这些终将会成为我们往后枕边的回忆💑。</span>
        <br />
        <span class="paragraph">
          还记得你曾问过我：是不是在一起越久，就越不在乎了？当然不是啦，在一起越久，你在我心里的分量就越重，怎么会越不在乎呢。
          只是这种分量，更多的是在你生活的方方面面，渗透进去你的生活了。会担心你是否有穿够衣服，是否有吃饱饭，甚至还会担心你是否有钱花。
          可能这就是爱情最深处的模样吧。从一开始的热烈四射，到现在的生活点滴。
        </span>
        <br />
        <span class="paragraph">
          其实呀，我是个很感性的人，虽然身为男儿，也学习了十来年的理工科。但是仍然抹去不了我的感性。
          我认定了你，那就一辈子是你了。我记得我跟你说过，在我们见面时见到你的那一刻，我仍然还会心跳加速，恨不得就直接在众人之下将你搂进怀中。
          这么多年来，从未改变。
        </span>
        <br />
        <span class="paragraph">
          我习惯了将你的照片作为壁纸，让我能够每天都看到你。我习惯了每天早上起床都告诉你一声，我知道你一定可以收到我的消息，
          我习惯了每天吃饭都拍照给你看，虽然你说过我很啰嗦，但是这样让我觉得我无时无刻都有你的陪伴。我也习惯了每天晚上你的“晚安🌙🌙”和“爱你😘😘”，
          让我能够安心睡下。
        </span>
        <br />
        <span class="paragraph">余生很长，愿与子携手共度。</span>
        <br />
        <span style="position: absolute; right: 30px;">刘鑫淞 2020年7月15日✉</span>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import httpaxios from "../unites/httpaxios";
export default {
  data() {
    return {
      score: 0
    };
  },
  computed: {
    ...mapState(["serviceUrl"])
  },
  beforeMount() {
    const getScore = () => {
      let url = this.serviceUrl;
      httpaxios.get(this, url + "/get-score/", response => {
        if (response.data.data !== "Unauthorized") {
          this.score = response.data.data;
          if (this.score < 5) {
            this.$router.push("/login");
          }
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
  position: absolute;
  background: #e2e2e5;
  height: calc(100% - 40px);
  width: calc(100% - 40px);
  z-index: 0;
  display: flex;
  justify-content: center;
  align-items: center;
}
.letter {
  position: absolute;
  width: 1024px;
  height: 600px;
  background-color: #f0efeb;
}
.letterContent {
  padding-left: 10px;
  padding-right: 10px;
  font-size: 20px;
  font-family: "Rubik", sans-serif;
  font-weight: 700;
  margin: 20px;
}
.hidden {
  visibility: hidden;
}
.paragraph {
  padding-left: 40px;
}

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

@media (max-width: 1024px) {
  .letter {
    width: 700px;
    height: 780px;
  }
}
@media (max-width: 700px) {
  .letter {
    width: 500px;
    height: 1050px;
  }
}
@media (max-width: 500px) {
  .letter {
    width: 300px;
    height: 1800px;
  }
}
</style>