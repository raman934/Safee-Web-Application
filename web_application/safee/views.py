from django.shortcuts import render

posts = [
	{
		'author': 'Raman Gandhi',
		'title': 'Safee - Web Application',
		'content': 'Template Creation Undergoing',
		'date_posted': 'April 28, 2020'
	}
]

def home(request):
	context = {
		'posts': posts, 
		'title': 'safee'
	}
	return render(request, 'safee/home.html', context)

def about(request):
	return render(request, 'safee/about.html', {'title': 'safee-about'})

def index(request):
	return render(request, 'safee/index.html', {'title': 'safee-home'})

def generic(request):
	return render(request, 'safee/generic.html', {'title': 'safee-generic'})

def elements(request):
	return render(request, 'safee/elements.html', {'title': 'safee-elements'})