from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('image/', views.image, name='image'),
    path('selected_process/', views.execute_process, name='execute_process'),
]
