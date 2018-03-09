from django import forms
from django.contrib.auth.models import User
from account.models import profile_info
class User_registration(forms.Form):
    username=forms.CharField(widget=forms.TextInput(
                attrs={'class':'form-control','placeholder':'enter your name'}),required=True,max_length=30)
    email=forms.EmailField(widget=forms.EmailInput(
    attrs={'class':'form-control','placeholder':'Enter your email'}),required=True,max_length=50)

    password=forms.CharField(widget=forms.PasswordInput(
    attrs={'class':'form-control','placeholder':'Enter your password'}),required=True,max_length=10)

    confirm_password=forms.CharField(widget=forms.PasswordInput(
    attrs={'class':'form-control','placeholder':'confirm your password'}),required=True,max_length=10)
    

    class Meta():
        model=User
        fields=['username','email','password','confirm_password']

class User_login(forms.Form):
    username=forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Username'}
    ),required=True,max_length=30)
    password=forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control','placeholder':'password'}
    ),required=True,max_length=10)

class edit(forms.ModelForm):
    full_name=forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'enter full name'}
    ),required=True,max_length=30)
    email=forms.EmailField(widget=forms.EmailInput(
        attrs={'class':'form-control','placeholder':'enter your email'}
    ),required=True,max_length=50)
    college_name=forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'enter college name'}
    ),required=True,max_length=30)
    office_name=forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'office_name'}
    ),required=True,max_length=50)
    phone_number=forms.IntegerField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'enter phone number'}
    ))
    class Meta():
        model=profile_info
        fields=['full_name','email','college_name','office_name','phone_number']


    
