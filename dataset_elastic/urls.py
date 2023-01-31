from django.urls import re_path

from dataset_elastic import views

urlpatterns = [
    # url(r'^index', views.index, name='index'),
    re_path(r'^home', views.home, name='home'),
    re_path(r'^result', views.home, name='result'),
    re_path(r'^search', views.search_index, name='search_index'),
    re_path(r'^rest', views.rest, name='rest'),
    # re_path(r'^indexingpipeline', views.indexingpipeline, name='indexingpipeline'),
    re_path(r'^genericsearch', views.genericsearch, name='genericsearch'),
    re_path(r'^aggregates', views.aggregates, name='aggregates')

]
