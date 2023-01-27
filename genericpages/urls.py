from django.conf.urls import include
from django.urls import re_path as url
from genericpages import views,models
from django.conf.urls.static import static
urlpatterns = [
	#re_path(r'^index', views.index, name='index'),
    re_path(r'^genericpages', views.genericpages, name='genericpages'),
    re_path('', views.landingpage, name='landingpage'),
]
