from django.conf.urls import url
from . import views

app_name = 'task'
urlpatterns = [
    url(r'^$', views.tasks),
    url(r'^addtask/', views.add_task)
]
