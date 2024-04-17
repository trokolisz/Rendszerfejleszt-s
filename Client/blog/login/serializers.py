from rest_framework import serializers
from .models import Comment, FavoriteTopic  # Import your Comment model

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'body', 'timestamp', 'topic_id', 'user_id' ]
        
        
class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteTopic
        fields = ['id', 'topic_id', 'user_id' ]
        