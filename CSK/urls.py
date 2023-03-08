from CSK.views import *
from django.urls import path
app_name='Chennai_Super_kings'

urlpatterns=[
    path('dhoni/',dhoni,name='dhoni'),
    path('raina/',raina,name='raina'),
    path('jadeja/',jadeja,name='jadeja')
]