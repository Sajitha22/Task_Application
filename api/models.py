from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
 task_name=models.CharField(max_length=200)
 user=models.ForeignKey(User,on_delete=models.CASCADE)
 created_date=models.DateTimeField(auto_now_add=True)
 status=models.BooleanField(default=False)


 def _str_(self):
    return self.task_name