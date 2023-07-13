from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add= True, auto_now= False, blank= True)
    updated_at = models.DateTimeField(auto_now= True, blank= True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=180)
    desc = models.CharField(max_length=400)
    published = models.BooleanField(default= False, blank= True)
    created_at = models.DateTimeField(auto_now_add= True, auto_now= False, blank= True)
    updated_at = models.DateTimeField(auto_now= True, blank= True)
    user = models.ForeignKey(User, on_delete= models.CASCADE, blank= True, null= True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name    