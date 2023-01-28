from django.urls import re_path as url

from notebookSearch import views

urlpatterns = [
    url(r'^genericsearch', views.genericsearch, name='genericsearch'),
    url(r'^github_index_pipeline', views.github_index_pipeline, name='github_index_pipeline')

]
