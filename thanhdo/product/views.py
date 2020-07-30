from django.shortcuts import render
from rest_framework import viewsets
from product.models import Carrier, Customer, Category, Product
from product.serializers import (
    CarrierSerializer,
    ProductSerializer,
    CategorySerializer,
)
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

# class CarrierViewSet(viewsets.ModelViewSet):
#     # queryset=Carrier.objects.all()
#     # serializer_class = CarrierSerliazer
class CarrierViewSet(viewsets.ViewSet):
    # queryset=Carrier.objects.all()
    # serializer_class = CarrierSerliazer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        carrier = Carrier.objects.all()
        serializer = CarrierSerializer(carrier, many=True, context={"request": request})
        response_dict = {
            "error": False,
            "message": "All Carrier List Data",
            "data": serializer.data,
        }
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = CarrierSerializer(
                data=request.data, context={"request": request}
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {
                "error": False,
                "message": "Carrier Data Save Successfully",
            }
        except:
            dict_response = {
                "error": True,
                "message": "Error During Saving Carrier Successfully",
            }
        return Response(dict_response)

    def update(self, request, pk=None):
        try:
            queryset = Carrier.objects.all()
            carrier = get_object_or_404(queryset, pk=pk)
            serializer = CarrierSerializer(
                carrier, data=request.data, context={"request": request}
            )
            serializer.is_valid()
            serializer.save()
            dict_response = {
                "error": False,
                "message": "Carrier Data updated Successfully",
            }
        except:
            dict_respomse = {
                "error": True,
                "message": "Error During Updating Carrier Data",
            }
        return Response(dict_response)


carrier_list = CarrierViewSet.as_view({"get": "list"})
carrier_creat = CarrierViewSet.as_view({"post": "create"})
carrier_creat = CarrierViewSet.as_view({"put": "update"})


class CategoryViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        carrier = Category.objects.all()
        serializer = CategorySerializer(
            Category, many=True, context={"request": request}
        )
        response_dict = {
            "error": False,
            "message": "All Category List Data",
            "data": serializer.data,
        }
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = CategorySerializer(
                data=request.data, context={"request": request}
            )
            serializer.is_valid()
            serializer.save()
            dict_response = {
                "error": False,
                "message": "Category Account Data Save Successfully",
            }
        except:
            dict_response = {
                "error": True,
                "message": "Error During Saving Carrier Account Successfully",
            }
        return Response(dict_response)


class ProductViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True, context={"request": request})
        response_dict = {
            "error": False,
            "message": "All Category List Data",
            "data": serializer.data,
        }
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = ProductSerializer(
                data=request.data, context={"request": request}
            )
            serializer.is_valid()
            serializer.save()
            print(serializer)
            dict_response = {
                "error": False,
                "message": "Carrier Account Data Save Successfully",
            }
        except:
            dict_response = {
                "error": True,
                "message": "Error During Saving Carrier Account Successfully",
            }
        return Response(dict_response)

    def retrieve(self, request, pk=None):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(product, context={"request": request})
        return Response(
            {"error": False, "message": "Single Data Fetch", "data": serializer.data}
        )

    def update(self, request, pk=None):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(
            product, data=request.data, context={"request": request}
        )
        serializer.is_valid()
        serializer.save()
        return Response({"error": False, "message": "Data Has Been Updated"})


class CarrierNameViewSet(generics.ListAPIView):
    serializer_class = CarrierSerializer

    def get_queryset(self):
        name = self.kwargs["name"]
        return Carrier.objects.filter(name=name)
