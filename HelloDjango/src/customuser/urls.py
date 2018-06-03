'''
Created on 2018. 5. 26.

@author: Jihyo
'''
from django.urls import path
from .views import *
from django.contrib.auth import views
#from .view import sign

app_name = 'customuser'

urlpatterns = [
     path('sign/', sign, name = 'sign'),
     path('Login/', views.login, name = 'Login'),
     path('Logout/', views.logout, name = 'Logout'),
#     path('Login/', login, name = 'Login'), 
#     path('Logout/', logout, name = 'Logout'), 
    ]
