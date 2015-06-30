from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<runnr>[0-9]+)/$', views.detail, name='detail'),
]
