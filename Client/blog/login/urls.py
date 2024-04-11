from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt



urlpatterns = [
    path('', views.index),
    path('login/', views.login),
    path('topic/', views.topic),
    # List and create comments
    path('api/comments/', views.CommentListCreateView.as_view(), name='comment-list-create'),
    # Retrieve, update, and delete a specific comment
    path('api/comments/<int:pk>/', views.CommentRetrieveUpdateDestroyView.as_view(), name='comment-detail'),
    path('comment/', csrf_exempt(views.comment)),
    path('favorites/', csrf_exempt(views.favorites)),
]
