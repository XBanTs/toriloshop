from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """
    ModelForm for creating and updating Product instances.
    Django automatically generates fields based on the model.
    """
    
    class Meta:
        model = Product
        fields = ['name', 'category', 'description', 'price', 'stock', 'image', 'is_available']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter product name'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter product description'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0'
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0',
                'min': '0'
            }),
             # File input widget for image upload
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
        }
        labels = {
            'name': 'Product Name',
            'category': 'Category',
            'description': 'Description',
            'price': 'Price (₦)',
            'stock': 'Stock Quantity',
            'image': 'Product Image',
            'is_available': 'Available for Sale',
        }
    
    def clean_price(self):
        """
        Custom validation: Price must be greater than 0.
        This method runs automatically when form.is_valid() is called.
        """
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price
    
    def clean_stock(self):
        """
        Custom validation: Stock cannot be negative.
        """
        stock = self.cleaned_data.get('stock')
        if stock is not None and stock < 0:
            raise forms.ValidationError("Stock cannot be negative.")
        return stock


class CategoryForm(forms.ModelForm):
    """
    ModelForm for creating and updating Category instances.
    """
    
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter category name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter category description (optional)'
            }),
        }
        labels = {
            'name': 'Category Name',
            'description': 'Description',
        }
    
    def clean_name(self):
        """
        Custom validation: Category name must be unique (case-insensitive).
        """
        name = self.cleaned_data.get('name')
        if name:
            # Check for existing category with same name (case-insensitive)
            existing = Category.objects.filter(name__iexact=name)
            if self.instance.pk:
                existing = existing.exclude(pk=self.instance.pk)
            if existing.exists():
                raise forms.ValidationError("A category with this name already exists.")
        return name