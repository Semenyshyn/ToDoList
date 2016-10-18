from django.conf.urls import url
from . import views

app_name = 'logsys'
urlpatterns = [
    url(r'^login/', views.log_in, name='login'),
    url(r'^logout/', views.log_out, name='logout'),
    url(r'^singup/', views.sing_up, name='sing_up')
]
