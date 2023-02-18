from rest_framework import serializers
from api.models import Task
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    created_date=serializers.DateTimeField(read_only=True)
    status=serializers.BooleanField(read_only=True)
    user=serializers.CharField(read_only=True)
    class Meta:
        model=Task
        fields="__all__"


# .........................localhost:8000/users/.........
class UserSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=User
        fields=["id","username","password","email","first_name","last_name"]        