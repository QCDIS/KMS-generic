from django.conf.urls import include
from django.urls import re_path as url
from notebookSearch import views,models
from django.conf.urls.static import static


urlpatterns = [
    re_path(r'^genericsearch', views.genericsearch, name='genericsearch'),
    re_path(r'^github_index_pipeline', views.github_index_pipeline, name='github_index_pipeline')
]


