from django.urls import include, path
from rest_framework.routers import DefaultRouter
from tradenetwork.views import SupplierViewSet, ProductViewSet
from tradenetwork.apps import TradenetworkConfig

app_name = TradenetworkConfig.name

suppplier_router = DefaultRouter()
suppplier_router.register(r"supplier", SupplierViewSet, basename="supplier")

product_router = DefaultRouter()
product_router.register(r"product", ProductViewSet, basename="product")

urlpatterns = [
    path("", include(suppplier_router.urls)),
    path("", include(product_router.urls)),
]