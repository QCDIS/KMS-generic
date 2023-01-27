from django.urls import re_path as url

from genericpages import views

urlpatterns = [
    # url(r'^index', views.index, name='index'),
    url(r'^genericpages', views.genericpages, name='genericpages'),
    url('', views.landingpage, name='landingpage'),
]
