from django.shortcuts import render
from django.http import HttpResponse
from Accounting.models import recording

def record_list(request):

    records=recording.objects.all()

    context={
        'records':records
    }
    return render(request,'html/record_list.html',context)

