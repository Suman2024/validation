from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
# Create your views here.

def validating(request):
    SF=StudentForm()
    d={'SF':SF}

    if request.method=='POST':
        FD=StudentForm(request.POST)
        if FD.is_valid():
            return HttpResponse('valid form')
    return render(request,'validate_forms.html',d)