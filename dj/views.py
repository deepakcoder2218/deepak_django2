from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    params = {'name': request.GET.get('name','')}
    return render (request,'index.html', params)

def contact(request):
    return HttpResponse("this is our new web page")