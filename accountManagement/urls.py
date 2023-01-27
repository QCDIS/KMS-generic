from django.conf.urls import include
from django.urls import re_path as url
from accountManagement import views,models
from django.conf.urls.static import static


urlpatterns = [
	#re_path(r'^index', views.index, name='index'),
    re_path(r'^login', views.login, name='login'),
]
