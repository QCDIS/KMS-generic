from django.conf.urls import include
from django.urls import re_path as url
from DSS import views,models
from django.conf.urls.static import static


urlpatterns = [
    re_path(r'^numberOfSolutions', views.numberOfSolutions, name='numberOfSolutions'),
    re_path(r'^listOfSolutions', views.listOfSolutions, name='listOfSolutions'),
    re_path(r'^detailedSolution', views.detailedSolution, name='detailedSolution')
]
