from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('mbti_check/', views.mbti_check, name='mbti_check'),
    path('mbti_share/<int:user_id>/', views.mbti_share, name='mbti_share'),
]
