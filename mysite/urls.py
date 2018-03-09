from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/',include(admin.site.urls)),
    url(r'^blog/',include('blog.urls',namespace='blog',app_name='blog')),
    url(r'^account/',include('account.urls',namespace='account',app_name='account')),
]
