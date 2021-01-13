<template>
  <div class="container mt-5 mb-5">
    <div class="row">
        <ProductItem class="col-md-4 mt-4"
          v-for="product in products"
          :name="product.PRDName"
          :description="product.PRDDesc"
          :instock="product.PRDInstock"
          :price="parseInt(product.PRDPrice)"
          :image="product.PRDIImage"
          :discount="parseInt(product.PRDDiscount)"
          :key="product.id"
          />
    </div>
  </div>
</template>

<script>
import ProductItem from '@/components/ProductItem.vue'
import axios from 'axios'

export default {
  name: 'Home',
  components: {
    ProductItem
  },
  data() {
    return {
      products: [],
    }
  },
  mounted() {
    this.getProducts()
    this.cart = JSON.parse(sessionStorage.getItem('cart'))
  },
  methods: {
    getProducts() {
      
      axios({
        methods: 'get',
        url: 'http://127.0.0.1:8000/products/',
        auth: {
          username: 'amyyne',
          password: 'amyyne'
        }
      }).then(response => this.products = response.data)
    }
  }
}
</script>
