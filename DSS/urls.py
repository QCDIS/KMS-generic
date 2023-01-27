from django.urls import re_path as url

from DSS import views

urlpatterns = [
    url(r'^numberOfSolutions', views.numberOfSolutions, name='numberOfSolutions'),
    url(r'^listOfSolutions', views.listOfSolutions, name='listOfSolutions'),
    url(r'^detailedSolution', views.detailedSolution, name='detailedSolution')
]
