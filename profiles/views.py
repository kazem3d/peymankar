from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse


def login_view(request):
    next_url = request.GET.get('next')

    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:

            login(request,user)
            redirect_url = next_url if next_url else reverse('accounting:about_us')
            return HttpResponseRedirect(redirect_url)
        else:
            context={
                'username':username,
                'error':'نام کاربری یافت نشد'
            }
            
    else:
        context={}
       
       
    return render(request,'profiles/login.html',context)    



    

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))