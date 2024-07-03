from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def primerpaso(request):
    return render (request,'primerpaso.html')

@login_required
def imagen_primerpaso(request):
    return render(request,'imagen_primerpaso.html')

@login_required
def presentacion_primerpaso(request):
    return render(request,'presentacion_primerpaso.html')

@login_required
def video_primerpaso(request):
    return render(request,'video_primerpaso.html')

@login_required
def formato_primerpaso(request):
    return render(request,'formato_primerpaso.html')