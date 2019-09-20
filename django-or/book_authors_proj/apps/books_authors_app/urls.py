from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^authors$', views.index2),

    #Book
    url(r'^add$', views.add),
    url(r'^view/(?P<id>\d+)$', views.view),
    url(r'^add_author/(?P<id>\d+)$', views.add_author),

    #Author
    url(r'^add_an_author$', views.add_an_author),
    url(r'^view_an_author/(?P<id>\d+)$', views.view_an_author),
    url(r'^add_book/(?P<id>\d+)$', views.add_book)



]