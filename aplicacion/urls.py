from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'), 
    path('register/', views.register_view, name='register'),
    path('password_reset/', views.password_reset_view, name='password_reset'),
    # ... otras rutas ...
]

