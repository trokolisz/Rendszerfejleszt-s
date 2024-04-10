from django.http import HttpResponse
from django.shortcuts import render
from .models import Topic, TopicType, Comment, User

def index(request):
    get_username= request.GET.get('user', -1)
    get_password = request.GET.get('pass', -1)
    get_topic_types =  request.GET.get('type', -1)
    if get_username in [-1, ''] or get_password in [-1, ''] :
        return render(request, 'login.html')
    try:
        #elenörzi a jelszó username párost
        
        User.objects.get(username=get_username, password=get_password)
        
    except:
        return render(request, 'login.html')
    
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
    return HttpResponse('Log in:')




