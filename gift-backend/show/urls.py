from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show-questions/', views.show_questions, name='show_questions'),
    path('ver/', views.ver, name='ver'),
    path('get-score/', views.get_score, name='get_score'),
    path('change-score/', views.change_score, name='change_score'),
]
