from django.conf.urls import url
from account import views

urlpatterns = [
    url(r'^registration/$',views.registration,name='registartion'),
    url(r'^login/$',views.login,name='login'),
    url(r'^edit/$',views.edit,name='edit'),
    
    
]