<template>
  <form @submit.prevent="submit">
    <h1 class="h3 mb-3 fw-normal">Please sign in</h1>

    <input placeholder="Enter your username" id="login" v-model="loginForm.login" >

    <input placeholder="Enter your password" id="password" v-model="loginForm.password" >


  </form>
</template>


<script>
export default {
  props: {
    logout: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      loginForm: {
        login: null,
        password: null
      },
      user: null,
      loading: false,
      registrationFormServerErrors: []
    }
  },
  created () {
    if (this.logout) {
      this.$notify({
        title: 'You logged out',
        position: 'top-right',
        duration: 5000
      })
      this.$auth.logout()
    } else if (this.$auth.check()) {
      this.$router.push({ name: 'root' })
    }
  },
  methods: {
    getCookie (name) {
      return document.cookie.split(';').some(c => {
        return c.trim().startsWith(name + '=')
      })
    },
    async onSubmit () {
      this.loading = true
      const redirect = this.$auth.redirect()
      this.registrationFormServerErrors = []
      await this.$auth.login({
        data: {
          username: this.loginForm.login,
          password: this.loginForm.password
        },
        redirect: {
          name: redirect ? redirect.from.name : 'root'
        }
      }).then(() => {
        this.$router.go()
      }).catch(err => {
        if (err.response && err.response.status === 401) {
          this.registrationFormServerErrors.push('Wrong credentials')
        } else {
          this.registrationFormServerErrors.push(err.message)
          throw err
        }
      }).finally(() => { this.loading = false })
    }
  }
}
</script>