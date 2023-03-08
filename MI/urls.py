from MI.views import *
from django.urls import path
app_name='Mumbai_Indians'

urlpatterns=[
    path('rohit/',rohit,name='rohit'),
    path('sachin/',sachin,name='sachin'),
    path('surya/',surya,name='surya'),
]