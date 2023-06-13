
<style scoped>
@import './login-page.css';
</style>

<template>
  <div class="signup-container">
    <div class="signup-box">
      <img src="@/assets/sp-logo.png" alt="Logo" class="logo" />
      <h1 class="signup-heading">SignUp</h1>
      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label for="username">Username</label>
          <input type="text" id="username" v-model="formData.username" class="form-control" required placeholder="Enter your username">
        </div>
        <div class="form-group">
          <label for="password">Password</label>
          <input type="password" id="password" v-model="formData.password" class="form-control" required placeholder="Enter your password">
        </div>
        <button type="submit" class="btn-primary">Sign Up</button>
      </form>
    </div>
  </div>
</template>


<script>
import axios from 'axios';

export default {
  // ...
  data() {
    return {
      formData: {
        username: '',
        password: ''
      }
    };
  },
  methods: {
    async submitForm() {
      try {
        // Send POST request to JSON Server API
        const response = await axios.post('http://localhost:3000/users', this.formData);
        console.log('User created:', response.data);

        // Reset form fields after successful signup
        this.formData.username = '';
        this.formData.password = '';

        // Redirect to login page or perform any other desired action
        this.$router.push({ name: 'Home' })
      } catch (error) {
        console.error('Error creating user:', error);
        // Handle error case
      }
    }
  }
}
</script>



  


<!-- <script>
import axios from 'axios';


export default {
    name: 'SignUp',
  data() {
    return {
      username: '',
      password: '',
    }
  },
  methods:{
    signUp(){
        let result = axios.post('http://localhost:3000/users',{ 
            username: this.username, 
            password: this.password 
        })

        console.log(result);
        if(result.status==201)
        {
            alert('SignUp successful')
            localStorage.setItem('user-info', JSON.stringify(result.data))
        }
    }
  }
  
}
</script> -->
  