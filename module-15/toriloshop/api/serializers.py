from rest_framework import serializers
from products.models import Product, Category
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """Simple serializer to show user info in product responses"""
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model.
    Includes a computed product_count field using SerializerMethodField.
    """
    
    # SerializerMethodField lets you add a computed/read-only field
    # The method must be named get_<field_name>
    product_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'product_count', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
    
    def get_product_count(self, obj):
        """
        Return the number of products in this category.
        obj is the Category instance being serialized.
        """
        return obj.products.count()


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model.
    
    Handles:
    - Nested category object in responses (read_only)
    - category_id for creating/updating products (write_only)
    """
    
    # Nested serializer - shows full category object in GET responses
    # read_only=True means this field is output only, not used for input
    category = CategorySerializer(read_only=True)
    
    # Accepts a category ID when creating or updating a product
    # write_only=True means it's only used for input, not shown in output
    # source='category' links this field to the category ForeignKey
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True
    )

    # NEW: Show who created the product (read only)
    created_by = UserSerializer(read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'price', 'stock',
            'is_available', 'image', 'category', 'category_id', 'created_by', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at', 'created_by']