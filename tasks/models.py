from django.db import models
from django.contrib.auth.models import User

#add Category
class Category(models.Model):
    name = models.CharField(max_length=255)

class Task (models.Model):
    title = models.CharField(max_length =250)
    description = models.TextField(blank=True , null=True )
    completed = models.BooleanField(default =False)
    created_date = models.DateTimeField(auto_now_add = True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True , blank=True)
    #connecting user to task
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__ (self):
        return self.title




