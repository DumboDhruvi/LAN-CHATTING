from django.db import models

class Message(models.Model):
    username = models.CharField(max_length=150)
    content = models.TextField()
    group_name = models.CharField(max_length=150)  # New field for group name
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} in {self.group_name}: {self.content} at {self.timestamp}"