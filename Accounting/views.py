from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from Accounting.models import recording,Project
from django.urls import reverse
from Accounting.forms import SearchForm,RegisterRecordForm

def record_list(request):
    search_form=SearchForm(request.GET)
    records=recording.objects.all()
    if search_form.is_valid():
       
        records=records.filter(title__contains=search_form.cleaned_data['record_name'])
        if search_form.cleaned_data['project_name'] is not None:
            records=records.filter(project=search_form.cleaned_data['project_name'])
        if search_form.cleaned_data['max_price'] is not None:
            records=records.filter(total_price__lte =search_form.cleaned_data['max_price'])
        if search_form.cleaned_data['min_price'] is not None:
            records=records.filter(total_price__gte =search_form.cleaned_data['min_price'])


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


def record_register(request):

    if request.method == 'POST':
        record_form=RegisterRecordForm(request.POST)
        if record_form.is_valid():
            record_form.save()

            return HttpResponseRedirect(reverse('accounting:record_list'))
    else:
        record_form=RegisterRecordForm()
        
               

    context={
        'record_form' : record_form
    }
    return render(request,'html/record_register.html',context)