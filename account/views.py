from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from account.forms import User_registration,User_login,edit
from django.contrib import messages
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def registration(request):
    if request.method=='POST':
        reg_form=User_registration(request.POST)
        if reg_form.is_valid():
            username=reg_form.cleaned_data['username']
            email=reg_form.cleaned_data['email']
            password=reg_form.cleaned_data['password']
            User.objects.create_user(username=username,email=email,password=password)
            messages.success(request,"You have been successfully registered")

            
            return HttpResponseRedirect('')
    else:
        reg_form=User_registration()

    return render(request,'account/registration.html',{'reg_form':reg_form})

def login(request):
    if request.method=='POST':
        log_form=User_login(request.POST)
        if log_form.is_valid():
            username=log_form.cleaned_data['username']
            password=log_form.cleaned_data['password']
            try:
                user=auth.authenticate(username=username,password=password)
                if user is not None:
                    auth.login(request,user)
                    return HttpResponseRedirect('/blog/')
                else:
                    messages.error(request,"Username and password didn't matched")
            except auth.ObjectDoesNotExist:
                print("invalid user")
        return render(request,'account/login.html',{'log_form':log_form})
        
def edit(request):
    if request.method=='POST':
        edit_form=edit(request.POST)
        if edit_form.is_valid():
            full_name=edit_form.cleaned_data['full_name']
            email=edit_form.cleaned_data['email']
            college_name=edit_form.cleaned_data['college_name']
            office_name=edit_form.cleaned_data['office_name']
            phone_number=edit_form.cleaned_data['phone_number']

            return HttpResponseRedirect('/edit/')
        else:
            messages.error(request,"please fill the form")

        return render(request,'account/edit.html',{'edit_form':edit_form})


            
            
            