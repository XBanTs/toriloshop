from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

urlpatterns = [
    # ============================================
    # Token Authentication Endpoints
    # ============================================
    
    # DRF built-in token auth
    # POST username + password → returns {"token": "abc123..."}
    path('token/', obtain_auth_token, name='api_token_auth'),
    
    # JWT endpoints
    # POST username + password → returns {"access": "...", "refresh": "..."}
    path('token/jwt/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # POST refresh token → returns {"access": "..."}
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  
    # Product endpoints
    path(
        'products/',
        views.ProductListCreateAPIView.as_view(),
        name='api_product_list'
    ),
    path(
        'products/<int:pk>/',
        views.ProductDetailAPIView.as_view(),
        name='api_product_detail'
    ),
    
    # Category endpoints
    path(
        'categories/',
        views.CategoryListAPIView.as_view(),
        name='api_category_list'
    ),
]