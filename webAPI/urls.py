from django.urls import re_path as url

from webAPI import views

urlpatterns = [
    url(r'^indexingpipeline', views.indexingpipeline, name='indexingpipeline'),
    url(r'^genericsearch', views.genericsearch, name='genericsearch'),
    url(r'^aggregates', views.aggregates, name='aggregates')
]
