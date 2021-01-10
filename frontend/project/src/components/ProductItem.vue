<script>
export default {
    name: "ProductItem",
    props: {
        name: {
            type: String,
            required: true
        },
        description: {
            type: String,
            required: true
        },
        instock: {
            type: Boolean,
            required: true,
        },
        price: {
            type: Number,
            required: true
        },
        image: {
            type: String,
            required: false
        },
        discount: {
            type: Number,
            required: true
        }

    },
    data() {
        return {
        }
    },
    computed: {
        generatedPrice() {
            if(this.discount > 0) {
                return (this.price - (this.price* (this.discount/100)))
            } else {
                return this.price
            }
        }
    },
    methods: {
        addToCart() {
            var item = JSON.parse(sessionStorage.getItem('cart'))
            item.push({nom: this.name, description: this.description, prix: this.generatedPrice})
            sessionStorage.setItem('cart', JSON.stringify(item))
        }
    }
}
</script>

<template>
    <div>
        <div class="card" style="width: 18rem;">
        <img class="card-img-top" :src="image" alt="Card image cap">
            <div class="card-body">
                <h5 class="card-title">{{ name }}</h5>
                <p class="card-text">{{ description }}</p>
            </div>
            <ul class="list-group list-group-flush">
                <li class="list-group-item bg-success">Prix: {{ generatedPrice }} $ | remise: {{ discount }} %</li>
                <li class="list-group-item" v-if="instock">En Stock</li>
                <li class="list-group-item" v-else>En rupture de stock</li>
                <li class="list-group-item bg-danger">Prix Avant Remise: {{ price }} $</li>
            </ul>
            <div class="card-body">
                <a href="#" class="btn btn-primary" @click="addToCart()">ADD TO CART</a>
            </div>
        </div>
    </div>
</template>