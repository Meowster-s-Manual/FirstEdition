<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Ping',
  data() {
    return {
      msg: 'Hello!',
    };
  },
  methods: {
    getData() {
      axios.get('http://70.112.90.159:61425/').then(dump =>{
	this.msg = dump.data;
      }).catch(err =>{
        console.log(err);
      });
    },   
  },
  created() {
    console.log(this);
    console.log(this.msg);
    this.getData();
  },
};
</script>

