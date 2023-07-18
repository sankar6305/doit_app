from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TodoItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=500)
    desc = models.CharField(max_length=400, blank=True, null=True)
    priority = models.CharField(max_length=10)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['priority']
