from rest_framework import serializers

from enterprise.models import Product, Material, ProductMaterial, Warehouse


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('name',)


class MaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Material
        fields = ('name',)


class ProductMaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductMaterial
        fields = ('product', 'material', 'quantity')


class WarehouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Warehouse
        fields = ('material', 'remainder', 'price')


class RequestSerializer(serializers.Serializer):
    product = serializers.CharField()
    quantity = serializers.IntegerField()


class ResultSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField()
    product_materials = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'name',
            'quantity',
            'product_materials'
        )

    @staticmethod
    def get_product_materials(obj):

        result = []
        quantity = obj.quantity

        for material in obj.product_material.all():
            warehouses = Warehouse.objects.filter(material__id=material.id)

            name = material.material.name
            limit = round((int(quantity) * material.quantity), 4)

            for warehouse in warehouses:

                price = warehouse.price
                if limit > warehouse.remainder:
                    qty = warehouse.remainder
                    limit = limit - qty
                else:
                    qty = limit

                result.append({
                    'warehouse_id': warehouse.id,
                    'material_name': name,
                    'qty': qty,
                    'price': price,
                })

        return result

