from django.http import HttpResponse
from rest_framework import generics
from .serializers import CommentSerializer
from django.shortcuts import render
from .models import Topic, TopicType, Comment, User

def index(request):
    get_username= request.GET.get('user', -1)
    get_password = request.GET.get('pass', -1)
    get_topic_types =  request.GET.get('type', -1)
    if get_username in [-1, ''] or get_password in [-1, ''] :
        return (login(request=request))
    try:
        #elenörzi a jelszó username párost
        
        User.objects.get(username=get_username, password=get_password)
        
    except:
        return (login(request=request))
    
    #return HttpResponse((username, password))
    topics =  Topic.objects.all()
    topic_types = TopicType.objects.all()
    if get_topic_types in [-1, '']:
        topics =  Topic.objects.all()
    else: 
    #   return HttpResponse(get_topic_types)
        topics =  Topic.objects.filter(type_id=get_topic_types)
    
    
    return render(request, 'index.html', {'topics': topics, "topic_types":topic_types})

def login(request):
    return render(request, 'login.html')




def topic(request):
    get_username= request.GET.get('user', -1)
    get_password = request.GET.get('pass', -1)
    if get_username in [-1, ''] or get_password in [-1, ''] :
        return (login(request=request))
    try:
        #elenörzi a jelszó username párost
        
        User.objects.get(username=get_username, password=get_password)
    except:
        return (login(request=request))
    get_topic =  request.GET.get('topic', -1)
    if get_topic in [-1, '']:
        return index(request=request)
    try:
        Topic.objects.get(id=get_topic)
    except:
        return index(request=request)
            
    topics =  Topic.objects.filter(id=get_topic)
    comments = Comment.objects.filter(topic_id=get_topic)
    return render(request, 'topic.html', {'topic': topics[0], 'comments':comments})


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer