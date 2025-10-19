from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile




def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)

            if UserProfile.objects.exists(request.user):
                return redirect('/profile/')
            else:
                return redirect('/create_profile/')
        

        
    return render(request, 'user_profile/login.html')


def register_user(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        print(first_name, last_name, email, password, confirm_password)

        user = User.objects.create_user(username=email, first_name=first_name, last_name=last_name, email=email, password=password)

        user.save()

        return redirect('/login/')
    
    return render(request, 'user_profile/register.html')



@login_required
def logout_user(request):
    logout(request)
    return redirect('/login/')