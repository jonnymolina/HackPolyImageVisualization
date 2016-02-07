from django.conf.urls import url
from photos import views

urlpatterns = [
    url(r'^run/$', views.Setup.as_view(), name='setup'),
    url(r'^load/$', views.Load.as_view(), name='load'),
    url(r'^clear/$', views.Clear.as_view(), name='clear'),
    url(r'^list/$', views.PhotoList.as_view(), name='list'),
]