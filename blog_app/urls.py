from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FavoriteTopicViewSet, TopicViewSet, CommentViewSet, TopicTypeViewSet
from . import views
from django.contrib.auth.views import LoginView, LogoutView

router = DefaultRouter()
router.register(r'favorite_topics', FavoriteTopicViewSet)
router.register(r'topics', TopicViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'topic_type', TopicTypeViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.index, name='index'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('accounts/profile/', views.profile_view, name='profile'),
    path('topic/', views.topic, name='topic'),
    path('my_comments/', views.my_comments, name='my_comments'),
    path('favorites/', views.favorites, name='favorites'),
]

