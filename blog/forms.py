from django import forms
from .models import Comment
class EmailPostForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(
                attrs={'class':'form-control','placeholder':'enter your name'}),required=True,max_length=30)
    email=forms.EmailField(widget=forms.EmailInput(
    attrs={'class':'form-control','placeholder':'Enter your email'}),required=True,max_length=50)
    to=forms.EmailField(
    widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'enter receivers email address',}),required=True,max_length=50
    )
    comments=forms.CharField(widget=forms.Textarea(
    attrs={'class':'form-control','placeholder':'enter your message',}
    ),required=True,max_length=250)


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','email','body')
