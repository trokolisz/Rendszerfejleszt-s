# myapp/admin.py

from django.contrib import admin
from .models import User, Topic, FavoriteTopic, TopicType, Comment

admin.site.register(User)
admin.site.register(Topic)
admin.site.register(FavoriteTopic)
admin.site.register(TopicType)
admin.site.register(Comment)


