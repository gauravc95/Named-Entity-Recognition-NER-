<template>
  <div id="app">
    <firstPage msg=""/>
  </div>
</template>

<script>
import firstPage from './components/home.vue'

export default {
  name: 'App',
  components: {
    firstPage
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
