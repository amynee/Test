<template>
	<div>
		<h1>Nom</h1>
		<p class="description">
			Bienvenue dans notre café ! Nous sommes réputés pour
			notre pain et nos merveilleuses pâtisseries. Faites vous plaisir dès le
			matin ou avec un goûter réconfortant. Mais attention, vous verrez qu'il
			est difficile de s'arrêter.
		</p>

		<section class="menu">
			<h2>Menu</h2>
			<ProductItem
				v-for="product in products"
				:name="product.PRDName"
                :description="product.PRDDesc"
				:price="product.PRDPrice"
                :discount="product.PRDDiscount"
				:inStock="product.PRDInstock"
				:key="product.id"
			/>
		</section>
	</div>
</template>

<script>
import axios from 'axios'
import ProductItem from "../components/ProductItem"
export default {
	name: "Home",
	components: {
		ProductItem
	},
    data() {
        return {
            products: []
        }
    },
    mounted() {
        this.getTasks()
    },
    methods: {
        getTasks() {
            axios({
                method: 'get',
                url: 'https://127.0.0.1:8000/products/',
                auth: {
                    username: 'amyyne',
                    password: 'amyyne',
                }
            }).then(response => this.products = response.data)
        }
    }
}
</script>

<style lang="scss">
.description {
	max-width: 960px;
	font-size: 1.2rem;
	margin: 0 auto;
}
.footer {
	font-style: italic;
	text-align: center;
}
.menu {
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
}
.shopping-cart {
	position: absolute;
	right: 30px;
	top: 0;
}
</style>
