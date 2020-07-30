from rest_framework import serializers
from product.models import (
    Bill,
    BillDetails,
    Carrier,
    CarrierAccount,
    CarrierBank,
    Category,
    Customer,
    CustomerRequest,
    Employee,
    EmployeeBank,
    EmployeeSalary,
    Product,
    ProductDetails,
)


class CarrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrier
        # fields=['name','address','phone_no']
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["carrier"] = CarrierSerializer(instance.carrier_id).data
        return response


class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetails
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["product"] = ProductSerializer(instance.product_id).data
        return response


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["customer"] = CustomerSerializer(instance.employee_id).data
        return response


class EmployeeSalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeSalary
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["employee"] = EmployeeSerializer(instance.customer_id).data
        return response


class BillDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillDetails
        fields = "__all__"


class CustomerRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerRequest
        fields = "__all__"


class CarrierAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarrierAccount
        fields = "__all__"


class CarrierBankSerializer(serializers.ModelSerializer):
    class Meata:
        model = CarrierBank
        fields = "__all__"


class EmployeeBankSerializer(serializers.ModelSerializer):
    model = EmployeeBank
    fields = "__all__"

