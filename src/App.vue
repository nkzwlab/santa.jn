<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div class="wrapper">
    <header>
      <div class="logo__container">
        <img class="logo" src="@/assets/no-christmas.png" />
        <span> 中澤・大越研究室 クリスマスパーティー </span>
      </div>
    </header>
    <!-- <div class="links">
      <div>
        <RouterLink to="/">Home</RouterLink>
      </div>
      <div>
        <RouterLink to="/about">About</RouterLink>
      </div>
    </div> -->
    <RouterView />
  </div>
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  height: 100px;
  width: auto;
}

.logo__container {
  display: flex;
  align-items: center;
  color: white;
  /* blur */
  text-shadow: 0 0 5px #fff;
  font-family: 'Kaisei Tokumin', serif !important;
  font-size: 2rem;

  gap: 10px;

  font-weight: 500;
}

.wrapper {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 20px;
  align-items: center;
  margin: 20px 0;
}

nav {
  color: #fff;
}
nav::before {
  content: '❄️';
  display: block;
}
</style>
