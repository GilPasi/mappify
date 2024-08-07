"""
URL configuration for MappifyDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# urls.py
# This file defines the URL patterns for the Django project. It includes
# routes for the admin site, video upload, video list, video detail, and
# video deletion views.

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('mappify_server.api_urls')),  # Ensure this is pointing to the correct api_urls module
    path('', include('mappify_server.urls')),  # Include the app-level urls if they exist
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

