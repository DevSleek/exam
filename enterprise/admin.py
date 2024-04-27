from django.contrib import admin

from enterprise.models import Product, Material, ProductMaterial, Warehouse


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name',)


admin.site.register(Product, ProductAdmin)


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Material, MaterialAdmin)


class ProductMaterialAdmin(admin.ModelAdmin):
    list_display = ('product', 'material', 'quantity')
    search_fields = ('product',)


admin.site.register(ProductMaterial, ProductMaterialAdmin)


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('material', 'remainder', 'price')
    search_fields = ('material', 'price',)


admin.site.register(Warehouse, WarehouseAdmin)