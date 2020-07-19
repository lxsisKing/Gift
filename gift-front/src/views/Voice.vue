<template>
  <div class="page">
      <audio src="../assets/Nevada.mp3" controls="controls" :class="{hidden: score < 10}"></audio>
  </div>
</template>


<script>
import { mapState } from 'vuex';
import httpaxios from '../unites/httpaxios';
export default {
    data() {
        return {
            score: 0
        };
    },
    computed: {
        ...mapState(['serviceUrl'])
    },
    beforeMount() {
            const getScore = () => {
      let url = this.serviceUrl;
      httpaxios.get(this, url + "/get-score/", response => {
        if (response.data.data !== "Unauthorized") {
          this.score = response.data.data;
          if (this.score < 10) {
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
}
</script>

<style scoped>
* {
    box-sizing: border-box;
}

.page {
    background: #e2e2e5;
    width: calc(100% - 40px);
    height: calc(100% - 40px);
    position: absolute;
    display: flex;
    justify-content: center;
    align-items: center;
}
.hidden {
  visibility: hidden;
}
</style>
