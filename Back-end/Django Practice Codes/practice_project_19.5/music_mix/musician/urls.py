from django.urls import path,include
from . import views
from musician.views import add_musician, edit_musician


urlpatterns = [
    path('add/',views.add_musician,name='add_musician'),
    path('edit/<int:id>', edit_musician, name="edit_musician"),
    path('delete/<int:id>',views.delete_musician,name='delete_musician')

]
