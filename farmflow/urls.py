from django.contrib import admin
from django.urls import path
from marketplace import views
from django.contrib import admin
from django.urls import path
from marketplace import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('register/farmer/', views.register,
         {'user_type': 'farmer'}, name='farmer_register'),

    path('register/buyer/', views.register,
         {'user_type': 'buyer'}, name='buyer_register'),
]
