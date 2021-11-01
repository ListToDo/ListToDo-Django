from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tasks.views import ProjectsAPI, MyProjectsAPI, LabelAPI, MyLabelsAPI

urlpatterns = [
    path('project/', ProjectsAPI.as_view()),
    path('project/<int:pk>/', ProjectsAPI.as_view()),
    path('projects/', MyProjectsAPI.as_view()),

    path('label/', LabelAPI.as_view()),
    path('label/<int:pk>/', LabelAPI.as_view()),
    path('labels/', MyLabelsAPI.as_view()),
]