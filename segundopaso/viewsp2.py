from django.shortcuts import render
from django.contrib.auth.decorators import login_required



@login_required
def segundopaso(request):
    return render (request,'segundopaso.html')

@login_required
def segundopaso2(request):
    return render (request,'mis_talentos_s2.html')

@login_required
def frase_segundopaso(request):
    return render (request,'frase_segundopaso.html')

@login_required
def presentacion_segundopaso(request):
    return render (request,'presentacion_segundopaso.html')

@login_required
def instruccionestest_segundopaso(request):
    return render (request,'instruccionestest_segundopaso.html')

@login_required
def test_segundopaso(request):
    return render (request,'test_segundopaso.html')

