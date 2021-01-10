<template>
  <div class="container mt-5">
    <table class="table table-striped">
      <thead>
        <tr>
          <th scope="col">Paniers</th>
          <th scope="col">Nom De Produit</th>
          <th scope="col">Description</th>
          <th scope="col">Prix</th>
          <th scope="col"></th>
        </tr>
      </thead>
      <tbody v-for="item in cart" v-bind:key="item.nom">
        <tr>
          <th scope="row">1</th>
          <td>{{ item.nom }}</td>
          <td>{{ item.description }}</td>
          <td>{{ item.prix }}</td>
          <td><button type="button" class="btn btn-danger" @click="deleteItem(item)">Supprimer</button><td/>
        </tr>
      </tbody>
      <tfoot class="bg-info">
        <tr>
          <th scope="row">All</th>
            <td colspan="2">Prix Total</td>
            <td>{{ getTotalPrice }}</td>
        </tr>
      </tfoot>
    </table>
  </div>
</template>

<script>
export default {
  name: 'Cart',
  data() { 
      return {
        cart: JSON.parse(sessionStorage.getItem('cart')),
        totalPrice: 0
      }
  },
  computed: {
    getTotalPrice() {
      this.cart.map((item) => {
        this.totalPrice += item.prix
      })
    return this.totalPrice
    }
  },
  methods: {
  }
}
</script>


