"""
URL configuration for server_api project.

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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.Signin,name='Signin'),
    path('upload_file', views.upload_file,name='upload_file'),
    path('check_details', views.check_details,name='check_details'),
    path('User_data', views.User_data.as_view()),
    path('User_data/<str:client_name>', views.User_data.as_view()),
    path('file_data', views.file_data.as_view()),
    path('file_data/<str:file_id>', views.file_data.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
