from django.db import models

# Create your models here.

class Product(models.Model):
    PRDName = models.CharField(max_length=100, verbose_name="Product Name")
    PRDCategory = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)
    PRDBrand = models.ForeignKey('settings.Brand', on_delete=models.CASCADE, blank=True, null=True)
    PRDDesc = models.TextField(verbose_name="Product Description")
    PRDPrice = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Price")
    PRDCost = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Cost")
    PRDDiscount = models.DecimalField(default=0, max_digits=2,decimal_places=0, verbose_name="Product Discount")
    PRDInstock = models.BooleanField(default=True, verbose_name="Product Stock")
    PRDCreated = models.DateTimeField(verbose_name="Created At")

    class Meta:
        verbose_name="Product"
        verbose_name_plural="Products"

    def __str__(self):
        return self.PRDName

class ProductImage(models.Model):
    PRDIproduct = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Product")
    PRDIImage = models.ImageField(upload_to="product/", verbose_name="Image")

    def __str__(self):
        return str(self.PRDIproduct)

class Category(models.Model):
    CATName = models.CharField(max_length=100, verbose_name="Category Name")
    CATParent = models.ForeignKey('self',limit_choices_to={'CATParent__isnull' : True}, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Category Parent")
    CATDesc = models.TextField(verbose_name="Category Description")
    CATImg = models.ImageField(upload_to='categry/', verbose_name="Category Image")

    class Meta:
        verbose_name="Category"
        verbose_name_plural="Categories"


    def __str__(self):
        return self.CATName
