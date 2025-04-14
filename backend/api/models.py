from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# This model represents a note created by a user.
# It contains fields for the title, content, creation date, and the user who created it.
class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    

    def __str__(self):
        return self.title


