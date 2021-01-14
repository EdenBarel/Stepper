"""Ass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include

from vue_app import views as vue_views

from django.conf import settings
from django.conf.urls.static import static

from vue_app.views import MyFilesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
ter = routers.DefaultRouter()
router.register(r'my-files', MyFilesViewSet)

urlpatterns = [
    path('files/', include(router.urls)), #http://127.0.0.1:8000/files/my-files/
    path('admin/', admin.site.urls),      #http://127.0.0.1:8000/admin/
    path('vue-app/', include("vue_app.urls")),    #http://127.0.0.1:8000/vue-app/
    path('vanilla-app/', include("vanilla_app.urls")),    #http://127.0.0.1:8000/vanilla-app/
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
