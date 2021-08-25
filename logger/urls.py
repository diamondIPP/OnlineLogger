from django.urls import path
from . import views

app_name = 'logger'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),  # index of the last 20 run logs
    path('<int:runnr>/', views.detail, name='detail'),  # detail for one run
    path('all/', views.all_, name='all'),  # display all (same as /all in index)
]
