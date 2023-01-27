from django.conf.urls import include
from django.urls import re_path
from webAPI import views,models
from django.conf.urls.static import static


urlpatterns = [
    re_path(r'^indexingpipeline', views.indexingpipeline, name='indexingpipeline'),
    re_path(r'^genericsearch', views.genericsearch, name='genericsearch'),
    re_path(r'^aggregates', views.aggregates, name='aggregates')
]
