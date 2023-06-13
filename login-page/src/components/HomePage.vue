<template>
  <div class="home-container">
    <div class="banner">
      <div class="contact-number">
        <!-- Sliding contact number content -->
      </div>
    </div>
    <div class="body">
      <header class="header">
        <div class="logo">
          <!-- Logo image -->
        </div>
        <div class="address">
          <!-- Address information -->
        </div>
        <div class="login-signup">
          <!-- Login/Sign up buttons -->
        </div>
      </header>
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
      <section class="slide-show">
        <!-- Slide show content -->
      </section>
      <section class="product-intro">
        <!-- Product intro content -->
      </section>
      <section class="our-services">
        <!-- Our services content -->
      </section>
      <section class="solution">
        <!-- Solution content -->
      </section>
    </div>
    <footer class="footer">
      <div class="top-footer">
        <div class="about-service">
          <!-- About Our Service section -->
        </div>
        <div class="solutions">
          <!-- Solutions section -->
        </div>
        <div class="contact">
          <!-- Contact section -->
        </div>
      </div>
      <div class="bottom-footer">
        <div class="faq">
          <!-- FAQ section -->
        </div>
        <div class="about">
          <!-- About section -->
        </div>
        <div class="contact">
          <!-- Contact section -->
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  // Component logic goes here
}
</script>

<style scoped>
/* Styles for the HomePage component */

.home-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.banner {
  height: 200px;
  background-color: #f2f2f2;
  display: flex;
  justify-content: center;
  align-items: center;
}

.contact-number {
  font-size: 24px;
  font-weight: bold;
  color: #333;
  animation: slide-in 1s infinite alternate;
}

@keyframes slide-in {
  from {
    transform: translateX(-100%);
  }
  to {
    transform: translateX(0%);
  }
}

.body {
  margin-top: 20px;
}

.header {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.logo {
  flex: 1;
}

.address {
  flex: 1;
  text-align: center;
}

.login-signup {
  flex: 1;
  text-align: right;
}

.slide-show {
  margin-bottom: 20px;
}

.product-intro {
  margin-bottom: 20px;
}

.our-services {
  margin-bottom: 20px;
}

.solution {
  margin-bottom: 20px;
}

.footer {
  background-color: #333;
  color: #fff;
  padding: 20px;
}

.top-footer {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.about-service {
  flex: 1;
}

.solutions {
  flex: 1;
  text-align: center;
}

.contact {
  flex: 1;
  text-align: right;
}

.bottom-footer {
  display: flex;
  align-items: center;
}

.faq {
  flex: 1;
}

.about {
  flex: 1;
  text-align: center;
}

.contact {
  flex: 1;
  text-align: right;
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
/* Additional styles for specific elements can be added here */

</style>

