from django.http import HttpResponse
from django.shortcuts import render
from .models import Topic, TopicType, Comment, User

def index(request):
    username= request.GET.get('user', -1)
    password = request.GET.get('pass', -1)
    
    if username in [-1, ''] or password in [-1, ''] :
        return render(request, 'login.html')
    try:
        #user_id=int(user_id)
        
            User.objects.get(username=username, password=password)
        
    except:
        return render(request, 'login.html')
        
    #return HttpResponse((users, password))
    #comments = Comment.objects.all()
    topics =  Topic.objects.all()
    
    topic_types = TopicType.objects.all()
    return render(request, 'index.html', {'topics': topics, "topic_types":topic_types})

def login(request):
    return HttpResponse('Log in:')




