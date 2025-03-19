from django.test import TestCase

from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Task
from .serializers import UserSerializer
from django.urls import reverse


# add unit test for task and user
class TaskTestCase(APITestCase):
    def setUp(self):
       
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client = APIClient() 
        self.client.force_authenticate(user=self.user) 
        self.task = Task.objects.create(title="Test Task", description="Test Description", completed=False , user=self.user,
    category=None)
        
    def test_create_task(self):
    
        url = reverse('task-list')  
        data = {"title": "New Task", "description": "Some details", "completed": False, "user": self.user.id}
        
      
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  
        self.assertEqual(Task.objects.count(), 2)  

