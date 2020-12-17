<template>
  <div class="hello">
    <b-card
      title="WHAT ARE YOU DOING ANDREW!!!!!!!!!!!!!!!!!!"
      img-src="https://media-exp1.licdn.com/dms/image/C4D03AQHDlAmFeET8EQ/profile-displayphoto-shrink_400_400/0/1605769341718?e=1613001600&v=beta&t=Kq7OCBVKw3SsYCcrhoZ6OGxZbHK6noil-_DetW7duu4"
      img-alt="Image"
      img-top
      tag="article"
      style="text-align: center;"
      class="mb-2"
    >
      <b-card-text>
        Some quick example text to build on the card title and make up the bulk of the card's content.
      </b-card-text>

      <b-button href="#" variant="primary">Go somewhere</b-button>
    </b-card>
    <b-card no-body>
      <b-card-body
        id="nav-scroller"
        ref="content"
        style="max-width: 30rem;right: 10px; height:1000px; overflow-y:scroll;"
      >
        <p>{{ text }}</p>
        <h4 id="fat">@fat</h4>
        <p v-for="i in 3" :key="i">{{ text }}</p>
        <h4 id="mdo">@mdo</h4>
        <p v-for="i in 3" :key="i">{{ text }}</p>
        <h4 id="one">one</h4>
        <p v-for="i in 2" :key="i">{{ text }}</p>
        <h4 id="two">two</h4>
        <p>{{ text }}</p>
        <h4 id="three">three</h4>
        <p v-for="i in 2" :key="i">{{ text }}</p>
        <h4 id="pi0">@pi0</h4>
        <p v-for="i in 3" :key="i">{{ text }}</p>
      </b-card-body>
    </b-card>
  </div>
</template>

<script>
export default {
  methods: {
    // Convenience method to scroll a heading into view.
    // Not required for scrollspy to work
    scrollIntoView(event) {
      event.preventDefault()
      const href = event.target.getAttribute('href')
      const el = href ? document.querySelector(href) : null
      if (el) {
        this.$refs.content.scrollTop = el.offsetTop
      }
    }
  },
  data() {
    return {
      text: `
        Quis magna Lorem anim amet ipsum do mollit sit cillum voluptate ex nulla
        tempor. Laborum consequat non elit enim exercitation cillum aliqua
        consequat id aliqua. Esse ex consectetur mollit voluptate est in duis
        laboris ad sit ipsum anim Lorem. Incididunt veniam velit elit elit veniam
        Lorem aliqua quis ullamco deserunt sit enim elit aliqua esse irure. Laborum
        nisi sit est tempor laborum mollit labore officia laborum excepteur
        commodo non commodo dolor excepteur commodo. Ipsum fugiat ex est consectetur
        ipsum commodo tempor sunt in proident.
      `
    }
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

.hello {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
}
</style>
