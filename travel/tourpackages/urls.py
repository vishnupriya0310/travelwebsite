from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('',views.homepage, name = 'home1'),
    path('flights/',views.flights, name = 'flights'),
    path('rentcar/', views.rentcar, name = 'rentcar'),
    path('travelpackages/', views.travelpackages, name = 'travelpackages'),
    path('register/', views.register, name = 'register1'),
    path('login1/', views.login1, name = 'login1'),
    path('alllink/', views.alllink, name = 'alllink'),
    path('date1/', views.date1, name = 'date1'),
    path('randomotp/', views.randomotp, name = 'randomotp'),
    path('randomotp1/', views.randomotp1, name='randomotp1'),
    path('getdate/', views.get_date, name='get_date'),
    path('getdate1/', views.getdate1, name='getdate1'),
    path('getdate2/', views.getdate2, name='getdate2'),
    path('print/', views.print_to_console, name='print_to_console'),
    path('p/', views.print1, name='print1'),
    path('popup/', views.my_view, name='popup_view'),
    path('register/', views.register, name='register'),
    path('login2/',views.user_login,name = 'login2'),
    # path('login1/', views.login, name='login'),
    path('logout/', views.user_logout, name='logout'),


    ]
