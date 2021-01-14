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
        <h4 id="item_list">Items</h4>
        <p v-for="data in dbData" :key="'item_list'+data._id">{{ data }}</p>
      </b-card-body>
    </b-card>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      dbData: {},
    }
  },

  created() {
    axios.get('http://localhost:8084').then(dump =>{
      this.dbData = dump.data;
      }).catch(err =>{
        console.log(err);
    });
  },

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
