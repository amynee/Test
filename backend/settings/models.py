from django.db import models

# Create your models here.

class Brand(models.Model):
    BRDName = models.CharField(max_length=100, verbose_name="Brand Name")
    BRDDesc = models.TextField(blank=True, null=True, verbose_name="Brand Description")

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    def __str__(self):
        return self.BRDName

class Variant(models.Model):
    VARName = models.CharField(max_length=100, verbose_name="Variant Name")
    VARDesc = models.TextField(blank=True, null=True, verbose_name="Variant Description") 

    class Meta:
        verbose_name = "Variant"
        verbose_name_plural = "Variants"

    def __str__(self):
        return self.VARName