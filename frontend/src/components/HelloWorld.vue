<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <form action="http://localhost:5000/pdf-1" method="post">
      <input type="submit" name="buttonone" value="Request PDF" />
    </form>
    <form action="http://localhost:5000/pdf-2" method="post">
      <input type="text" name="Name" value="name" />
      <input type="submit" name="buttonone" value="Request PDF" />
    </form>
    <form action="http://localhost:5000/pdf-3" method="post">
      <input type="submit" name="buttonone" value="Request PDF" />
    </form>
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
