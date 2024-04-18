from django.db import models
from django.contrib.auth.models import User

class TopicType(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=255)
    type = models.ForeignKey(TopicType, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class FavoriteTopic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    body = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)