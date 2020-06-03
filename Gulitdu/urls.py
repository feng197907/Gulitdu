"""Gulitdu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import xadmin
from django.conf import settings
from django.views.static import serve
from users.views import index

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('courses/', include(('courses.urls', 'courses'), namespace='courses')),
    path('orgs/', include(('orgs.urls', 'orgs'), namespace='orgs')),
    path('operations/', include(('operations.urls', 'operations'), namespace='operations')),
    path('', index, name='index')
]
