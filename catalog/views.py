from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # Below we set the logic such that anyone can read but only authenticated users can edit
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Key features: filtering and sorting
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # 1. Filtering by category '/api/products/?category=1'
    filterset_fields = ['category']

    #2. Sorting by price and creation date '/api/products/?ordering=price' '
    ordering_fields = ['price' 'created_at']

    #3. Searching by name and description '/api/products/?search=phone'
    search_fields = ['name', 'description']