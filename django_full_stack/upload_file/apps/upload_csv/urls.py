from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.index), 
    url(r'^upload_csv$', views.upload_csv), 
]
