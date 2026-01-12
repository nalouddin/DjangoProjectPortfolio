from django.shortcuts import render
from .forms import ProjectForm
from project.models import Project, Review


# Create your views here.

def projects(request):
    reviews_p = Review.objects.filter(value='+')
    reviews_m = Review.objects.filter(value='-')
    projects = Project.objects.filter(project_reviews__isnull=True)
    context = {
        'projects': projects,
        'reviews_p': reviews_p,
        'reviews_m': reviews_m,
    }
    return render(request, 'project_list.html', context)

def project_detail(request, pk):
    project = Project.objects.get(id=pk)
    tags = project.tags.all()
    context = {
        'project': project,
        'tags': tags,
    }
    return render(request, 'project.html', context)

def project_add(request):
    form = ProjectForm()
    context = {
        'form': form,
    }
    return render(request, 'project_add.html', context)
