from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from products.models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from .permissions import IsOwnerOrReadOnly


# ============================================
# PRODUCT API VIEWS
# ============================================

class ProductListCreateAPIView(generics.ListCreateAPIView):
    """
    GET /api/products/ — List all products (paginated)
    POST /api/products/ — Create a new product
    
    ListCreateAPIView handles:
    - GET: Returns queryset as JSON (supports pagination)
    - POST: Validates input, creates product, returns 201

    Filtering:
    - ?category=1 — filter by category ID
    - ?is_available=true — filter by availability
    - ?search=laptop — search by name or category name
    - ?ordering=price or ?ordering=-price — sort by price (asc/desc)
    - ?ordering=-created_at — sort by newest first
    """
    queryset = Product.objects.all().select_related('category', 'created_by')
    serializer_class = ProductSerializer

     # Filtering, search, and ordering fields
    filterset_fields = ['category', 'is_available']
    search_fields = ['name', 'description', 'category__name']
    ordering_fields = ['price', 'stock', 'created_at', 'name']
    ordering = ['-created_at']  # Default: newest first
    
    def get_permissions(self):
        """
        GET requests are public.
        POST requests require authentication.
        """
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]
    
    def perform_create(self, serializer):
        """
        Automatically set the created_by field to the current user
        when a product is created via POST.
        """
        serializer.save(created_by=self.request.user)



class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET /api/products/<pk>/ — Retrieve a single product
    PUT /api/products/<pk>/ — Full update of a product
    PATCH /api/products/<pk>/ — Partial update (not explicitly used but supported)
    DELETE /api/products/<pk>/ — Delete a product
    
    RetrieveUpdateDestroyAPIView handles:
    - GET: Returns a single product as JSON
    - PUT: Replaces the entire product
    - PATCH: Updates only the provided fields
    - DELETE: Removes the product, returns 204 No Content
    """
    queryset = Product.objects.all().select_related('category', 'created_by')
    serializer_class = ProductSerializer

    def get_permissions(self):
        """
        GET is public.
        PUT and DELETE require authentication AND ownership.
        """
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        # For PUT and DELETE: must be authenticated AND be the creator
        return [permissions.IsAuthenticated(), IsOwnerOrReadOnly()]



# ============================================
# CATEGORY API VIEWS
# ============================================

class CategoryListAPIView(generics.ListAPIView):
    """
    GET /api/categories/ — List all categories with product counts
    
    ListAPIView handles:
    - GET: Returns queryset as JSON (supports pagination)
    
    Note: This is read-only. The assignment only requires GET for categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]