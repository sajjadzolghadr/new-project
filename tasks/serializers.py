from rest_framework import serializers
from .models import Task #add api for tasks
from django.contrib.auth.models import User

#add api for tasks
class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'
        

# add api for user 
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only =True)

    class Meta :
        model = User
        fields = ['id', 'username','password']

    def create(self,validateed_date):
        user = User.objects.create_user(
            username=validateed_date['username'],
            password=validateed_date['password']
        )
        return user


        