<template>
  <div class="page">
    <div class="allcards">
      <home-card></home-card>
      <home-card></home-card>
      <home-card></home-card>
    </div>
  </div>
</template>

<script>
import HomeCard from "../components/HomeCard.vue";
export default {
  components: {
    HomeCard
  },
  data() {
    return "a";
  }
};
</script>

<style>
* {
  box-sizing: border-box;
}

body {
  background: white;
}
.page {
  background: #e2e2e5;
  display: grid;
  /* font-family: var(--font-sans); */
  height: calc(100% - 40px);
  width: calc(100% - 40px);
}
.allcards {
  grid-gap: 1rem;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  place-items: center;
  max-width: 1024px;
  margin: 0 auto;
  padding: 1rem;
}

/* @media (min-width: 600px) {
  .page-content {
    grid-template-columns: repeat(2, 1fr);
  }
}
@media (min-width: 800px) {
  .page-content {
    grid-template-columns: repeat(4, 1fr);
  }
}

@media (min-width: 600px) {
    .casr {
        height: 350px;
    }
} */
</style>