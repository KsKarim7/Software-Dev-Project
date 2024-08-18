from django.urls import path,include
from . import views

urlpatterns = [
    path('kids/',views.kids),
    path('mens/',views.mens),
    path('womens/',views.womens),
]