"""
URL configuration for safahermandad project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from safahermandad import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hermandapp.urls')),
    path('hermandad/', include('hermandapp.urls')),
    path("__reload__/", include("django_browser_reload.urls")),

    #Cargar css en modo debug=False
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.STATIC_URL}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_URL}),
]
