# catalog/views.py

from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
# Import IsAdminUser for explicit admin checks
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # Standard permissions for categories (keeping it simple for now)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # Key features: filtering and sorting
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category']
    ordering_fields = ['price', 'created_at']
    search_fields = ['name', 'description']

    # -------------------------------------------------------------
    # Custom Permission Logic
    # -------------------------------------------------------------
    def get_permissions(self):
        """
        Custom permission logic:
        - Read actions (list, retrieve) are public (AllowAny).
        - Write actions (create, update, destroy) require admin status (IsAdminUser).
        """
        if self.action in ['list', 'retrieve']:
            # Allow everyone (unauthenticated or authenticated) to view products
            permission_classes = [AllowAny]
        else:
            # Require admin for POST, PUT, PATCH, DELETE operations
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]