from django.contrib import admin

from products.models import ProductCategory, Product, Basket


admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'description', ('price', 'quantity'), 'image', 'category')
    search_fields = ('name',)
    ordering = ('name', )


class BasketAdmin(admin.TabularInline):
    model = Basket
    list_display = ('product', 'quantity')
