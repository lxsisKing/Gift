<template>
  <div class="card" :style="{'--img': 'url('+getUrl+')'}">
    <div class="content">
      <h2 class="title">{{ textTitle }}</h2>
      <p class="text">计划你的下一次海滩之旅</p>
      <button class="btn">查看详情</button>
    </div>
  </div>
</template>

<script>
export default {
  props: ['getUrl', 'textTitle'],
  data() {
    return {
      imgUrl: require('../assets/1.jpg'),
    }
  },
};
</script>

<style>
:root {
  --d: 700ms;
  --e: cubic-bezier(0.19, 1, 0.22, 1);
  --font-sans: "Rubik", sans-serif;
  --font-serif: "Cardo", serif;
}
.card {
  position: relative;
  display: -webkit-box;
  display: flex;
  -webkit-box-align: end;
  align-items: flex-end;
  overflow: hidden;
  padding: 1rem;
  width: 100%;
  text-align: center;
  color: whitesmoke;
  background-color: whitesmoke;
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.1), 0 2px 2px rgba(0, 0, 0, 0.1),
    0 4px 4px rgba(0, 0, 0, 0.1), 0 8px 8px rgba(0, 0, 0, 0.1),
    0 16px 16px rgba(0, 0, 0, 0.1);
}

.card:before {
  background-image: var(--img);
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 110%;
  background-size: cover;
  background-position: 0 0;
  -webkit-transition: -webkit-transform calc(var(--d) * 1.5) var(--e);
  transition: -webkit-transform calc(var(--d) * 1.5) var(--e);
  transition: transform calc(var(--d) * 1.5) var(--e);
  transition: transform calc(var(--d) * 1.5) var(--e),
    -webkit-transform calc(var(--d) * 1.5) var(--e);
  pointer-events: none;
}
.card:after {
  content: "";
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 200%;
  pointer-events: none;
  background-image: -webkit-gradient(
    linear,
    left top,
    left bottom,
    from(rgba(0, 0, 0, 0)),
    color-stop(11.7%, rgba(0, 0, 0, 0.009)),
    color-stop(22.1%, rgba(0, 0, 0, 0.034)),
    color-stop(31.2%, rgba(0, 0, 0, 0.072)),
    color-stop(39.4%, rgba(0, 0, 0, 0.123)),
    color-stop(46.6%, rgba(0, 0, 0, 0.182)),
    color-stop(53.1%, rgba(0, 0, 0, 0.249)),
    color-stop(58.9%, rgba(0, 0, 0, 0.32)),
    color-stop(64.3%, rgba(0, 0, 0, 0.394)),
    color-stop(69.3%, rgba(0, 0, 0, 0.468)),
    color-stop(74.1%, rgba(0, 0, 0, 0.54)),
    color-stop(78.8%, rgba(0, 0, 0, 0.607)),
    color-stop(83.6%, rgba(0, 0, 0, 0.668)),
    color-stop(88.7%, rgba(0, 0, 0, 0.721)),
    color-stop(94.1%, rgba(0, 0, 0, 0.762)),
    to(rgba(0, 0, 0, 0.79))
  );
  background-image: linear-gradient(
    to bottom,
    rgba(0, 0, 0, 0) 0%,
    rgba(0, 0, 0, 0.009) 11.7%,
    rgba(0, 0, 0, 0.034) 22.1%,
    rgba(0, 0, 0, 0.072) 31.2%,
    rgba(0, 0, 0, 0.123) 39.4%,
    rgba(0, 0, 0, 0.182) 46.6%,
    rgba(0, 0, 0, 0.249) 53.1%,
    rgba(0, 0, 0, 0.32) 58.9%,
    rgba(0, 0, 0, 0.394) 64.3%,
    rgba(0, 0, 0, 0.468) 69.3%,
    rgba(0, 0, 0, 0.54) 74.1%,
    rgba(0, 0, 0, 0.607) 78.8%,
    rgba(0, 0, 0, 0.668) 83.6%,
    rgba(0, 0, 0, 0.721) 88.7%,
    rgba(0, 0, 0, 0.762) 94.1%,
    rgba(0, 0, 0, 0.79) 100%
  );
  -webkit-transform: translateY(-50%);
  transform: translateY(-50%);
  -webkit-transition: -webkit-transform calc(var(--d) * 2) var(--e);
  transition: -webkit-transform calc(var(--d) * 2) var(--e);
  transition: transform calc(var(--d) * 2) var(--e);
  transition: transform calc(var(--d) * 2) var(--e),
    -webkit-transform calc(var(--d) * 2) var(--e);
}
.content {
  position: relative;
  display: -webkit-box;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  flex-direction: column;
  -webkit-box-align: center;
  align-items: center;
  width: 100%;
  padding: 1rem;
  padding-top: 4rem;
  -webkit-transition: -webkit-transform var(--d) var(--e);
  transition: -webkit-transform var(--d) var(--e);
  transition: transform var(--d) var(--e);
  transition: transform var(--d) var(--e), -webkit-transform var(--d) var(--e);
  z-index: 1;
}
.content > * + * {
  margin-top: 1rem;
}
.title {
  font-size: 1.3rem;
  font-weight: bold;
  line-height: 1.2;
}
.text {
  font-family: var(--font-serif);
  font-style: italic;
  line-height: 1.35;
  font-size: 1.125rem;
}

.btn {
  cursor: pointer;
  margin-top: 1.5rem;
  /* 粗体 */
  font-weight: bold;
  font-size: 0.8rem;
  color: #ffffff;
  background-color: #000000;
  padding: 0.75rem 1.5rem;
  /* 调节字体间距 */
  letter-spacing: 0.05rem;
  border: none;
}

@media (min-width: 600px) {
  .content {
    height: 350px;
  }
}
@media (hover: hover) and (min-width: 600px) {
  .card:after {
    -webkit-transform: translateY(0);
    transform: translateY(0);
  }

  .content > *:not(.title) {
    opacity: 0;
    -webkit-transform: translateY(1rem);
    transform: translateY(1rem);
    -webkit-transition: opacity var(--d) var(--e),
      -webkit-transform var(--d) var(--e);
    transition: opacity var(--d) var(--e), -webkit-transform var(--d) var(--e);
    transition: transform var(--d) var(--e), opacity var(--d) var(--e);
    transition: transform var(--d) var(--e), opacity var(--d) var(--e),
      -webkit-transform var(--d) var(--e);
  }
  .content {
    -webkit-transform: translateY(60%);
    transform: translateY(60%);
  }

  .card:hover,
  .card:focus-within {
    -webkit-box-align: center;
    align-items: center;
  }
  .card:hover:before,
  .card:focus-within:before {
    -webkit-transform: translateY(-4%);
    transform: translateY(-4%);
  }
  .card:hover:after,
  .card:focus-within:after {
    -webkit-transform: translateY(-50%);
    transform: translateY(-50%);
  }
  .card:hover .content,
  .card:focus-within .content {
    -webkit-transform: translateY(0);
    transform: translateY(0);
  }
  .card:hover .content > *:not(.title),
  .card:focus-within .content > *:not(.title) {
    opacity: 1;
    -webkit-transform: translateY(0);
    transform: translateY(0);
    -webkit-transition-delay: calc(var(--d) / 8);
    transition-delay: calc(var(--d) / 8);
  }

  .card:focus-within:before,
  .card:focus-within:after,
  .card:focus-within .content,
  .card:focus-within .content > *:not(.title) {
    -webkit-transition-duration: 0s;
    transition-duration: 0s;
  }
}
</style>
