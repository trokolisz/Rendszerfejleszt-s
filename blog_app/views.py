from django.shortcuts import render
from rest_framework import viewsets, renderers, status
from rest_framework.response import Response
from .models import FavoriteTopic, Topic, TopicType
from .serializers import FavoriteTopicSerializer, TopicSerializer, TopicTypeSerializer
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.db.models import Q
from celery import shared_task
from django.core.mail import send_mail
import time
from django.contrib.auth.models import User

def logout_view(request):
    logout(request)
    return redirect('login')  # or redirect to wherever you want
# Create your views here.
def index(request):
    return render(request, 'index.html' )

def topic(request):
    topic_id = request.GET.get('id')
    if topic_id is None:
        return redirect('index')  # or redirect to wherever you want
    topic = Topic.objects.get(id=topic_id)
    if topic is None:
        return redirect('index')  # or redirect to wherever you want
    favorite_topics = FavoriteTopic.objects.filter(Q(topic=topic_id) & Q(user=request.user))
    return render(request, 'topic.html', {'topic': topic, 'favorite_topics': favorite_topics})

def favorites(request):
    return render(request, 'my_favorites.html')

def my_comments(request):
    
    return render(request, 'my_comments.html')

class FavoriteTopicViewSet(viewsets.ModelViewSet):
    queryset = FavoriteTopic.objects.all()
    serializer_class = FavoriteTopicSerializer   
    renderer_classes = [renderers.JSONRenderer]
    
    def get_queryset(self):
        user_id = self.request.query_params.get('user_id', None)
        if user_id is not None:
            return FavoriteTopic.objects.filter(user_id=user_id)
        return FavoriteTopic.objects.all()
    
    def destroy(self, request, *args, **kwargs):
        user_id = self.request.data.get('user')
        topic_id = self.request.data.get('topic')
        instances = self.queryset.filter(user=user_id, topic=topic_id)
        for instance in instances:
            self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
    

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    renderer_classes = [renderers.JSONRenderer]
    
    def get_queryset(self):
        topic_type = self.request.query_params.get('topic_type', None)
        if topic_type is not None:
            return Topic.objects.filter(type=topic_type)
        return Topic.objects.all()

from .models import Comment
from .serializers import CommentSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    renderer_classes = [renderers.JSONRenderer]
    
    def get_queryset(self):
        topic_id = self.request.query_params.get('topic_id', None)
        type_id = self.request.query_params.get('type_id', None)
        if topic_id is not None:
            return Comment.objects.filter(topic=topic_id)
        user = self.request.query_params.get('user', None)
        if user is not None:
            if type_id is not None:
                return Comment.objects.filter(user=user, topic__type=type_id)
            return Comment.objects.filter(user=user)
        
        return Comment.objects.all()
    
def profile_view(request):
    return render(request, 'profile.html')


class TopicTypeViewSet(viewsets.ModelViewSet):
    queryset = TopicType.objects.all()
    serializer_class = TopicTypeSerializer
    renderer_classes = [renderers.JSONRenderer]
    
    def get_queryset(self):
        return TopicType.objects.all()
    
@shared_task
def watch_topic_task(topic_id):
    topic = Topic.objects.get(pk=topic_id)
    last_count = topic.posts.count()

    while True:
        time.sleep(1)  # Wait for a while before checking again
        current_count = topic.posts.count()

        if current_count > last_count:
            users = User.objects.filter(is_watching_topic=topic)
            for user in users:
                send_mail(
                    'New post in watched topic',
                    'A new post has been added to the topic you\'re watching.',
                    'from@example.com',
                    [user.email],
                    fail_silently=False,
                )
            last_count = current_count