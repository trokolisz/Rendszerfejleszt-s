from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response

from .serializers import CommentSerializer
from django.shortcuts import render, get_object_or_404
from .models import Topic, TopicType, Comment, User
from django.http import JsonResponse

def index(request):
    get_username= request.GET.get('user', -1)
    get_password = request.GET.get('pass', -1)
    get_topic_types =  request.GET.get('type', -1)
    if get_username in [-1, ''] or get_password in [-1, ''] :
        return (login(request=request))
    try:
        #elenörzi a jelszó username párost
        
        my_user = User.objects.get(username=get_username, password=get_password)
        
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
    user = get_object_or_404(User, username=get_username)
    user_id = user.id
    topics =  Topic.objects.filter(id=get_topic)
    comments = Comment.objects.filter(topic_id=get_topic)
    return render(request, 'topic.html', {'topic': topics[0], 'comments':comments, 'user_id':user_id})
@csrf_exempt
@api_view(['GET', 'POST'])
def comment(requests):
    if requests.method == 'GET':
        comments= Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return JsonResponse({'message': serializer.data})
    if requests.method == 'POST':
        serializer= CommentSerializer(data=requests.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    
def my_api_view(request):
    if request.method == 'POST':
        data = request.POST  # Change this to request.body for JSON data
        # Process the data and return a response
        return JsonResponse({'message': 'Data received successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    
    

    