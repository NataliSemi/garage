<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/login">Login</router-link>
      <router-link to="/register">Register</router-link>
    </div>
    <router-view/>
  </div>
</template>

<style>


#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
  padding: 3em;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
