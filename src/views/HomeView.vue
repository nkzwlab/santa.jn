<script setup lang="ts">
import MainContent from '@/components/MainContent.vue'
import { ref, onMounted, computed } from 'vue'

interface Participant {
  name: string
  loginname: string
  attribute: string
}

const participants = ref<Participant[]>([])

const sortedParticipants = computed(() => {
  const _participants = participants.value
  _participants.sort((a, b) => {
    const order = ['Faculty', '博士', '修士', '学部生', '卒業生']
    const aIndex = order.indexOf(a.attribute)
    const bIndex = order.indexOf(b.attribute)
    return aIndex - bIndex
  })
  return _participants
})

onMounted(() => {
  fetchParticipants()
})

function fetchParticipants() {
  const url = 'https://api.sheety.co/9d16b6b7e0afa9dd48e3fcf1257b3c4f/xmasParticipant/form1'
  fetch(url)
    .then((response) => response.json())
    .then((json) => {
      participants.value = json.form1.map((item: any) => ({
        name: item.フルネーム,
        loginname: item.ログイン名,
        attribute: item.属性
      }))
    })
    .catch((error) => {
      console.error('データの取得中にエラーが発生しました:', error)
    })
}
</script>

<template>
  <MainContent title="中澤大越研究室クリスマスパーティー">
    <h2 id="-">開催日時・場所(お店へのリンク、地図アプリへのリンク)</h2>
    <h4>開催日時</h4>
    <p>12月16日(土) 17:30から</p>
    <h4>開催場所</h4>
    <p>Harlod＆Co</p>
    <p>
      <a href="https://supertramps.jp/restaurant/harold/"
        >https://supertramps.jp/restaurant/harold/</a
      >
    </p>
    <p>〒107-0061 東京都港区北青山３丁目６−２３ 青山ダイハンビル B1F</p>
    <p>
      グーグルマップ：<a href="https://maps.app.goo.gl/7SUy4P63HpZzhK4i6"
        >https://maps.app.goo.gl/7SUy4P63HpZzhK4i6</a
      >
    </p>
    <p>東京メトロ表参道駅B2出口から徒歩30秒</p>
    <p>表参道駅から143m</p>
    <h2 id="-">参加フォーム</h2>
    <p>参加してくださる方は、以下のフォームへの回答をお願いいたします。</p>
    <p>
      参加フォームは<a
        href="https://docs.google.com/forms/d/e/1FAIpQLSdt80-fEFqZyddYr7rdDecKbxEsQlb8ZSu207VySj-Iu4BCsg/viewform"
        >こちら</a
      >
    </p>
    <p>締め切りは1週間前の12月9日(土)です。</p>
    <h2 id="-">プレゼント交換</h2>
    <p>各自一人一つプレゼントを持ち寄り、ランダムに交換するイベントです！</p>
    <p>プレゼントの予算は2000円程度です。</p>
    <h2 id="-">会費</h2>
    <p>faculty,OB/OGの方々：10000円</p>
    <p>学部生・院生：5000円</p>
    <p>※人数の変動などにより変更になる可能性があります</p>
    <h2 id="-">服装に関して</h2>
    <p>
      また、ドレスコードはラフでなければ自由とさせていただきますが、かっこいい、もしくはゴージャスなスタイルでいらしてください。
    </p>
    <p>男性 スーツ/女性 ドレス などが無難です。</p>
    <h2 id="-">当日のタイムスケジュール</h2>
    <p>17:00~17:30 入場＆会場準備</p>
    <p>17:30 乾杯</p>
    <p>18:00~18:20 プレゼント交換タイム</p>
    <p>18:30~19:00 トーク（ひとり3~5分程度）</p>
    <p>19:00~19:20 余興</p>
    <p>19:30 締めの挨拶</p>
    <p>~20:00 退場</p>
    <h2 id="-">参加者一覧</h2>
    <table>
      <tr>
        <th>参加者氏名</th>
        <th>ログイン名</th>
        <th>属性</th>
      </tr>
      <tr v-for="participant in sortedParticipants" :key="participant.name">
        <td>{{ participant.name }}</td>
        <td>{{ participant.loginname }}</td>
        <td>{{ participant.attribute }}</td>
      </tr>
    </table>

    <h2 id="-">連絡先</h2>
    <p>M1:影嶋亮太朗（090-6376-2812,kageshima23 (あっとまーく) keio.jp)</p>
    <p>M1:富沢立（070-8981-7627,tatsuru (あっとまーく) keio.jp）</p>
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
