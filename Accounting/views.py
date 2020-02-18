from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from Accounting.models import recording,Project

from Accounting.forms import SearchForm

def record_list(request):
    search_form=SearchForm(request.GET)
    if search_form.is_valid():
        record_name=search_form.cleaned_data['record_name']
        records=recording.objects.filter(title__contains=record_name)
    else:


        records=recording.objects.all()

    context={
        'records':records,
        'search_form':search_form
    }
    return render(request,'html/record_list.html',context)

def record_details(request,record_id):
    
    record=get_object_or_404(recording,pk=record_id)
    context={
        'record':record

    }
    return render(request,'html/record_details.html',context)