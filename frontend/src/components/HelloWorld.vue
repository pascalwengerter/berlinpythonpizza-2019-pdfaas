<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <details style="margin-bottom: 25px;">
      <summary>PDF PRINT</summary>
      <form action="http://localhost:5000/pdf-1" method="get" target="_blank">
        <input type="submit" value="Request PDF" />
      </form>
    </details>
    <details>
      <summary>ALL YOUR DATA</summary>
      <form action="http://localhost:5000/pdf-2" method="get" target="_blank">
        First name: <input type="text" name="name" />
        <input type="submit" value="Request PDF" />
      </form>
    </details>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
