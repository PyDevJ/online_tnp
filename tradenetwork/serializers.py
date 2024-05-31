from rest_framework import serializers
from tradenetwork.models import Product, Supplier
from tradenetwork.validators import SimultaneousSelectionValidator


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class SupplierSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, required=False)
    # Проверка на соответствие иерархической структуры
    validators = [
        SimultaneousSelectionValidator(network_level="network_level", supply="supply")
    ]

    class Meta:
        model = Supplier
        fields = "__all__"


class SupplierUpdateSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, required=False)
    validators = [
        SimultaneousSelectionValidator(network_level="network_level", supply="supply")
    ]

    class Meta:
        model = Supplier
        fields = "__all__"
        # запрет на обновление поля «Задолженность перед поставщиком»
        read_only_fields = [
            "debt_to_supplier"
        ]
