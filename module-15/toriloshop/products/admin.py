from django.contrib import admin
from .models import Category, Product

# Register your models here.
# admin.site.register(Category)
# admin.site.register(Product)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Custom admin for Category model"""
    list_display = ['name', 'description', 'product_count', 'created_at']
    search_fields = ['name', 'description']
    list_filter = ['created_at']
    
    def product_count(self, obj):
        """Show number of products in this category"""
        return obj.products.count()
    product_count.short_description = 'Products'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Custom admin for Product model with enhanced management features"""
    
    # Columns displayed in the product list
    list_display = [
        'name', 
        'category', 
        'price', 
        'stock', 
        'is_available',
        'image_preview',
        'created_at'
    ]
    
    # Search box - searches these fields
    # Use double underscore to search related model fields
    search_fields = ['name', 'description', 'category__name']
    
    # Sidebar filters
    list_filter = ['category', 'is_available', 'created_at']
    
    # Fields that can be edited directly in the list view
    list_editable = ['price', 'stock', 'is_available']
    
    # Default sorting (newest first)
    ordering = ['-created_at']
    
    # Number of items per page
    list_per_page = 20
    
    # Registered custom bulk actions
    actions = ['mark_out_of_stock', 'mark_in_stock']
    
    # Organise fields in the edit form
    fieldsets = (
        ('Product Information', {
            'fields': ('name', 'category', 'description')
        }),
        ('Pricing & Inventory', {
            'fields': ('price', 'stock', 'is_available')
        }),
        ('Product Image', {
            'fields': ('image',),
            'description': 'Upload a clear product image. Recommended size: 800x800 pixels.'
        }),
    )
    
    def image_preview(self, obj):
        """Show a small thumbnail in the admin list"""
        if obj.image:
            return f'✅'
        return '❌'
    image_preview.short_description = 'Image'
    
    # Custom Admin Actions
    
    def mark_out_of_stock(self, request, queryset):
        """
        Bulk action: Set selected products to out of stock.
        queryset contains all the rows the user selected.
        """
        updated = queryset.update(stock=0, is_available=False)
        self.message_user(
            request, 
            f'{updated} product(s) marked as out of stock.'
        )
    mark_out_of_stock.short_description = 'Mark selected as out of stock'
    
    def mark_in_stock(self, request, queryset):
        """
        Bulk action: Set selected products to in stock with 10 units.
        """
        updated = queryset.update(stock=10, is_available=True)
        self.message_user(
            request,
            f'{updated} product(s) marked as in stock (10 units).'
        )
    mark_in_stock.short_description = 'Mark selected as in stock (10 units)'
