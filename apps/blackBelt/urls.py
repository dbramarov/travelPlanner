from django.conf.urls import url, include
#from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='my_index'),
    url(r'^plans$', views.plan, name='plans'),
    url(r'^addTrip$', views.addTrip, name='addTrip'),
    url(r'^display/(?P<id>\d+)$', views.display, name='display'),
    url(r'^join/(?P<id>\d+)$', views.join, name='join')
]
