from django.urls import path
from . import auth_views, views

urlpatterns = [
    path('login/', auth_views.login_user, name='login_user'),
    path('register/', auth_views.register_user, name='register_user'),
    path('logout/', auth_views.logout_user, name='logout_user'),
    path('profile/', views.profile_view, name='profile_view'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('create_profile/', views.create_profile, name='create_profile')
]
