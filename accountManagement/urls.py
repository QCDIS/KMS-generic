from django.urls import re_path as url

from accountManagement import views

urlpatterns = [
    # url(r'^index', views.index, name='index'),
    url(r'^login', views.login, name='login'),
]
