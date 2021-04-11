from django.urls import re_path, path
from basic_app import views

app_name = 'basic_app'

urlpatterns= [
    path('relative',views.relative,name='relative'),
    path('other',views.other,name='other'),
]
