from django.urls import path

from .views import projects, project_detail, project_add
urlpatterns = [
    path('', projects, name='projects'),
    path('project/<uuid:pk>/', project_detail, name='project-detail'),

    path('project_add/', project_add, name='project-add'),
]