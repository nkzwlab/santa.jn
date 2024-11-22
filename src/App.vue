<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div class="wrapper">
    <header class="header">
      <div class="logo__container">
        <img class="logo" src="@/assets/no-christmas.png" />
        <div class="logo__text">
          <span> 中澤・大越研究室</span> <span>クリスマスパーティー</span>
        </div>
      </div>
    </header>
    <div class="links">
      <div>
        <RouterLink to="/">イベント概要</RouterLink>
      </div>
      <!-- <div>
        <RouterLink to="/participants">参加者一覧</RouterLink>
      </div> -->
    </div>
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

.logo__text {
  display: flex;
  flex-direction: row;
  gap: 5px;

  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  /* shrink */
  flex-shrink: 1;
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

.header {
  margin: 10px;
}

.links > div > a {
  color: white;
}

.links > div > a:before {
  content: '❄️';
  display: inline-block;
  margin-right: 5px;
}

.links {
  display: flex;
  gap: 20px;
}
</style>
