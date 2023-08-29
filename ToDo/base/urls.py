from django.urls import path
from .views import *            # * imports all urls defined in views

urlpatterns = [
    path('home/',home, name='home'),
    path('create/',create, name = 'create'),
    path('edit/<int:pk>/',edit, name = 'edit'),
    path('delete/<int:id>/',delete, name = 'delete'),
    path('deleteall/<int:id>/',deleteall, name = 'deleteall'),
]