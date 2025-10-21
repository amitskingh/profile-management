from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib import messages



def login_user(request):
    if request.user.is_authenticated:
        if UserProfile.objects.filter(user=request.user).exists():
            return redirect('profile_view')
        else:
            return redirect('create_profile')


    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is None:
            messages.error(request, 'Invalid email or password')
            return render(request, 'user_profile/login.html')

        # Login successful
        login(request, user)


    return render(request, 'user_profile/login.html')



def register_user(request):

    if request.user.is_authenticated:
        if UserProfile.objects.filter(user=request.user).exists():
            return redirect('profile_view')
        else:
            return redirect('create_profile')

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')


        # Password match
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return render(request, 'user_profile/register.html')

        # Email exists
        if User.objects.filter(username=email).exists():
            messages.error(request, 'Email already exists')
            return render(request, 'user_profile/register.html')

        user = User.objects.create_user(
            username=email,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )

        user.save()

        messages.success(request, 'Account created successfully! Please login.')
        return redirect('login_user')
    
    # GET request
    return render(request, 'user_profile/register.html')



@login_required
def logout_user(request):
    logout(request)
    return redirect('login_user')