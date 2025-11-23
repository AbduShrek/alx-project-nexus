# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.request import Request # to fix request.query_params warnings

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by("name") # TODO: later show only active categories by default
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]  # TODO: later we can restrict for writes


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related("category").all().order_by("name")
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]  # TODO: later: IsAuthenticatedOrReadOnly

    request: Request #to fix request.query_params warnings

    # Enable search & ordering (DRF global filter backends use these)
    search_fields = ["name", "slug", "sku", "description"]
    ordering_fields = ["name", "price", "created_at"]


    def get_queryset(self):
        queryset = super().get_queryset()

        # Filtering by query params
        category_id = self.request.query_params.get("category_id")
        min_price = self.request.query_params.get("min_price")
        max_price = self.request.query_params.get("max_price")
        is_active = self.request.query_params.get("is_active", "true")

        if category_id:
            queryset = queryset.filter(category_id=category_id)

        if min_price:
            queryset = queryset.filter(price__gte=min_price)

        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        if is_active.lower() in ["true", "1", "yes"]:
            queryset = queryset.filter(is_active=True)
        elif is_active.lower() in ["false", "0", "no"]:
            queryset = queryset.filter(is_active=False)

        return queryset