from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count, Q  # Add Q for complex queries
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from .models import Product, Category
from .forms import ProductForm, CategoryForm
from django.http import HttpResponse 


def home(request):
    """Home page with featured products"""
    featured_products = Product.objects.filter(stock__gt=0)[:6]
    categories = Category.objects.annotate(product_count=Count('products'))[:4]
    context = {
        'featured_products': featured_products,
        'categories': categories,
    }
    return render(request, 'products/home.html', context)


def product_list(request):
    """Display all products with optional search filtering"""
    
    # Get the search query from the URL parameters
    search_query = request.GET.get('search', '')
    
    # Start with all products
    products = Product.objects.all().select_related('category')
    
    # Apply search filter if a query exists
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |           # Search by product name
            Q(description__icontains=search_query) |    # Search in description
            Q(category__name__icontains=search_query)   # Search by category name
        )
    
    context = {
        'products': products,
        'search_query': search_query,  # Pass back to template to keep the search box filled
    }
    return render(request, 'products/product_list.html', context)


def product_detail(request, pk):
    """Display single product details"""
    try:
        product = get_object_or_404(Product.objects.select_related('category'), pk=pk)
    except:
        # If product doesn't exist, redirect to product list
        from django.shortcuts import redirect
        return redirect('product_list')
    
    context = {'product': product}
    return render(request, 'products/product_detail.html', context)


def category_list(request):
    """Display all categories with product counts"""
    categories = Category.objects.annotate(product_count=Count('products'))
    context = {'categories': categories}
    return render(request, 'products/category_list.html', context)


def about(request):
    """About page"""
    context = {
        'total_products': Product.objects.count(),
        'total_categories': Category.objects.count(),
    }
    return render(request, 'products/about.html', context)


# Bonus:Custom 404 Handler
def custom_404(request, exception):
  content = '''
      <h1>404 - Page Not Found</h1>
      <p>Sorry, the page you are looking for does not exist on ToriloShop.</p>
      <a href="/"><- Return to Home</a>  
  '''
  return HttpResponse(content, status=404)    

# ---------- PRODUCT CRUD ----------
@login_required
def product_create(request):
    """
    Handle creation of new products.
    GET: Display empty form.
    POST: Validate and save form data.
    """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, f'✅ Product "{product.name}" was created successfully!')
            return redirect('product_list')
        else:
            messages.error(request, '❌ Please correct the errors below.')
    else:
        form = ProductForm()
    
    context = {
        'form': form,
        'title': 'Add New Product',
        'submit_text': 'Create Product',
    }
    return render(request, 'products/product_form.html', context)


@login_required
def product_update(request, pk):
    """
    Handle editing of existing products.
    GET: Display form pre-filled with product data.
    POST: Validate and update the product.
    """
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            updated_product = form.save()
            messages.success(request, f'✅ Product "{updated_product.name}" was updated successfully!')
            return redirect('product_detail', pk=product.pk)
        else:
            messages.error(request, '❌ Please correct the errors below.')
    else:
        form = ProductForm(instance=product)
    
    context = {
        'form': form,
        'product': product,
        'title': f'Edit Product: {product.name}',
        'submit_text': 'Update Product',
    }
    return render(request, 'products/product_form.html', context)


@login_required
def product_delete(request, pk):
    """
    Handle deletion of products.
    GET: Display confirmation page.
    POST: Delete the product and redirect.
    """
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        product_name = product.name
        product.delete()
        messages.success(request, f'🗑️ Product "{product_name}" was deleted successfully!')
        return redirect('product_list')
    
    context = {
        'product': product,
        'title': f'Delete Product: {product.name}',
    }
    return render(request, 'products/product_confirm_delete.html', context)


# ---------- CATEGORY CRUD ----------

@login_required
def category_create(request):
    """
    Handle creation of new categories.
    """
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            messages.success(request, f'✅ Category "{category.name}" was created successfully!')
            return redirect('category_list')
        else:
            messages.error(request, '❌ Please correct the errors below.')
    else:
        form = CategoryForm()
    
    context = {
        'form': form,
        'title': 'Add New Category',
        'submit_text': 'Create Category',
    }
    return render(request, 'products/category_form.html', context)


@login_required
def category_update(request, pk):
    """
    Handle editing of existing categories.
    """
    category = get_object_or_404(Category, pk=pk)
    
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            updated_category = form.save()
            messages.success(request, f'✅ Category "{updated_category.name}" was updated successfully!')
            return redirect('category_list')
        else:
            messages.error(request, '❌ Please correct the errors below.')
    else:
        form = CategoryForm(instance=category)
    
    context = {
        'form': form,
        'category': category,
        'title': f'Edit Category: {category.name}',
        'submit_text': 'Update Category',
    }
    return render(request, 'products/category_form.html', context)


@login_required
def category_delete(request, pk):
    """
    Handle deletion of categories.
    GET: Display confirmation page with warning about affected products.
    POST: Delete the category and redirect.
    """
    category = get_object_or_404(Category, pk=pk)
    product_count = category.products.count()
    
    if request.method == 'POST':
        category_name = category.name
        category.delete()
        messages.success(request, f'🗑️ Category "{category_name}" and all its products were deleted.')
        return redirect('category_list')
    
    context = {
        'category': category,
        'product_count': product_count,
        'title': f'Delete Category: {category.name}',
    }
    return render(request, 'products/category_confirm_delete.html', context)


 