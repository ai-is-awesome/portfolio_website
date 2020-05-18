from django.shortcuts import render
from .models import Project
# Create your views here.


def index(request):
	projects = Project.objects.all()
	project = projects[0]
	context = {'projects': projects, 
				'project' : project
				}
	return render(request, 'post/index.html', context)


def project_detail(request, pk):
	project = Project.objects.get(id = pk)
	context = {'project' : project}
	return render(request, 'post/project_detail.html', context)

