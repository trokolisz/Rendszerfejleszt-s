from django.db import models


# Create your models here.
# class Login(models.Model):
#     name = models.CharField(max_length=32)
#     password = models.CharField(max_length=16)
#     e = models.IntegerField()
#     image_url = models.CharField(max_length=2083)
    


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Topic(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    type_id = models.ForeignKey('TopicType', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class FavoriteTopic(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    topic_id = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_id} likes {self.topic_id}"
    
class TopicType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    topic_id = models.ForeignKey(Topic, on_delete=models.CASCADE)
    body = models.CharField(max_length=255)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"Comment by {self.user_id} on {self.topic_id}"



