from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from Accounting.models import recording,Project

def record_list(request):

    records=recording.objects.all()

    context={
        'records':records
    }
    return render(request,'html/record_list.html',context)

def record_details(request,record_id):
    
    record=get_object_or_404(recording,pk=record_id)
    context={
        'record':record

    }
    return render(request,'html/record_details.html',context)