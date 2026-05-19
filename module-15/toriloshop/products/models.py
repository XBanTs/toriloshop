from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  # Import User model


class Category(models.Model):
    """Product category model - represents product groupings"""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    """Product model - individual items for sale"""
    name = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'  # This enables category.products.all()
    )
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    # NEW: Image field for product photos
    # upload_to='products/' saves files in MEDIA_ROOT/products/
    # blank=True makes it optional in forms
    # null=True allows NULL in the database
    image = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True,
        help_text='Upload a product image'
    )

    # Helper field for admin and templates
    is_available = models.BooleanField(default=True)

     # NEW: Track who created this product
    # on_delete=models.CASCADE means if the user is deleted, their products are also deleted
    # related_name='created_products' lets us do user.created_products.all()
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='created_products',
        null=True,  # Allow null for existing products
        blank=True
    )

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']  # Newest first

    def __str__(self):
        return self.name

    def is_in_stock(self):
        """Helper method to check if product has stock"""
        return self.stock > 0
    
     # NEW: Property to automatically update availability based on stock
    def save(self, *args, **kwargs):
        if self.stock <= 0:
            self.is_available = False
        else:
            self.is_available = True
        super().save(*args, **kwargs)