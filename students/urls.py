from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.student , name='student'),  
    path('checkout/', views.checkout, name='checkout'),  
    path('carousel/', views.carousel, name='carousel'),  
    path('carousel2/', views.carousel2, name='carousel2'),  
    path('footballer/', views.footballer, name='footballer'),  
    path('check_footballers/', views.check_footballers, name='check_footballers'),  
]

