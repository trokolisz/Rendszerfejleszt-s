from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/topic/(?P<topic_name>\w+)/$', consumers.TopicConsumer.as_asgi()),
]
