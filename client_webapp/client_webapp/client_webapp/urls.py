"""
URL configuration for client_webapp project.

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
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.load_index,name='load_index'),
    path('Signin', views.Signin,name='Signin'),
    path('Signup', views.Signup,name='Signup'),
    path('download', views.download,name='download'),
    path('downlaod_file', views.downlaod_file,name='downlaod_file'),
    path('create_user', views.create_user,name='create_user'),
    path('check_details', views.check_details,name='check_details'),
]
