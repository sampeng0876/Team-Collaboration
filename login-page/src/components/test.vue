<template>
    <div class="home-container">
      <nav class="navbar">
        <ul class="nav-menu">
          <li><router-link to="/">Home</router-link></li>
          <li><router-link to="/product">Product</router-link></li>
          <li><router-link to="/pricing">Pricing</router-link></li>
          <li><router-link to="/about">About</router-link></li>
          <li><router-link to="/contact">Contact</router-link></li>
        </ul>
      </nav>
      <h1>Welcome to the Home Page!</h1>
      <!-- Add your content for the home page -->
    </div>
  </template>
  
  <script>
  export default {
    // Add any necessary component logic or data here
  }
  </script>
  
  <style scoped>
  .home-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
  }
  
  .navbar {
    background-color: #f2f2f2;
    padding: 10px 0;
  }
  
  .nav-menu {
    display: flex;
    list-style: none;
    margin: 0;
    padding: 0;
  }
  
  .nav-menu li {
    margin-right: 15px;
  }
  
  .nav-menu li:last-child {
    margin-right: 0;
  }
  
  .nav-menu li a {
    text-decoration: none;
    color: #333;
    font-weight: bold;
  }
  
  h1 {
    margin-top: 40px;
    text-align: center;
    color: #333;
  }
  </style>
  