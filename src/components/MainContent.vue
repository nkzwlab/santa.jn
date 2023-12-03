<template>
  <div class="content">
    <h1 class="title">{{ title }}</h1>
    <slot></slot>
  </div>
</template>
<script setup lang="ts">
defineProps({
  title: {
    type: String
  }
})
</script>
<style>
.content {
  background-color: #fff;
  border-radius: 10px;
  max-width: 1000px;
  width: 80%;
  padding: 20px;
}

.title {
  font-size: 2rem;
  margin-bottom: 20px;
}

h1 {
  position: relative;
  line-height: 1.4;
}

/* 雪の結晶や星などの装飾を追加 */
h1:before {
  content: '❄'; /* 雪の結晶のシンボル */
  color: blue; /* 青色 */
  font-size: 24px; /* シンボルのサイズ */
  padding: 0 10px; /* 左右のパディング */
}

h1:after {
  content: '';
  display: block;
  height: 4px;
  background: -webkit-linear-gradient(to right, rgb(230, 90, 90), transparent);
  background: linear-gradient(to right, rgb(230, 90, 90), transparent);
}
</style>
