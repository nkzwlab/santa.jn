<script setup lang="ts">
import MainContent from '@/components/MainContent.vue'
</script>

<template>
  <MainContent title="中澤大越研究室クリスマスパーティー">
    <h2 id="-">開催日時・場所(お店へのリンク、地図アプリへのリンク)</h2>
    <h4>開催日時</h4>
    <p>2024年12月14日(土) 14:00から</p>
    <h4>開催場所</h4>
    <p>BRASSERIE CAFÉ LE CONTE</p>
    <p>
      <a href="https://supertramps.jp/restaurant/harold/"
        >https://supertramps.jp/restaurant/harold/</a
      >
    </p>
    <p>〒107-0062 東京都港区南青山3-18-19 フェスタ表参道 3F</p>
    <p>
      グーグルマップ：<a href="https://maps.app.goo.gl/CioJapv4DwEnvCXq7"
        >https://maps.app.goo.gl/CioJapv4DwEnvCXq7</a
      >
    </p>
    <p>東京メトロ銀座線 表参道駅A4出口から徒歩1分</p>
    <p>表参道駅から70m</p>
    <p>東京メトロ銀座線 外苑前駅a1出口から徒歩11分</p>
    <p>外苑前駅から810m</p>
    <p>東京メトロ千代田線 明治神宮前駅から徒歩14分</p>
    <p>明治神宮前駅から1.1km</p>

    <h2 id="-">参加フォーム</h2>
    <p>参加してくださる方は、以下のフォームへの回答をお願いいたします。</p>
    <p>
      参加フォームは<a
        href="https://forms.gle/WfJwFkfC2KYUAK2n8"
        >こちら</a
      >
    </p>
    <p>締め切りは1週間前の12月6日(金)です。</p>
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
    <p>13:30~14:00 開場・受付</p>
    <p>14:15 乾杯</p>
    <p>14:30~14:50 プレゼント交換タイム</p>
    <p>15:00~16:00 トーク（ひとり3~5分程度）・余興</p>
    <p>16:30 締めの挨拶</p>
    <p>~16:45 退場</p>
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
    <p>M1:浦田 駿（-,- (あっとまーく) keio.jp)</p>
    <p>M1:伊藤 隆（080-2249-6400,ito_takashi (あっとまーく) keio.jp）</p>
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
