from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name="j"),
    path('login/', views.login)
]
