# myproject/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AVNRSystem.urls')),  # Include the URLs from your 'myapp' app
]

