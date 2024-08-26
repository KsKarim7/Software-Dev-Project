from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.DjangoModel),
    # path('django_form/',views.DjangoForm,name = 'django_form')
]