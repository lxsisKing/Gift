<template>
  <div class="page">
    <div class="container">
      <div class="left">
        <div class="loginTop">我们在一起：</div>
        <div class="login">{{ time }}</div>
        <div class="eula">三周年快乐！❤❤❤</div>
      </div>
      <div class="right">
        <svg viewBox="0 0 320 300">
          <defs>
            <linearGradient
              inkscape:collect="always"
              id="linearGradient"
              x1="13"
              y1="193.49992"
              x2="307"
              y2="193.49992"
              gradientUnits="userSpaceOnUse"
            >
              <stop style="stop-color:#ff00ff;" offset="0" id="stop876" />
              <stop style="stop-color:#ff0000;" offset="1" id="stop878" />
            </linearGradient>
          </defs>
          <path
            d="m 40,120.00016 239.99984,-3.2e-4 c 0,0 24.99263,0.79932 25.00016,35.00016 0.008,34.20084 -25.00016,35 -25.00016,35 h -239.99984 c 0,-0.0205 -25,4.01348 -25,38.5 0,34.48652 25,38.5 25,38.5 h 215 c 0,0 20,-0.99604 20,-25 0,-24.00396 -20,-25 -20,-25 h -190 c 0,0 -20,1.71033 -20,25 0,24.00396 20,25 20,25 h 168.57143"
          />
        </svg>
        <div class="form">
          <label for="username">账号</label>
          <input type="text" id="username" v-model="loginForm.username" />
          <label for="password">密码</label>
          <input type="password" id="password" v-model="loginForm.passwd" />
          <input type="submit" id="submit" value="提交" @click="login" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapMutations } from "vuex";
import anime from "animejs";
import httoaxios from "../unites/httpaxios.js";
import { Notify } from "vant";
export default {
  components: {
    [Notify.name]: Notify
  },
  data() {
    return {
      interval: "",
      time: "",
      loginForm: {
        username: "",
        passwd: ""
      }
    };
  },
  computed: {
    ...mapState(["serviceUrl"])
  },
  methods: {
    // serviceUrl返回的是一个函数，return this.$store.st ate.serviceUrl
    ...mapMutations(["changeLogin"]),
    login() {
      // let that = this
      if (this.loginForm.username === "" || this.loginForm.passwd === "") {
        Notify({ type: "warning", message: "账号或密码不能为空！" });
      } else {
        // let url = this.serviceUrl
        let url = this.serviceUrl;
        httoaxios.post(this, url + "/ver/", this.loginForm, response => {
          if (response.data.code === 200) {
            let token = response.data.token;
            this.changeLogin(token);
            this.$router.push("/home");
          } else {
            Notify({ type: "warning", message: "账号或密码错误！" });
          }
        });
      }
    },
    usernameAnime() {
      if (this.current) {
        this.current.pause();
      }
      this.current = anime({
        targets: "path", //定义了制作动画的元素或对象
        strokeDashoffset: {
          value: 0,
          duration: 700,
          easing: "easeOutQuart"
        },
        strokeDasharray: {
          value: "240 1386",
          duration: 700,
          easing: "easeOutQuart"
        }
      });
    },
    passwordAnime() {
      if (this.current) {
        this.current.pause();
      }
      this.current = anime({
        targets: "path",
        strokeDashoffset: {
          value: -336,
          // duration：设置动画
          duration: 700,
          easing: "easeOutQuart"
        },
        strokeDasharray: {
          value: "240 1386",
          duration: 700,
          easing: "easeOutQuart"
        }
      });
    },
    submitAnime() {
      if (this.current) {
        this.current.pause();
      }
      this.current = anime({
        targets: "path",
        strokeDashoffset: {
          value: -730,
          duration: 700,
          easing: "easeOutQuart"
        },
        strokeDasharray: {
          value: "530 1386",
          duration: 700,
          easing: "easeOutQuart"
        }
      });
    },
    getTime() {
      let beginTime = "2017/07/15 21:00:00";
      let nowTime = new Date();
      let time = nowTime.getTime() - new Date(beginTime).getTime();

      let days = Math.floor(time / (24 * 3600 * 1000));

      let leftOne = time % (24 * 3600 * 1000);
      let hours = Math.floor(leftOne / (3600 * 1000));

      let leftTwo = leftOne % (3600 * 1000);
      let minutes = Math.floor(leftTwo / (60 * 1000));

      let leftThree = leftTwo % (60 * 1000);
      let seconds = Math.floor(leftThree / 1000);

      
      this.time = days + "天" + hours + "小时" + minutes + "分钟" + seconds + "秒"
      
    }
  },

  mounted() {
    document
      .querySelector("#username")
      .addEventListener("focus", this.usernameAnime, true);
    document
      .querySelector("#password")
      .addEventListener("focus", this.passwordAnime, true);
    document
      .querySelector("#submit")
      .addEventListener("focus", this.submitAnime, true);

    this.interval = setInterval(this.getTime, 1000);
  },
  beforeDestroy() {
    clearInterval(this.interval);
  }
};
</script>

<style scoped>
::selection {
  background: #2d2f36;
}
::-webkit-selection {
  background: #2d2f36;
}
::-moz-selection {
  background: #2d2f36;
}
body {
  background: white;
  font-family: "Inter UI", sans-serif;
  margin: 0;
  padding: 20px;
}
.page {
  background: #e2e2e5;
  display: flex;
  flex-direction: column;
  height: calc(100% - 40px);
  position: absolute;
  place-content: center;
  width: calc(100% - 40px);
}
@media (max-width: 767px) {
  .page {
    height: auto;
    margin-bottom: 20px;
    padding-bottom: 20px;
  }
}
.container {
  display: flex;
  height: 320px;
  margin: 0 auto;
  width: 640px;
}
@media (max-width: 767px) {
  .container {
    flex-direction: column;
    height: 630px;
    width: 320px;
  }
}
.left {
  background: white;
  height: calc(100% - 40px);
  top: 20px;
  position: relative;
  width: 50%;
}
@media (max-width: 767px) {
  .left {
    height: 100%;
    left: 20px;
    width: calc(100% - 40px);
    max-height: 270px;
  }
}
.loginTop {
  font-size: 30px;
  font-weight: 900;
  margin: 30px 20px 10px;
}
.login {
  font-size: 30px;
  font-weight: 900;
  margin: 10px 20px 10px;
}
.eula {
  color: #999;
  font-size: 20px;
  line-height: 1.5;
  margin: 30px;
}
.right {
  background: #474a59;
  box-shadow: 0px 0px 40px 16px rgba(0, 0, 0, 0.22);
  color: #f1f1f2;
  position: relative;
  width: 50%;
}
@media (max-width: 767px) {
  .right {
    flex-shrink: 0;
    height: 100%;
    width: 100%;
    max-height: 350px;
  }
}
svg {
  position: absolute;
  width: 320px;
}
path {
  fill: none;
  stroke: url(#linearGradient);
  stroke-width: 4;
  stroke-dasharray: 240 1386;
}
.form {
  margin: 40px;
  position: absolute;
}
label {
  color: #c2c2c5;
  display: block;
  font-size: 14px;
  height: 16px;
  margin-top: 20px;
  margin-bottom: 5px;
}
input {
  background: transparent;
  border: 0;
  color: #f2f2f2;
  font-size: 20px;
  height: 30px;
  line-height: 30px;
  outline: none !important;
  width: 100%;
}
input::-moz-focus-inner {
  border: 0;
}
#submit {
  color: #707075;
  margin-top: 40px;
  transition: color 300ms;
}
#submit:focus {
  color: #f2f2f2;
}
#submit:active {
  color: #d0d0d2;
}
</style>
