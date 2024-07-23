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
from segundopaso import viewsp2
from tercerpaso import viewsp3

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
    path('mis-intereses-s2/',viewsp1.primerpasos2, name='mis-intereses-s2'),
    path('infografia-primer-paso/',viewsp1.infografia_primerpaso, name='infografia-primer-paso'),
    path('test-primer-paso/',viewsp1.test_primerpaso, name='test-primer-paso'),
    path('segundopaso/',viewsp2.segundopaso,name='segundopaso'),
    path('mis-talentos-s2/',viewsp2.segundopaso2,name='mis-talentos-s2'),
    path('frase-segundo-paso/',viewsp2.frase_segundopaso,name='frase-segundo-paso'),
    path('presentacion-segundo-paso/',viewsp2.presentacion_segundopaso,name='presentacion-segundo-paso'),
    path('test-segundo-paso',viewsp2.test_segundopaso,name='test-segundo-paso'),
    path('instrucciones-test-segundo-paso/',viewsp2.instruccionestest_segundopaso,name='instrucciones-test-segundo-paso'),
    path('tercerpaso/',viewsp3.tercerpaso, name='tercer-paso'),
    path('infografia-tercer-paso/',viewsp3.infografia_tercerpaso, name='infografia-tercer-paso'),
    path('mi-entorno-s2/',viewsp3.mi_entorno_s2, name='mi-entorno-s2'),
    path('tablero-interactivo-tercer-paso/',viewsp3.tablero_tercerpaso, name='tablero-interactivo-tercer-paso'),
    path('video-tercer-paso/',viewsp3.video_tercerpaso, name='video-tercer-paso'),
    path('mi-entorno-s3/',viewsp3.mi_entorno_s3, name='mi-entorno-s3'),
    path('video-consejo-tercer-paso/',viewsp3.video_consejo_tercerpaso, name='video-consejo-tercer-paso'),

    
]
