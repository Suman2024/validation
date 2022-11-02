from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.

def validate_forms(request):
    sf=Studentform()
    d={'form':sf}
    if request.method=='POST':
        form_data=Studentform(request.POST)
        if form_data.is_valid():
            return HttpResponse(str(form_data.cleaned_data))
    return render(request,'validate_forms.html',d)