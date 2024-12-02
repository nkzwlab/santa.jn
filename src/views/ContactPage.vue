<script setup lang="ts">
import MainContent from '@/components/MainContent.vue'
import { ref } from 'vue';

const zokusei = ref<"博士" | "修士" | "学部生" | "卒業生" | null>(null)

const item = ref<{
  name: string
  loginName: string
  graduateYear: string
  companionMiddleSchool: number
  companionElementarySchool: number
  companionInfant: number
  allergies: string[]
  otherAllergies: string
}>({
  name: '',
  loginName: '',
  graduateYear: '',
  companionMiddleSchool: 0,
  companionElementarySchool: 0,
  companionInfant: 0,
  allergies: [],
  otherAllergies: ''
})

const submit = async () => {
  // post localhost:8000/record
  const res = await fetch('http://localhost:8000/record', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      zokusei: zokusei.value,
      ...item.value
    })
  })
  if (res.ok) {
    alert('送信しました')
  } else {
    alert('送信に失敗しました')
  }
}

</script>

<template>
  <MainContent title="参加フォーム">
    <pre>
    2024年度クリスマス会の幹事を務めるM1のtakitoです🎄
    12月14日の14:00より表参道の BRASSERIE CAFÉ LE CONTE にてクリスマスパーティーを実施します！
    会場のリンク：<a href="https://brasseriecafeleconte.foodre.jp/">https://brasseriecafeleconte.foodre.jp/</a>
    皆様のご参加お待ちしております。
    ※フォームの締め切りは12月6日です。
    </pre>
    <div class="w-full flex flex-col gap-4">
      <label class="form-control w-full">
        <div class="label">
          <span class="label-text">属性</span>
        </div>
        <select class="select select-bordered" v-model="zokusei">
          <option disabled selected>選択してください</option>
          <option>Faculty</option>
          <option>博士</option>
          <option>修士</option>
          <option>学部生</option>
          <option>卒業生</option>
        </select>
      </label>
      <label class="form-control w-full">
        <div class="label">
          <span class="label-text">メールアドレス</span>
        </div>
        <input type="email" class="input input-bordered w-full" />
      </label>
      <label class="form-control w-full">
        <div class="label">
          <span class="label-text">本名フルネーム</span>
        </div>
        <input type="text" class="input input-bordered w-full" v-model="item.name" />
      </label>
      <label class="form-control w-full">
        <div class="label">
          <span class="label-text">{{ zokusei !== '卒業生' ? "ログイン名" : "在籍時ログイン名(任意)" }}</span>
        </div>
        <input type="text" class="input input-bordered w-full" v-model="item.loginName" />
      </label>
      <label class="form-control w-full" v-if="zokusei === '卒業生'">
        <div class="label">
          <span class="label-text">卒業年度</span>
        </div>
        <input type="text" class="input input-bordered w-full" v-model="item.graduateYear" />
      </label>
      <label class="form-control w-full" v-if="zokusei === '卒業生'">
        <div class="label">
          <span class="label-text">同行者人数(中学生以上)</span>
        </div>
        <input type="text" class="input input-bordered w-full" v-model="item.companionMiddleSchool" />
      </label>
      <label class="form-control w-full" v-if="zokusei === '卒業生'">
        <div class="label">
          <span class="label-text">同行者人数(小学生)</span>
        </div>
        <input type="text" class="input input-bordered w-full" v-model="item.companionElementarySchool" />
      </label>
      <label class="form-control w-full" v-if="zokusei === '卒業生'">
        <div class="label">
          <span class="label-text">同行者人数(乳幼児/未就学児)</span>
        </div>
        <input type="text" class="input input-bordered w-full" v-model="item.companionInfant" />
      </label>
      <div class="label">
        <span class="label-text">アレルギー</span>
      </div>
      <div v-for="name in ['卵', '乳', '小麦', 'そば', 'えび']" :key="name">
        <label class="label cursor-pointer justify-start gap-2" :for="name">
          <input type="checkbox" :value="name" class="checkbox" v-model="item.allergies" />
          <span class="label-text">{{ name }}</span>
        </label>
      </div>
      <label class="form-control w-full">
        <div class="label">
          <span class="label-text">その他アレルギー</span>
        </div>
        <input type="text" class="input input-bordered w-full" v-model="item.otherAllergies" />
      </label>
      <button @click="submit" class="btn btn-primary">送信</button>
    </div>
  </MainContent>
</template>
<style>
table {
  border-collapse: collapse;
  width: 100%;
}

th,
td {
  border: 1px solid black;
  padding: 8px;
  text-align: left;
}
</style>
<!-- 
【参加フォーム】12月14日開催 中澤大越研究会 クリスマスパーティー
2024年度クリスマス会の幹事を務めるM1のtakitoです🎄
12月14日の14:00より表参道の BRASSERIE CAFÉ LE CONTE  にてクリスマスパーティーを実施します！
会場のリンク：https://brasseriecafeleconte.foodre.jp/
皆様のご参加お待ちしております。
※フォームの締め切りは12月6日です。
tatsuru10330@gmail.com アカウントを切り替える
 
共有なし
 
* 必須の質問です
属性
*
Faculty
博士
修士
学部生
卒業生
ログイン名
フルネーム
*
卒業年度を教えてください
同行者(中学生以上)がいらっしゃいましたら人数を入力してください
同行者(小学生)がいらっしゃいましたら人数を入力してください
同行者(乳幼児/未就学児)がいらっしゃいましたら人数を入力してください
食物アレルギーをお持ちの方のみあてはまるものをお選びください
卵
乳
小麦
そば
えび
その他:
Google フォームでパスワードを送信しないでください。
このフォームは 慶應義塾 内部で作成されました。 不正行為の報告
Google フォーム -->