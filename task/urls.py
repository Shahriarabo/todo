from django.urls import path
from . import views

urlpatterns = [
    path('', views.index ),
    path('edit/<int:task_id>', views.edit,), 
    path('delete/<int:task_id>', views.delete ),
]