from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    name_text = models.CharField(max_length=200)
    description_text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    date_to_finish = models.DateTimeField('date finished')
    task_from = models.ForeignKey(User)
