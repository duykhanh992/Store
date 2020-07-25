from rest_framework import serializers
from .models import Carrier, Product, Category


class CarrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrier
        # fields=['name','address','phone_no']
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
