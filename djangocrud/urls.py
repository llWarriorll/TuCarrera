"""
URL configuration for djangocrud project.

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
from django.contrib import admin
from django.urls import path
from users import views
from home import viewsh
from primerpaso import viewsp1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', viewsh.home, name='home'),
    path('aboutprogram/',viewsh.aboutprogram, name='aboutprogram'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('permission-denied/', views.permissiondenied, name='permission_denied'),
    path('homeadmin/', views.homeadmin, name='homeadmin'),
    path('homeuser/', views.homeuser, name='homeuser'),
    path('primerpaso/',viewsp1.primerpaso, name='primerpaso'),
    path('imagen-primer-paso/',viewsp1.imagen_primerpaso, name='imagen-primer-paso'),
    path('presentacion-primer-paso/',viewsp1.presentacion_primerpaso, name='presentacion-primer-paso'),
    path('video-primer-paso/',viewsp1.video_primerpaso, name='video-primer-paso'),
    path('formato-primer-paso/',viewsp1.formato_primerpaso, name='formato-primer-paso'),
    
    
    
]
