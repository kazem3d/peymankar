from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def record_list(request):
    return render(request,'html/index.html')

