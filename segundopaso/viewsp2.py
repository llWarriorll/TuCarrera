from django.shortcuts import render
from django.contrib.auth.decorators import login_required



@login_required
def segundopaso(request):
    return render (request,'segundopaso.html')
