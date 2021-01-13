<template>
  <div class="container mt-5">
    <table class="table table-striped">
      <thead>
        <tr>
          <th scope="col">Quantité</th>
          <th scope="col">Nom De Produit</th>
          <th scope="col">Description</th>
          <th scope="col">Prix(Unité)</th>
          <th scope="col"></th>
        </tr>
      </thead>
      <tbody v-for="item in cart" v-bind:key="item.nom">
        <tr>
          <th scope="row">{{ item.quantite }} <button @click="addQty(item)" class="btn btn-success btn-sm">+</button> <button @click="removeQty(item)" class="btn btn-danger btn-sm">-</button></th>
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
        totalPrice: 0,
      }
  },
  watch: {
    totalPrice() {
      this.totalPrice = 0
    },
  },
  computed: {
    getTotalPrice() {
      this.cart.map((item) => {
        this.totalPrice += item.prix * item.quantite
      })
      return this.totalPrice
    },
  },
  methods: {
    deleteItem(cartItem) {
      let changedCart = JSON.parse(sessionStorage.getItem('cart'))
      for (var key in changedCart) {
          if( changedCart[key].nom === cartItem.nom ) {
            changedCart.splice(key,1)
            sessionStorage.setItem('cart', JSON.stringify(changedCart))
            this.cart = JSON.parse(sessionStorage.getItem('cart'))
          }
      }
      return this.cart
    },
    addQty(item) {
      return item.quantite++
    },
    removeQty(item) {
      if( item.quantite <= 1 ) {
        item.quantite = 1
      } else {
        item.quantite--
      }
    }
  }
}
</script>


