from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('login/')),  # Redirect root to login
     path('admin/', admin.site.urls),
    path('', include('records.urls')),
    
]
