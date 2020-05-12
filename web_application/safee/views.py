from django.shortcuts import render
from .models import Post

def home(request):
	context = {
		'posts': Post.objects.all(), 
		'title': 'safee'
	}
	return render(request, 'safee/home.html', context)

def about(request):
	return render(request, 'safee/about.html')

def index(request):
	return render(request, 'safee/index.html', {'title': 'safee-home'})

def generic(request):
	return render(request, 'safee/generic.html', {'title': 'safee-generic'})

def elements(request):
	return render(request, 'safee/elements.html', {'title': 'safee-elements'})
