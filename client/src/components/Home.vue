<template>
  <div class="hello">
    <b-card
      title="WHAT ARE YOU DOING ANDREW!!!!!!!!!!!!!!!!!!"
      img-src="https://media-exp1.licdn.com/dms/image/C4D03AQHDlAmFeET8EQ/profile-displayphoto-shrink_400_400/0/1605769341718?e=1613001600&v=beta&t=Kq7OCBVKw3SsYCcrhoZ6OGxZbHK6noil-_DetW7duu4"
      img-alt="Image"
      img-top
      tag="article"
      style="max-width: 20rem; text-align: center; margin: 0 auto;"
      class="mb-2"
    >
      <b-card-text>
        Some quick example text to build on the card title and make up the bulk of the card's content.
      </b-card-text>

      <b-button href="#" variant="primary">Go somewhere</b-button>
    </b-card>

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

<!-- Add "scoped" attribute to limit CSS to this component only -->
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
