from rest_framework import serializers
from .models import Comment  # Import your Comment model

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'