from rest_framework import serializers
from .models import FavoriteTopic, Topic, TopicType

class FavoriteTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteTopic
        fields = ['id', 'user', 'topic']
        


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'name', 'description']  # replace with your actual fields
        
from .models import Comment
from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)  # specify the desired format here and set read_only=True
    username = serializers.CharField(source='user.username', read_only=True)  # add this line to include the username and set read_only=True
    topic_name = serializers.CharField(source='topic.name', read_only=True)
    type_id = serializers.CharField(source='topic.type.id', read_only=True)
        
    class Meta:
        model = Comment
        fields = ['id', 'user', 'username', 'topic', 'body', 'timestamp', 'topic_name', 'type_id']  # replace with your actual fields
        read_only_fields = ['timestamp', 'username', 'topic_name', 'type_id']  # add the read_only_fields attribute to specify the read-only fields
        
        
class TopicTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicType
        fields = ['id', 'name']  # replace with your actual fields