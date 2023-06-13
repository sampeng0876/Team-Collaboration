<style scoped>
@import './login-page.css';
</style>

<template>
  <div class="login-container">
    <div class="login-box">
      <img src="@/assets/sp-logo.png" alt="Logo" class="logo" />
      <h1 class="login-heading">Login</h1>
      <form class="login-form">
        <div class="form-group">
          <label for="username">Username</label>
          <input type="text" id="username" v-model="username" class="form-control" required placeholder="Enter your username" />
        </div>
        <div class="form-group">
          <label for="password">Password</label>
          <input type="password" id="password" v-model="password" class="form-control" required placeholder="Enter your password" />
        </div>
        <button type="submit" class="btn btn-primary btn-block" @click.prevent="login">Login</button>
      </form>
    </div>
  </div>
</template>
  


<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
      error: ''
    };
  },
  methods: {
    login() {
      axios.get('http://localhost:3000/users', {
        params: {
          username: this.username,
          password: this.password
        }
      })
        .then(response => {
          const user = response.data[0];
          if (user) {
            // Redirect to the main page or perform necessary actions after successful login
            console.log('Logged in successfully');
            // Example: Redirect to the main page
            this.$router.push('/main');
          } else {
            this.error = 'Invalid username or password';
          }
        })
        .catch(error => {
          console.error(error);
          this.error = 'An error occurred during login';
        });
    }
  }
}
</script>
  