from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<runnr>[0-9]+)/$', views.detail, name='detail'), #detail for one run
    url(r'^all/', views.all, name='all'), #display all (same as /all in index)
]
