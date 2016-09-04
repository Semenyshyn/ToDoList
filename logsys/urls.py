from django.conf.urls import url
from . import views

app_name = 'logsys'
urlpatterns = [
    url(r'^login/', views.log_in),
    url(r'^logout/', views.log_out),
    url(r'^singup/', views.sing_up)

]
