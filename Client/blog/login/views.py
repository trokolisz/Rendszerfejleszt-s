from django.http import HttpResponse
from django.shortcuts import render
from .models import Topic, TopicType, Comment, User

def index(request):
    user_id= request.GET.get('user', -1)
    password = request.GET.get('pass', -1)
    if user_id in [-1, ''] or password in [-1, ''] :
         return render(request, 'login.html')
    try:
        #user_id=int(user_id)
        
            users = User.objects.get(username=user_id)
        
    except:
        users = 1
        
    #return HttpResponse((users, password))
    #comments = Comment.objects.all()
    topics =  Topic.objects.filter()
    
    topic_types = TopicType.objects.all()
    return render(request, 'index.html', {'topics': topics, "topic_types":topic_types})

def login(request):
    return HttpResponse('Log in:')




