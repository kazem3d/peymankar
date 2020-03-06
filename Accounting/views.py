from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from Accounting.models import recording,Project
from django.urls import reverse
from Accounting.forms import SearchForm,RegisterRecordForm,ProjectForm
from django.db.models import  Sum,Avg

def home(request):
    return render(request,"html/home_page.html")



def record_list(request):
    search_form=SearchForm(request.GET)

    records=recording.objects.filter(types='1')
    expense_sum=records.aggregate(jam=Sum('total_price'))
    expense_sum=list(expense_sum.values())[0]

    records=recording.objects.filter(types='2')
    income_sum=records.aggregate(jam=Sum('total_price'))
    income_sum=list(income_sum.values())[0]
    
    
    records=recording.objects.all()

    if search_form.is_valid():
        
        

        records=records.filter(title__contains=search_form.cleaned_data['record_name'])
        if search_form.cleaned_data['type_of'] is not None :
            records=records.filter(types=search_form.cleaned_data['type_of'])
        if search_form.cleaned_data['project_name'] is not None:
            records=records.filter(project=search_form.cleaned_data['project_name'])
        if search_form.cleaned_data['max_price'] is not None:
            records=records.filter(total_price__lte =search_form.cleaned_data['max_price'])
        if search_form.cleaned_data['min_price'] is not None:
            records=records.filter(total_price__gte =search_form.cleaned_data['min_price'])


        

   
    context={
        'records':records,
        'search_form':search_form,
        'expense_sum':expense_sum,
        'income_sum':income_sum
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

def record_edit(request,record_edit_id):

    record=recording.objects.get(id=record_edit_id)
    if request.method == "POST" :
         edit_form=RegisterRecordForm(request.POST,instance=record)
         if edit_form.is_valid():
             edit_form.save()
             
             return HttpResponseRedirect(reverse('accounting:record_details', args=(record.id,) ))
    else:
        edit_form=RegisterRecordForm(instance=record)


    context={
        'edit_form' :  edit_form
    }

    return render(request,'html/edit_record.html',context)

def project_register(request):
    
    if request.method == 'POST':
        project=ProjectForm(request.POST)
        if project.is_valid():
            project.save()
            return HttpResponseRedirect(reverse('accounting:record_list'))
    else:
        project=ProjectForm()

    context={
        'project':project
    }
    return render(request,'html/register_project.html',context)

def projects_list(request):
    projects=Project.objects.all()
    context={
        'projects':projects
    }

    return render(request,'html/projects_list.html',context)

def project_details(request,project_id):

    projects=get_object_or_404(Project,id=project_id)
    context={
        'projects':projects
    }
    return render(request,'html/project_details.html',context)

def project_edit(request,project_edit_id):
    
    project=Project.objects.get(id=project_edit_id)
    if request.method == 'POST':
            project_form=ProjectForm(request.POST,instance=project)
            if project_form.is_valid():
                project_form.save()
                return HttpResponseRedirect(reverse('accounting:project_details', args=(project.id,) ))
    else:


        project_form=ProjectForm(instance=project)

    context={
        'project_form':project_form
    }
    return render(request,'html/project_edit.html/',context)

def about_us(request):

    return render(request,'html/about_us.html/')
    