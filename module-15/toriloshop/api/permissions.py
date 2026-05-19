from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission:
    - Anyone can read (GET, HEAD, OPTIONS) — SAFE_METHODS
    - Only the creator (created_by) can edit or delete
    
    This is an object-level permission — it runs after the view
    has fetched the specific product object.
    """
    
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        # SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
        if request.method in SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to the creator of the product
        # obj.created_by is the User who created this product
        return obj.created_by == request.user