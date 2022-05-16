import axios from 'axios'
import qs from 'qs'

export let globals = {
  authed: false,
}

export function request(url, data, succ, fail, times) {
  if (times !== 0) {
    fail = fail ?? (() => setTimeout(request, 1000, url, data, succ, undefined, (times ?? 10) - 1))
    axios.post(url, qs.stringify(data)).then(value => {
      if (value.data['status'] === 'ok') {
        succ(value.data['data'])
      } else {
        fail()
      }
    }, fail).catch(fail)
  }
}

export function getOfficialKeywords(callback) {
  let now = Date.now()
  let official = JSON.parse(localStorage.getItem('officialKeywords') ?? '[]')
  let officialTime = parseInt(localStorage.getItem('officialTime') ?? '0')

  if (official.length === 0 || now - officialTime >= 86400000) {
    request('/keywords', {}, data => {
      localStorage.setItem('officialKeywords', JSON.stringify(data))
      localStorage.setItem('officialTime', now.toString())
      callback(data)
    })
  } else {
    callback(official)
  }
}

export function getHistoryKeywords() {
  return JSON.parse(localStorage.getItem('historyKeywords') ?? '[]')
}

export function addHistoryKeywords(keyword) {
  removeHistoryKeywords(keyword)
  let history = JSON.parse(localStorage.getItem('historyKeywords') ?? '[]')
  history.push(keyword)
  localStorage.setItem('historyKeywords', JSON.stringify(history))
}

export function removeHistoryKeywords(keyword) {
  let history = JSON.parse(localStorage.getItem('historyKeywords') ?? '[]')
  let index = history.indexOf(keyword)

  if (index !== -1) {
    history.splice(index, 1)
  }

  localStorage.setItem('historyKeywords', JSON.stringify(history))
}
