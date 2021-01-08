from django.contrib import admin

# Register your models here.
from .models import Product, ProductImage, Category



admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Category)
