<script setup lang="ts">
import MainContent from '@/components/MainContent.vue'
import { ref, onMounted, computed } from 'vue'

const loading = ref(true)

const filterItem = ref<string | null>(null)

const filters = [
  { label: '全て', value: null },
  { label: 'Faculty', value: 'Faculty' },
  { label: '博士', value: '博士' },
  { label: '修士', value: '修士' },
  { label: '学部生', value: '学部生' },
  { label: '卒業生', value: '卒業生' }
]

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
  if (filterItem.value) {
    return _participants.filter((item) => item.attribute === filterItem.value)
  }
  return _participants
})

onMounted(() => {
  fetchParticipants()
})

function fetchParticipants() {
  loading.value = true
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
    .finally(() => {
      loading.value = false
    })
}
</script>

<template>
  <MainContent title="参加者一覧">
    <div v-if="!loading">
      <div>
        <select v-model="filterItem">
          <option v-for="filter in filters" :key="filter.value ?? ''" :value="filter.value">
            {{ filter.label }}
          </option>
        </select>
      </div>
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
    </div>
    <div v-else>読み込み中</div>
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

select {
  width: 100%;
  height: 40px;
  font-size: 1rem;
  padding: 0 10px;
  border-radius: 5px;
  border: 1px solid #ccc;
  outline: none;
  appearance: none;
  background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' fill='%23333333' viewBox='0 0 16 16'%3E%3Cpath d='M8 10.586L4.707 7.293a1 1 0 00-1.414 1.414l4 4a1 1 0 001.414 0l4-4a1 1 0 00-1.414-1.414L8 10.586z'/%3E%3C/svg%3E")
    no-repeat right 10px center/15px 15px;
  margin-bottom: 10px;
}
</style>
