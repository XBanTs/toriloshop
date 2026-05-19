from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import CustomUserCreationForm

# Create your views here.

def register(request):
    """
    Handle user registration.
    GET: Display empty registration form.
    POST: Validate form, create user, log them in, redirect to home.
    """
    # If user is already logged in, redirect to home
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Save the new user to the database
            user = form.save()
            # Automatically log in the new user
            login(request, user)
            messages.success(request, f'✅ Welcome, {user.username}! Your account has been created.')
            return redirect('home')
        else:
            messages.error(request, '❌ Please correct the errors below.')
    else:
        form = CustomUserCreationForm()
    
    context = {
        'form': form,
        'title': 'Create an Account',
    }
    return render(request, 'accounts/register.html', context)
