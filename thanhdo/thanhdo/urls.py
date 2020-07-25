"""thanhdo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from thanhdo import settings
from rest_framework import routers
from product import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


routers = routers.DefaultRouter()
routers.register("carrier", views.CarrierViewSet, basename="carrier")
routers.register("product", views.ProductViewSet, basename="product")
routers.register("category", views.CategoryViewSet, basename="category")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(routers.urls)),
    path("api/gettoken/", TokenObtainPairView.as_view(), name="gettoken"),
    path("api/refresh_token/", TokenRefreshView.as_view(), name="refresh_token"),
    path("", include("home.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

