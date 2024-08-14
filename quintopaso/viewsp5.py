from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

@login_required
def quintopaso(request):
    return render (request,'quintopaso.html')

@login_required
def mis_apoyos_s2(request):
    return render (request,'mis_apoyos_s2.html')

@login_required
def mis_apoyos_s3(request):
    return render (request,'mis_apoyos_s3.html')

@login_required
def imagen_quintopaso(request):
    return render (request,'imagen_quintopaso.html')

@login_required
def tablero_quintopaso(request):
    return render (request,'tablero_quintopaso.html')