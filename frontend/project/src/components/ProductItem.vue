<script>
export default {
	name: "ProductItem",
	props: {
		inStock: {
			type: Boolean,
			required: true
		},
		name: {
			type: String,
			required: true
		},
        description: {
            type: String,
            required: true
        },
		price: {
			type: Number,
			required: true
		},
        discount: {
            type: Number,
            required: true
        }
	},
}
</script>

<template>
	<div class="menu-item">
		<img class="menu-item__image" :src="image.source" :alt="image.alt" />
		<div>
			<h3>{{ name }}</h3>
			<p>
				Prix : {{ generatedPrice }}
				<span v-if="onSale">(10% de réduction !)</span>
			</p>
			<p v-if="inStock">En stock</p>
			<p v-else>En rupture de stock</p>
		</div>
	</div>
</template>

<style lang="scss">
.menu-item {
	display: flex;
	width: 500px;
	justify-content: space-between;
	margin-bottom: 30px;
	&__image {
		max-width: 300px;
	}
}
</style>