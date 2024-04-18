from django.contrib import admin
from .models import User, Topic, FavoriteTopic, TopicType, Comment



class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'description')  # replace 'name' with your actual field

class FavoriteTopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic')  # replace 'name' with your actual field

class TopicTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # replace 'name' with your actual field

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'body', 'user', 'topic', 'timestamp')


admin.site.register(Topic, TopicAdmin)
admin.site.register(FavoriteTopic, FavoriteTopicAdmin)
admin.site.register(TopicType, TopicTypeAdmin)
admin.site.register(Comment, CommentAdmin)