from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'ajax/suggestionname', views.suggestionName, name = 'suggestionName'),
    url(r'ajax/data', views.data, name = 'data'),
    url(r'^$', views.home, name = 'home'),
]
