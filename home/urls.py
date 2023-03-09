from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mbti_test/', views.mbti_test, name='mbti_test'),
    path('results/', views.results, name='results'),
]