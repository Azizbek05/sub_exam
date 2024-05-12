from django.contrib import admin
from .models import Products, Category

# Register your models here.
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'price', 'description')
    class Meta:
        model = Products
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'image')